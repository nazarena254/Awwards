from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('signup/',views.signup_view, name='signup'),
    path('upload/project/', views.upload_project, name='add_project'),
    path('review/<project_title>', views.rate_project, name='rate'),
    re_path(r'^search/', views.search_project,name='search_results'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)