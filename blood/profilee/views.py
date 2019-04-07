from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserUpdateForm
from  django.urls import reverse_lazy
from .models import UserProfile
from braces.views import LoginRequiredMixin, UserFormKwargsMixin, CsrfExemptMixin
from .models import User
#from django.contrib.auth.forms import UserChangeForm
# Create your views here.

#class HomeView(TemplateView):
    #template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = ('registration/signup.html')


class UserProfileFormView(CreateView):
    #form_class = UserProfileForm
    model = UserProfile
    fields = ('user', 'bio', 'blood_group', 'gender', 'phone', 'city', 'country')
    success_url = reverse_lazy('home')
    template_name = ('profileform.html')

class HomeListView(ListView):
    model = UserProfile
    template_name = 'home.html'


class UserProfileView(ListView):
    model = UserProfile
    template_name = 'profile.html'


#class UserDetailView(DetailView):
    #model = UserProfile
    #template_name = 'profile.html'

class UserprofileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'profileform.html'
    fields = ('bio', 'blood_group', 'gender', 'phone', 'city', 'country', 'image',)
    login_url = "login/"
    #redirect_field_name = "login"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        fields = ('username',)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=request.user)
        args = {'form' : form}
        return render(request, 'registration/login.html', args)

class UserListView(ListView):
    model = User
    template_name = 'userlist.html'
    context_object_name = 'user_list'

    def get_queryset(self) :
        queryset = User.objects.filter(is_active=True)
        return queryset
