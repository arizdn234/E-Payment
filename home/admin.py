from django.contrib import admin
from .models import Siswa, TahunAjaran, Jurusan, SPP, Pembayaran

# @admin.register(SiswaLogin)
# class SiswaLoginAdmin(admin.ModelAdmin):
#     list_display = ["nis", "username", "password"]

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ["nama", "kelas", "jurusan", "nis"]


@admin.register(TahunAjaran)
class TahunAjaranAdmin(admin.ModelAdmin):
    list_display = ["tahun"]


@admin.register(Jurusan)
class JurusanAdmin(admin.ModelAdmin):
    list_display = ["nama"]


@admin.register(SPP)
class SPPAdmin(admin.ModelAdmin):
    list_display = ["tahun_ajaran", "jurusan", "jumlah"]


@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = ["siswa", "tahun_ajaran", "tanggal", "jumlah"]
