from django.urls import path, include
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #path('', views.HomeListView.as_view(), name='home'),
    path('profileform/', views.UserProfileFormView.as_view(), name='profileform'),
    path('profile/', views.UserProfileView.as_view(), name = 'profile'),
    path('profileupdate/', views.UserprofileUpdateView.as_view(), name='profileupdate'),
    path('userprofile/', views.edit, name='userprofile'),
    path('userlist/', views.UserListView.as_view(), name='userlist')


]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
