from django.urls import path, include
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [


    path('', views.ImageHomeView.as_view(), name='home'),
    path('userprofile/', views.profileView.as_view(), name='userprofile'),
    path('create/', views.ImageCreateView.as_view(), name='create'),
    path('userdetail/<int:pk>/', views.profileView.as_view(), name='userdetail'),
    path('imagedetail/<int:pk>/', views.ImageDetailView.as_view(), name='imagedetail'),


]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
