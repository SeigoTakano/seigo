from django.urls import path
from . import views

app_name = "seigoapp"

urlpatterns = [path('',views.IndexView.as_view(), name = 'index'),
               path('mypage/',views.MypageView.as_view(),name='mypage'),
               path('stu_score/',views.Stu_scoreView.as_view(),name='stu_score'),
               path('schedule/',views.ScheduleView.as_view(),name= 'schedule'),
               path('contact/',views.ContactView.as_view(),name= 'contact'),
               path('register/', views.register_student_with_score, name='register_student_with_score'),
               ]