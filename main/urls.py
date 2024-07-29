from django.urls import path
from .views import CommentView, CategoryView, RegisterView, VideoView, TagView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('category/', CategoryView.as_view(), name='category'),
    path('tag/', TagView.as_view(), name='tag'),
    path('video/', VideoView.as_view(), name='video')
]
