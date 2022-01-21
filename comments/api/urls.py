from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Welcome),
    path('comments/', CommentView.as_view()),
    path('post/<str:pk>/comments/', PostCommentApiView.as_view()),
]