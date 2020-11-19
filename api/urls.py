from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('student/', views.studentData, name="task-filter"),
	path('studentPush/', views.studentPush, name="student-push"),
]
