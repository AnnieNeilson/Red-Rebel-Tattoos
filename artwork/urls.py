from django.urls import path
from . import views


urlpatterns = [
    path('artwork', views.PostList.as_view(), name='artwork'),
    path('artwork/<slug:slug>/', views.PostDetail.as_view(),
         name='post_detail'),
    path('artwork/like/<slug:slug>', views.PostLike.as_view(),
         name='post_like'),
]
