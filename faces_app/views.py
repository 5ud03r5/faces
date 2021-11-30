from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from faces_app.forms import CreateComment, CreatePost, ProfileUpdate, UserLoginForm
from .models import Comment, Message, Post, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import authenticate, login


@login_required(login_url='login')
def updateProfile(request, pk):
    profile=Profile.objects.get(id=pk)
    print(request.user.profile.id)
    print(pk)

    form = ProfileUpdate(instance=profile)
    if request.method == 'GET':
        if request.user.profile.id != profile.id:
            return redirect('profile', pk)

    
    elif request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('profile', pk)

    context = {'form':form}

    return render(request, 'update_profile.html', context)

    

class Login(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    success_url = 'login.html'
    redirect_field_name = None
    
@login_required(login_url='login')
def mainPage(request):
    
    posts = Post.objects.all()
    form_comment = CreateComment()
    form_post = CreatePost()

    if request.method == "POST":

        if request.POST.get('type') == 'Add Post':
            form_post = CreatePost(request.POST, request.FILES)
            if form_post.is_valid:
                new_post = form_post.save(commit=False)
                new_post.owner = request.user.profile
                new_post.created_by = request.user.profile
                new_post.save()
                return redirect('main_page')

        elif request.POST.get('type') == 'Add Comment':
            form_comment = CreateComment(request.POST, request.FILES)
            if form_comment.is_valid:
                new_comment = form_comment.save(commit=False)
                new_comment.owner = request.user.profile
                new_comment.post_id = request.GET.get('post')
                print(new_comment.post_id)
                new_comment.save()
                return redirect('main_page')
    
    context = {'posts':posts, 'form_comment':form_comment, 'form_post':form_post}

    return render(request, 'main_page.html', context)



class Register(CreateView):
    template_name = 'register.html'
    model = User
    form_class = UserCreationForm
    

    def form_valid(self, form):
        #save the new user first
        form.save()

        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']

        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        
        return redirect('update_profile', user.profile.id)






@login_required(login_url='login')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(owner_id = pk)
    form_comment = CreateComment()
    form_post = CreatePost()

    if request.method == "POST":

        if request.POST.get('type') == 'Add Post':
            form_post = CreatePost(request.POST, request.FILES)
            if form_post.is_valid:
                new_post = form_post.save(commit=False)
                if request.user.profile.id == pk:
                    new_post.owner = request.user.profile
                    new_post.created_by = request.user.profile
                    new_post.save()
                else:
                    new_post.owner_id = pk
                    new_post.created_by = request.user.profile
                    new_post.save()
                return redirect('profile', pk)

        elif request.POST.get('type') == 'Add Comment':
            form_comment = CreateComment(request.POST, request.FILES)
            if form_comment.is_valid:
                new_comment = form_comment.save(commit=False)
                new_comment.owner = request.user.profile
                new_comment.post_id = request.GET.get('post')
                new_comment.save()
                return redirect('profile', pk)
    
    context = {'profile': profile, 'posts':posts, 'form_comment':form_comment, 'form_post':form_post}

    return render(request, 'profile.html', context)



class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    model = User

    def get_success_url(self):
        url = self.request.GET.get('next')
        return url


class Messages(LoginRequiredMixin, ListView):
    model = Profile  
    template_name = 'messages.html'
    context_object_name = 'profiles'
  
    

class SendMessage(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'message.html'
    fields = ['body']
      
    def form_valid(self, form):
        pk = self.kwargs['pk']      
        form.instance.sender = self.request.user.profile
        form.instance.receipient_id = pk
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['messages'] = Message.objects.distinct().filter(Q(receipient_id__exact=pk) | Q(sender_id__exact=pk)).order_by('-created')
        context['profile'] = Profile.objects.get(id=pk)
        return context

    
class Profiles(LoginRequiredMixin, TemplateView):
    

    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()

        if request.GET.get('search'):
            search_query = request.GET.get('search')
            profiles = Profile.objects.distinct().filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        
        context = {'profiles':profiles}
        return render(request, 'profiles.html', context)


class DeleteObject(TemplateView, LoginRequiredMixin):
    template_name = 'delete.html'
    success_url = '/'

    def post(self, request, *args,  **kwargs):                  
        pk = self.kwargs['pk']       
        if Post.objects.filter(id__exact=pk):                          
            delete_object = Post.objects.get(id=pk)
            print(pk)
            delete_object.delete()
            
        elif Comment.objects.filter(id__exact=pk):            
            delete_object = Comment.objects.get(id=pk)
            delete_object.delete()

        return redirect('main_page')

