from django.urls import path
#from .views import homes, undefinedUrl,Home,test,UserListCreateAPIView
from . import views
from .views import image_list, image_detail, role_list_create, custom_user_list_create, custom_user_retrieve_update_destroy ,custom_user_role_update, images_not_approved,images_approved
urlpatterns = [
    path('images/', image_list, name='image-list'),
    path('images/<int:pk>/', image_detail, name='image-detail'),
    path('roles/', role_list_create, name='role-list-create'),
    path('users/', custom_user_list_create, name='customuser-list-create'),
    path('users/<int:pk>/', custom_user_retrieve_update_destroy, name='customuser-retrieve-update-destroy'),
    path('users/<int:pk>/roles/', custom_user_role_update, name='customuser-role-update'),
    path('images/not-approved/', images_not_approved, name='images-not-approved'),
    path('images/approved/', images_approved, name='images-approved'),
]

