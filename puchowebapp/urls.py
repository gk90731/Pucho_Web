from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index ,name="home"),
    path('what_we_do/',views.what_we_do ,name="what_we_do"),
    path('about/',views.about ,name="about"),
    path('protfolio/',views.protfolio ,name="protfolio"),
    path('gallery/',views.gallery ,name="gallery"),
    path('contact/',views.contact ,name="contact"),
]
