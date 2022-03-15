from django.urls import path

from .views import GetStudentsView,AddStudentView,UpdateStudentView,DeleteStudentView

app_name = "student"

urlpatterns = [
    path('students', GetStudentsView.as_view()),
    path('addstudent', AddStudentView.as_view()),
    path('updatestudent', UpdateStudentView.as_view()),
    path('deletestudent', DeleteStudentView.as_view()),
]