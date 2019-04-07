from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import ImageCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Image
from profilee.models import User
# Create your views here.



class profileView(ListView):
    model = Image
    template_name = 'image/userprofile.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return Image.objects.filter(user=self.user)

    def get_context_data(self,**kwargs):
        context = super(profileView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context




class ImageCreateView(LoginRequiredMixin, CreateView):
    form_class = ImageCreationForm
    template_name = 'image/create.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ImageHomeView(ListView):
    model = Image
    template_name = 'image/home.html'





class ImageDetailView(DetailView):
    model = Image
    template_name = 'image/detail.html'

#class CommentView(CreateView):
    #model = Comment
    #fields = ['content']
    #template_name = 'detail.html'
    #def form_valid(self, form):
        #models_name = Comment()
        #models_name.content = self.request.POST['content']
        #models_name.author = self.request.user
        #models_name.post = Movie.objects.get(pk=self.kwargs['pk'])
        #models_name.save()
        #return redirect(self.get_success_url(id = self.kwargs['pk']))

    #def get_success_url(self, **kwargs):
        #if  kwargs != None:
            #return reverse_lazy('detail', kwargs = {'pk': kwargs['id']})
        #else:
            #return reverse_lazy('detail', args = (self.object.id,))


#def dispatch(self, request, *args, **kwargs):
    #obj = self.get_object()
    #if obj.user != self.request.user:
        #return Http404("You are not allowed to edit this Post")
    #return super(EditPost, self).dispatch(request, *args, **kwargs)

#class EditPost(LoginRequiredMixin, UpdateView):
    #def get_queryset(self):
        #return super(EditPost, self).filter(user=self.request.user)
