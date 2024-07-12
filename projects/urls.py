from django.urls import path
from .views import projects,project,createProject,updateProject,deleteObject



urlpatterns = [
    path('',projects,name='projects'),
    path('project-object/<str:pk>/',project,name='project'),
    path('create-project/',createProject,name="create-project"),
    path('update-project/<str:pk>/',updateProject,name="update-project"),
    path('delete-project/<str:pk>/',deleteObject,name="delete-project"),
]