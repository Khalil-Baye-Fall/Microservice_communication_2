from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Welcome),
    path('posts/', PostApiView.as_view())
]