from . import views
from django.urls import path

urlpatterns = [
    path('artwork', views.PostList.as_view(), name='artwork'),
    path('artwork/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('artwork/like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('', views.HomePage.as_view(), name='home'),
    path('contact', views.ContactPage.as_view(), name='contact'),
    path('booking', views.BookingPage.as_view(), name='booking'),
]