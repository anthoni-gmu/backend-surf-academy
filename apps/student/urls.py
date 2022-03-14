from django.urls import path

from .views import GetStudentsView,AddStudentView

app_name = "student"

urlpatterns = [
    path('students', GetStudentsView.as_view()),
    path('addstudent', AddStudentView.as_view()),
]