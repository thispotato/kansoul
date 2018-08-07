from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'blog'
urlpatterns = [
    path('' , views.index , name='index'),
    path('category/<int:pk>', views.category , name ='category'),
    path('view/<int:pk>' , views.view , name = 'view'),
    path('edit/<int:pk>' , views.edit , name = 'edit'),
    path('user/<int:pk>' , views.user , name = 'user'),
    path('user/posts/<int:pk>' , views.author_post , name = 'author_post'),
]+static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
