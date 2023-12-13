from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.index_page),
  path("custommaps/", views.custommaps),
  path("create_custommaps/", views.create_custommaps),
  path("custom_maps/<title>/", views.custommaps_detail),

  path('projects/', views.projects),
  path('create_project/', views.create_project),
  path('projects/<title>', views.project_detail),
  path('projects/<title>/view/', views.project_view),
  path('project_categories/<project_title>', views.project_categories),

  path('project/add_category', views.add_category),
  path('project/add_sub_category', views.add_sub_category),
  path('project/add_sub_category', views.add_sub_category),
  path('project/get_categories', views.get_categories),

  # pins
  path("pins/", views.get_pins),
  path("pins/create", views.create_pins),
  path('pins/delete/<title>', views.delete_pins),

  # icons
  path("icons", views.icons_list),
  path("icons_list/", views.get_icons),

  # user acc
  # path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)