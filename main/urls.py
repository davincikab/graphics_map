from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
  path('', views.index_page),
  path("custommaps/", views.custommaps),
  path("create_custommaps/", views.create_custommaps),
  path("custom_maps/<title>/", views.custommaps_detail),

  path('projects/', views.projects),
  path('create_project/', views.create_project),
  path('projects/<title>', views.project_detail),
  path('pins', views.pins_page),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)