from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("main.urls"),name="main"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('i18n/', include('django.conf.urls.i18n')), 
]
