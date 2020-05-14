from django.urls import path
from evaluation import views_evaluation

app_name = 'evaluation'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('formd1a/', views_evaluation.create_d1a, name='formd1a'),
    path('formd1b/', views_evaluation.create_d1b, name='formd1b'),
    path('formd2/', views_evaluation.create_d2, name='formd2'),
    path('formd3/', views_evaluation.create_d3, name='formd3'),
    path('eval_forms_artwork/', views_evaluation.eval_forms_artwork, name='eval_forms_artwork'),
    path('updateAllD2s/', views_evaluation.updateWorkJudge2to3, name='updateAllD2s'),
]
