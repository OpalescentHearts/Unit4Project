from django.contrib import admin
from django.urls import path
from app.views import project_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",project_view),
]
