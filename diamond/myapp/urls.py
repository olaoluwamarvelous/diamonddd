from .views import  BlogView, TeamView,  Post,TestimonyView , index, RecentView


from . import views
from django.urls import path

#from .views import views


urlpatterns = [
    path('team/', views.TeamView.as_view(), name='team'),


    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),

    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('recent/', views.RecentView.as_view(), name='recent'),

    #path('<slug:slug>/', views.blogdetail, name='blogdetail'),
    path('<slug:slug>/', views.blogdetail, name='blogdetail'),

   # path('blogdetail/', views.blogdetail, name='blogdetail'),

    path('main/', views.main, name='main'),

    path('portfolio/', views.portfolio, name='portfolio'),

    #generic ones

    path('testimony/', views.TestimonyView.as_view(), name='testimony'),


    path('recentpost/', views.RecentpostView.as_view(), name='recentpost'),
    path('', views.index, name='index'),

]
