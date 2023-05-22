from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('contact_us/',views.contact_us,name='contact_us '),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
