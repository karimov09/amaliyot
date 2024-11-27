from django.urls import path
from . import views

urlpatterns = [
    path('api/teachers/', views.TeachersListView.as_view(), name='api_TeachersListView'),
    path('api/teachers/<int:teachers_id>/', views.TeachersDetailView.as_view(), name='api_teacher_detail'),
    path('api/students/', views.StudentsListView.as_view(), name='api_students_list'),
    path('api/StudentsDetailView/<int:students_id>/', views.StudentsDetailView.as_view(), name='api_student_detail'),
]
