from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('profile/', profile_view, name="profile"),
    path('favorite/', wishlist_view, name="favorite"),
]