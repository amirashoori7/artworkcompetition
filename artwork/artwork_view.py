from django.shortcuts import render, get_object_or_404
from artwork.artwork_models import Artwork, School, convert_to_df
from django.http import HttpResponse
import json
from artwork.artwork_forms import EntryForm, UserForm, UploadFileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from account.models_account import ProjectUser
import os
from django.core.mail import send_mail
from zipfile import ZipFile
from evaluation.models import D2, D1A, D1B, D3
from django.core.files.storage import FileSystemStorage
import zipfile
import pandas
from account.forms_account import UserRegistrationForm
from django.core.files.base import File
from artwork import utils


def index(request):
    context = {}
    return render(request, 'index.html', context)


def managerConsole(request):
    form = UploadFileForm()
    context = {'form' : form}
    return render(request, 'adminPages/admin_console.html', context)


def home(request):
    num_works = Artwork.objects.all().count()
    num_schools = School.objects.all().count()
    context = {
        'num_works': num_works,
        'num_schools': num_schools}
    return render(request, 'home.html', context)


def aboutus(request):
    context = {}
    return render(request, 'aboutus.html', context)


def contactus(request):
    context = {}
    return render(request, 'contactus.html', context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context)


def history(request):
    context = {}
    return render(request, 'history.html', context)


def howtoenter(request):
    context = {}
    return render(request, 'howtoenter.html', context)


def rules(request):
    context = {}
    return render(request, 'rules.html', context)


def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)


@login_required
def work_lists(request):
    status = request.GET.get('status', -2)
    if request.user.user_type == 2:  # judge 1
        works = Artwork.objects.filter(Q (status=4))
    elif request.user.user_type == 3:  # decision maker
        works = Artwork.objects.filter(Q (status=5))
    elif request.user.user_type == 4:  # Judge 2
        d2s = list(D2.objects.filter(author=request.user).values_list('artwork__id', flat=True))
        works = Artwork.objects.filter(Q (status=6, id__in=d2s))
#         .exclude(Q(id__in=d2s))
    elif request.user.user_type == 5:  # judge 3
        works = Artwork.objects.filter(Q (status=10))
    elif status == '-2':
        works = Artwork.objects.all()
    else:
        works = Artwork.objects.filter(status=status)
    works = works.order_by('-id')
    numberofartworks = Artwork.objects.filter(status__gte=0).count()
    numberoflearners = ProjectUser.objects.filter(user_type=1).count()
    context = {'works': works, 'numberofartworks': numberofartworks, 'numberoflearners':numberoflearners}
    return render(request, 'adminPages/work_lists.html', context)


@login_required
def work_lists_checkbox(request):
    grade = request.GET.get('grade', '')
    judge = request.GET.get('judge', '')
    judgeuser = ProjectUser.objects.get(username=judge)
    d2s = list(D2.objects.filter(author=judgeuser).values_list('artwork__id', flat=True))
    works = Artwork.objects.filter(learnergrade=grade, status=6).exclude(Q(id__in=d2s))
    works = works.order_by('-id')
    context = {'works': works}
    return render(request, 'adminPages/work_lists_checkbox.html', context)


def getStatusDisplay(status):
    strt = str(utils.Status(status))
    strt = strt.replace("Status.", "")
    strt = strt.replace("_", " ")
    return strt


def getfile(request):  
    artworks = Artwork.objects.all().order_by("-id")  # status__gte=0
    d2s = D2.objects.all().order_by("-id")  # status__gte=0
    d3s = D3.objects.all().order_by("-id")  # status__gte=0
    users = ProjectUser.objects.all()
    fieldsArtwork = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__cellphone',
              'owner__dob', 'owner__parentname', 'owner__parentemail', 'owner__parentphone',
              'school__province', 'school__name', 'school__natemis', 'id', 'status', 'worktitle', 'workfile',
                  'learnergrade', 'workformulafile', 'teachername',
                  'teacheremail', 'teacherphone', 'question1',
                  'question2', 'question3']
    fieldsUser = ['username', 'dob', 'user_type', 'cellphone',
              'organisation', 'parentname', 'grade', 'parentphone',
              'parentmail', 'id']
    df = convert_to_df(artworks, fieldsArtwork)
    users = convert_to_df(users, fieldsUser)
    d2s = convert_to_df(d2s, None)
    d3s = convert_to_df(d3s, None)
    df['work status'] = df.apply(lambda x: getStatusDisplay(x['status']), axis=1)
    df['Unique Id'] = df.apply(lambda x: calc_uid(int(x['id'])), axis=1)
    df = df.drop(columns=['status'])
    df = df.drop(columns=['id'])
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SITE_ROOT = os.path.join(BASE_DIR, 'media')
    csvfilename = os.path.join(SITE_ROOT, "artworklist.xlsx")
    zipfilename = os.path.join(SITE_ROOT, "backupFile.zip")
    df.to_excel(csvfilename,
             sheet_name='artwork')
    with pandas.ExcelWriter(csvfilename,
                    mode='a') as writer:  
        d2s.to_excel(writer, sheet_name='Judge 2')
    with pandas.ExcelWriter(csvfilename,
                    mode='a') as writer2:  
        d3s.to_excel(writer2, sheet_name='Judge 3')
    with pandas.ExcelWriter(csvfilename,
                    mode='a') as writer3:  
        users.to_excel(writer3, sheet_name='Users')
    with ZipFile(zipfilename, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(SITE_ROOT):
            if "gallery" not in folderName:
                for filename in filenames:
                    if "zip" not in filename:
                        filePath = os.path.join(folderName, filename)
                        zipObj.write(filePath)
    with open(zipfilename, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(zipfilename)
    return response

#     sql, params = ProjectUser.objects.exclude(Q (user_type=6)).order_by("-id").query.sql_with_params()
#     sql = f"COPY ({sql}) TO STDOUT WITH (FORMAT CSV, HEADER, DELIMITER E',')"
#     filename = 'f.csv'
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = f'attachment; filename={filename}'
#     with connection.cursor() as cur:
#         sql = cur.mogrify(sql, params)
#         cur.copy_expert(sql, response)
#     return response


def importfile(request): 
    response_data = {} 
#     response_data['errorResults'] = 'Under the test.' 
#     return HttpResponse(json.dumps(response_data),
#                 content_type="application/json") 
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['fileimport']
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            BULK_ROOT = os.path.join(MEDIA_ROOT, 'bulkartwork')
            cleanFiles(BULK_ROOT)
            cleanFiles(os.path.join(BULK_ROOT, 'artworks'))
            cleanFiles(os.path.join(BULK_ROOT, 'formulas'))
            fileaddr = os.path.join(BULK_ROOT, f.name)
            fs = FileSystemStorage()
            filename = fs.save(fileaddr, f)
            uploaded_file_url = fs.url(filename)
            fullpathhandle = open(filename, 'rb') 
            zfobj = zipfile.ZipFile(fullpathhandle)
            for name in zfobj.namelist():
                if name.endswith('/'):
                    try: 
                        os.mkdir(os.path.join(BULK_ROOT, name))
                    except:
                        pass
                else:
                    outfile = open(os.path.join(BULK_ROOT, name), 'wb')
                    outfile.write(zfobj.read(name))
                    outfile.close()
            fullpathhandle.close()            
            fields = ['Learner email', 'Learner First Name', 'Learner Surname', 'Learner Cellphone',
                  'Learner Date of Birth', 'Parent / Guardian Name & Surname', 'Parent / Guardian Email', 'Parent / Guardian Cellphone',
                  'Title of Artwork', 'Artwork Image Filename', 'EMIS Number',
                      'Learner Grade ', 'Filename of Mathematics', 'Teacher Name',
                      'Teacher email', 'Teacher Phone ', 'Answer to Question 1',
                      'Answer to Question 2', 'Answer to Question 3']
            filename = os.path.join(BULK_ROOT, 'participants.xlsx')
            pd = pandas.read_excel(filename, cols=fields, header=5, converters={'Parent / Guardian Cellphone':str, 'Learner Cellphone':str, 'Teacher Phone ':str, 'Filename of Mathematics':str, 'Learner Grade ':str})
            response_data = {}
            for index, row in pd.iterrows():
                user_data_dict = {}
                if len(str(row['Learner email'])) <= 3:
                    continue
                user_data_dict['username'] = row['Learner email']
                user_data_dict['first_name'] = row['Learner First Name']
                user_data_dict['last_name'] = row['Learner Surname']
                user_data_dict['cellphone'] = "0" + row['Learner Cellphone']
                user_data_dict['dob'] = row['Learner Date of Birth']
                user_data_dict['parentname'] = row['Parent / Guardian Name & Surname']
                user_data_dict['parentemail'] = row['Parent / Guardian Email']
                user_data_dict['parentphone'] = "0" + row['Parent / Guardian Cellphone']
                user_data_dict['password1'] = "abcdefg12345!@#$%"
                user_data_dict['password2'] = "abcdefg12345!@#$%"
                user_form = UserRegistrationForm(user_data_dict)
                if user_form.is_valid():
                    artwork_data_dict = {}
                    artwork_data_dict['worktitle'] = row['Title of Artwork']
                    artwork_data_dict['workfile'] = os.path.join(os.path.join(BULK_ROOT, 'artworks'), row['Artwork Image Filename'])
                    artwork_data_dict['learnergrade'] = "Grade " + row['Learner Grade ']
                    artwork_data_dict['teacheremail'] = row['Teacher email']
                    artwork_data_dict['teacherphone'] = "0" + row['Teacher Phone ']
                    artwork_data_dict['question1'] = row['Answer to Question 1']
                    artwork_data_dict['teachername'] = row['Teacher Name']
                    artwork_data_dict['question2'] = row['Answer to Question 2']
                    artwork_data_dict['question3'] = row['Answer to Question 3']
                    artwork_form = EntryForm(artwork_data_dict)
                    school = School.objects.get(natemis=int(row['EMIS Number']))
                    if artwork_form.is_valid():
                        user_form.save()
                        created_user = ProjectUser.objects.get(username=user_data_dict['username'])
                        artwork_form = artwork_form.save(commit=False)
                        artwork_form.school = school
                        artwork_form.status = 0
                        artwork_form.owner = created_user
                        if os.path.exists(artwork_data_dict['workfile']):
                            with open(artwork_data_dict['workfile'], 'rb') as img_file:
                                artwork_form.workfile.save(row['Artwork Image Filename'], File(img_file), save=True)
                        else:
                            response_data['errorResult'] = "Work file " + artwork_data_dict['worktitle'] + " doesn't exist."        
                            return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
                        artwork_data_dict['workformulafile'] = os.path.join(os.path.join(BULK_ROOT, 'formulas'), row['Filename of Mathematics'])
                        if os.path.exists(artwork_data_dict['workformulafile']):
                            if isNaN(row['Filename of Mathematics']) != True and len(str(row['Filename of Mathematics'])) > 0:
                                with open(artwork_data_dict['workformulafile'], 'rb') as formula_file:
                                    artwork_form.workformulafile.save(row['Filename of Mathematics'], File(formula_file), save=True)
                        artwork_form.save()
                else:
                    response_data['errorResults'] = user_form.errors.as_json(True)
                    response_data['index'] = index
                    return HttpResponse(json.dumps(response_data),
                                        content_type="application/json")
            response_data['successResult'] = "Successfully imported"        
            return HttpResponse(json.dumps(response_data),
                    content_type="application/json")


def cleanFiles(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
#         if os.path.isdir(file_path):
#             os.unlink(file_path)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)


def isNaN(string):
    return string != string


@login_required
def work_details(request, id, view):
    work = get_object_or_404(Artwork, id=id)
    if work.school is None:
        sno = 'XX_XXXXX_XXXXX'
    else:
        sno = get_province(work.school.province) + "_" + str(work.learnergrade.split(" ")[1]) + "_" + str(work.id)
    fname_lname = work.owner.last_name + ", " + work.owner.first_name
    context = {'work': work, 'sno':sno, 'fname_lname': fname_lname, 'view':view}
    return render(request, 'adminPages/work_details.html', context)


def calc_uid(workid):
    work = get_object_or_404(Artwork, id=workid)
    if work.school != None and work.learnergrade != None:
        return get_province(work.school.province) + "_" + str(work.learnergrade.split(" ")[1]) + "_" + str(work.id)
    else:
        return "XX_XXXXX_XXXXX"


def get_province(provinceVal):
    switcher = {
                'LP':'A',
                'KZN':'B',
                'WC':'C',
                'EC':'D',
                'NW':'E',
                'FS':'F',
                'NC':'G',
                'MP':'H',
                'GP':'I',
                'Other':'J',
                'GT':'K'
             }
    return switcher.get(provinceVal, "L")


def work_detail_update(request):
    response_data = {}
    if request.method == 'POST':
        workapproved = request.POST.get('workapproved', '') == 'False'
        bioapproved = request.POST.get('bioapproved', '') == 'False'
        qapproved = request.POST.get('qapproved', '') == 'False'
        comment = request.POST.get('comment', '')
        Artwork.objects.filter(id=request.POST['id']).update(status=request.POST['status'], workapproved=workapproved,
                                                     bioapproved=bioapproved, qapproved=qapproved, comment=comment)
        artwork = Artwork.objects.get(id=request.POST['id'])
        if request.POST.get('status', '1') == '1':
            subject = "<No-Reply>  MathArt Portal - Artwork requires revision"
            message = "Dear {0} {1}, the artwork you have submitted for the MathArt competition requires revision. Please login to the portal http://mathart.co.za and modify the work. ".format(artwork.owner.first_name, artwork.owner.last_name)
            send_mail(subject, message, 'mathart.co.za@gmail.com', [artwork.owner.email])
        response_data['successResult'] = 'Successful.'
    return HttpResponse(json.dumps(response_data),
                content_type="application/json")

    
def signup_page(request):   
    context = {}
    return render(request, 'signup_page.html', context)


@login_required
@transaction.atomic
def entry_form(request):
    if request.user.is_anonymous:
        userModel = None
    else:
        userModel = ProjectUser.objects.get(username=request.user)
        user_form = UserForm(instance=request.user)
    if request.method == 'POST':
        response_data = {}
        user_form = UserForm(data=request.POST, instance=userModel)
        if user_form.has_changed(): 
            if user_form.is_valid():
                user_form.save()
                response_data['successResult'] = "Saved successfully!"
            else:
                response_data['errorResults'] = user_form.errors.as_json(True)
                return HttpResponse(json.dumps(response_data),
                    content_type="application/json")
        try:
            old_data = get_object_or_404(Artwork, id=request.POST["id"])
        except:
            response_data['errorResults'] = "No access to entry form update."
            return HttpResponse(json.dumps(response_data),
                    content_type="application/json")
        artwork_form = EntryForm(data=request.POST, files=request.FILES, instance=old_data)
        if artwork_form.is_valid():
            artwork_form = artwork_form.save(commit=False)
            artwork_form.owner = request.user
            if request.POST.get('status', '-1') != '-1':
                artwork_form.status = int(request.POST.get("status"))
            if request.POST.get('teacherphone', '-1') != '-1' and len(request.POST.get('teacherphone')) > 1:
                artwork_form.teacherphone = request.POST.get("teacherphone")
#             if request.POST.get('status', '1') != '1':
#                 artwork_form.status = int(request.POST.get("status"))
            if int(request.POST.get("school", 0)) > 0:
                school = get_object_or_404(School, id=request.POST["school"])
                artwork_form.school = school
                artwork_form.school_id = int(request.POST["school"])
            try:
#                 if artwork_form.status == 1:
#                     artwork_form.status = 2
                artwork_form.save()
            except:
                response_data['errorResults'] = "Error in saving the artwork. Try again now. If this error occurred again, please contact us."
                return HttpResponse(json.dumps(response_data),
                    content_type="application/json")
            response_data['id'] = artwork_form.id
            if artwork_form.status == 0:
                try:
                    subject = "<No-Reply> MathArt Portal - Entry Submission Successful"
                    message = "Dear {1} {0}, you have successfully Submitted in MathArt competition.\n\n Thank you for completing the submission of your artwork in the MathArt competition.".format(request.user.last_name, request.user.first_name)
                    send_mail(subject, message, 'mathart.co.za@gmail.com', [request.user.username])
                except:
                    response_data['errorResults'] = "The entry is saved successfully. The system failed to send you the confirmation email, please contact us to ensure that the artwork is received."
                    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
            response_data['successResult'] = "Saved successfully!"
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = artwork_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel is not None and userModel.user_type == 1:
        try:
            artwork_model = get_object_or_404(Artwork, owner=request.user)
        except:
            artwork_model, artwork_obj = Artwork.objects.get_or_create(owner=request.user)
        artwork_form = EntryForm(instance=artwork_model)
    else:
        artwork_form = EntryForm()
        user_form = UserForm()
    context = {'form': artwork_form, 'user_form': user_form}
    return render(request, 'entry_form.html', context)

 
def entry_form_view(request):
    artwork_form = EntryForm()
    user_form = UserForm()
    context = {'form': artwork_form, 'user_form': user_form}
    return render(request, 'entry_form_view.html', context)   

