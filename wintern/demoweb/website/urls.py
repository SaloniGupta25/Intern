from django.urls import path
from . import views
from .views import HomePageView, CreatePostView


urlpatterns = [
	path('register/', views.registerPage,name="register"),
	path('', HomePageView.as_view(), name='home'),

	path('post/', CreatePostView.as_view(), name='add_post'),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('profile/', views.hotel_image_view, name='image_upload'),
    path('hotel_images/', views.display_hotel_images, name = 'hotel_images'),
]