from django.shortcuts import render, get_object_or_404
from artwork.artwork_models import Artwork, School, convert_to_df
from django.http import HttpResponse
import json
from artwork.artwork_forms import EntryForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from account.models_account import ProjectUser
import os
import pandas
from account.forms_account import UserRegistrationForm
from django.core.mail import send_mail
from zipfile import ZipFile


def index(request):
    context = {}
    return render(request, 'index.html', context)


def managerConsole(request):
    context = {}
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


def work_lists(request):
    works = Artwork.objects.all()
#     filter(status__gte=0)
    context = {'works': works}
    return render(request, 'adminPages/work_lists.html', context)

def getfile(request):  
    artworks = Artwork.objects.filter()  # status__gte=0
    fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__cellphone',
              'owner__dob', 'owner__parentname', 'owner__parentemail', 'owner__parentphone',
              'worktitle', 'workfile', 'school',
                  'learnergrade', 'workformulafile', 'teachername',
                  'teacheremail', 'teacherphone', 'question1',
                  'question2', 'question3']
    df = convert_to_df(artworks, fields=fields)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SITE_ROOT = os.path.join(BASE_DIR, 'media')
    csvfilename = SITE_ROOT + '\\artworks.csv'
    zipfilename = SITE_ROOT + '\\backup.zip'
    df.to_csv(csvfilename, mode='w')
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




def importfile(request):  
    fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__cellphone',
              'owner__dob', 'owner__parentname', 'owner__parentemail', 'owner__parentphone',
              'worktitle', 'workfile',
                  'learnergrade', 'workformulafile', 'teachername',
                  'teacheremail', 'teacherphone', 'question1',
                  'question2', 'question3']
    filename = os.path.dirname(os.path.abspath(__file__)) + '\\artworksd.csv'
    pd = pandas.read_csv(filename, usecols=fields, header=0)
    response_data = []
    for index, row in pd.iterrows():
        user_data_dict = {}
        user_data_dict['username'] = row['owner__username']
        user_data_dict['first_name'] = row['owner__first_name']
        user_data_dict['last_name'] = row['owner__last_name']
        user_data_dict['cellphone'] = row['owner__cellphone']
        user_data_dict['dob'] = row['owner__dob']
        user_data_dict['parentname'] = row['owner__parentname']
        user_data_dict['parentemail'] = row['owner__parentemail']
        user_data_dict['parentphone'] = row['owner__parentphone']
        user_data_dict['password1'] = "abcdefg12345!@#$%"
        user_data_dict['password2'] = "abcdefg12345!@#$%"
        user_form = UserRegistrationForm(user_data_dict)
        if user_form.is_valid():
            user_form.save()
            created_user = ProjectUser.objects.get(username=user_data_dict['username'])
            artwork_data_dict = {}
            artwork_data_dict['worktitle'] = row['worktitle']
            artwork_data_dict['workfile'] = row['workfile']
            artwork_data_dict['learnergrade'] = row['learnergrade']
            artwork_data_dict['teacheremail'] = row['teacheremail']
            artwork_data_dict['teacherphone'] = row['teacherphone']
            artwork_data_dict['question1'] = row['question1']
            artwork_data_dict['teachername'] = row['teachername']
            artwork_data_dict['question2'] = row['question2']
            artwork_data_dict['question3'] = row['question3']
            artwork_data_dict['workformulafile'] = row['workformulafile']
            artwork_form = EntryForm(artwork_data_dict)
            if artwork_form.is_valid():
                artwork_form.save(commit=False)
                school = School().objects.get(id=row['school'])
                artwork_form.school = school
                artwork_form.status = 0
                artwork_form.owner = created_user
                artwork_form.save()
        else:
            response_error = {}
            response_error['errorResults'] = user_form.errors.as_json(True)
            response_error['index'] = index
            response_data.append(response_error)
    return HttpResponse(json.dumps(response_data),
            content_type="application/json")


def work_details(request, id):
    if request.method == 'POST':
        Artwork.objects.filter(id=id).update(status='updated_name')
    work = get_object_or_404(Artwork, id=id)
    context = {'work': work}
    return render(request, 'adminPages/work_details.html', context)


def work_detail_update(request):
    response_data = {}
    if request.method == 'POST':
        workapproved = request.POST.get('workapproved', '') == 'False'
        bioapproved = request.POST.get('bioapproved', '') == 'False'
        qapproved = request.POST.get('qapproved', '') == 'False'
        comment = request.POST.get('comment', '')
        Artwork.objects.filter(id=request.POST['id']).update(status=request.POST['status'], workapproved=workapproved,
                                                     bioapproved=bioapproved, qapproved=qapproved, comment=comment)
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
        old_data = get_object_or_404(Artwork, id=request.POST["id"])
        artwork_form = EntryForm(request.POST, request.FILES, instance=old_data)
        response_data = {}
        if artwork_form.is_valid():
            artwork_form = artwork_form.save(commit=False)
            artwork_form.owner = request.user
            if request.POST.get('status', '-1') != '-1':
                artwork_form.status = int(request.POST.get("status"))
            if int(request.POST.get("school", 0)) > 0:
                school = get_object_or_404(School, id = request.POST["school"])
                artwork_form.school = school
                artwork_form.school_id = int(request.POST["school"])
            try:
                artwork_form.save()
            except:
                response_data['errorResults'] = "Error in saving the artwork. Try again now. If this error occurred again, please contact us."
                return HttpResponse(json.dumps(response_data),
                    content_type="application/json")
            response_data['id'] = artwork_form.id
            if artwork_form.status == 0:
                try:
                    subject = "MathArt Portal - Entry Submission Successful"
                    message = "Dear {0} {1}, you have successfully Submitted in MathArt competition.\n\n Please go on and finish your artwork submission".format(request.user.last_name, request.user.first_name)
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

