from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('projects/', views.projects, name='projects'),
    # path('contact/', views.contact, name='contact'),
    
    path('home/', views.home),
    path("get-cities/", views.get_cities, name="get_cities"),

    path('create-project/', views.createProject, name='create_project'),
    path('project-list/', views.projectList, name='project_list'),
]