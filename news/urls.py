from django.urls import path, include
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Title'}), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(extra_context={'title': 'Title'}), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
