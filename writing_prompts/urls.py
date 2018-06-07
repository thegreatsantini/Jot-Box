from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signout/', views.signout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<username>', views.profile_view, name="profile"),
    path('profile/post_entry/', views.post_entry, name="post_entry"),
    path('profile/delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),      
]
# path('signup/', views.post_cat, name='signup')
