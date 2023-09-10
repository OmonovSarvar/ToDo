from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('todomodel/<int:pk>', views.Message.as_view()),
    path('new/', views.PostTweet.as_view(), name='new'),
    path('todomodel/<int:pk>/delete', views.DeleteTweet.as_view(), name='delete'),
]
