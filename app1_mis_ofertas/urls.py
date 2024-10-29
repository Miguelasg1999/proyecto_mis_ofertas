from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name="signout"),
    path('post_product/', views.post_product, name='post_product'),
    path('product/<int:id>/', views.product, name='product'),
    path('eliminarProd/<int:id>', views.eliminarProd, name='eliminarProd'),
    path('editarProd/<int:id>', views.editarProd, name='editarProd'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)