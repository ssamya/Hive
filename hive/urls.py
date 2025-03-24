from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('user/', include('users.urls', namespace='user')),
    path('', include('main.urls', namespace='main')),
    path('order_time_page/', views.order_time_page, name='order_time_page'),
    path('thanks/', views.thanks_page, name='thanks_page'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)