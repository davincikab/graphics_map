from django.contrib import admin
from django.urls import path,include
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',include("main.urls"),name="main"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('i18n/', include('django.conf.urls.i18n')), 
]
