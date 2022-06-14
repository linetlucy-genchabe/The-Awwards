from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path('', views.home , name='home'),
    path('register/',views.register),
    path('login/',views.user_login, name='login'),
    path('logout/',views.signout),
    path('profile/',views.profile),
    path('search/', views.search_projects, name='search_results'),
    path('project/<int:id>', views.get_project, name='project_results'),
    path('new/project', views.new_project, name='new-project'),
    path('accounts/profile/', views.user_profiles, name='profile'),
    
    # path('ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    path('api/projects/', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)