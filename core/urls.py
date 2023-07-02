from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    # path("siswa-login/", views.siswa_login_view, name='siswa-login'),
    # path("profile/", views.profile, name='profile'),
]
