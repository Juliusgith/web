from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import register, subscription_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('success/', views.success, name='success'),  
    path('subscription/', subscription_view, name='subscription'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
