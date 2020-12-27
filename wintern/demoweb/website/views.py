from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages


from django.views.generic import ListView
from .models import Post

# Create your views here.
from .models import *
from .forms import CreateUserForm,HotelForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post



def registerPage(request):
    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
    else:
        form=CreateUserForm()

    context = {'form': form}
    return render(request, 'website/signup.html', context)


def loginPage(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'website/signin.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

# def home(request):
#     return render(request, 'website/base.html')



class HomePageView(ListView):
    model = Post
    template_name = 'website/home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'website/post.html'
    success_url = reverse_lazy('home')

def profile(request):
    context={
        'user':request.user
}
    return render(request,'website/profile.html',context)





def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('hotel_images')
    else:
        form = HotelForm()
    return render(request, 'website/profile.html', {'form': form})




def display_hotel_images(request):
    if request.method == 'GET':
        Hotels = Hotel.objects.order_by('id')[::-1]
        return render(request, 'website/display_hotel_images.html',{'hotel_images': Hotels})









