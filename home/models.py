from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models


class TahunAjaran(models.Model):
    tahun = models.CharField(max_length=9)


class Jurusan(models.Model):
    nama = models.CharField(max_length=100)


class SPP(models.Model):
    tahun_ajaran = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)


class Siswa(models.Model):
    nis = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=10)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)


class Pembayaran(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tahun_ajaran = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)


# class SiswaLoginManager(BaseUserManager):
#     def create_user(self, nis, username, password=None, **extra_fields):
#         if not nis:
#             raise ValueError("NIS harus diisi")
#         if not username:
#             raise ValueError("Username harus diisi")

#         user = self.model(nis=nis, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, nis, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(nis, username, password, **extra_fields)


# class SiswaLogin(AbstractBaseUser):
#     nis = models.CharField(max_length=20, unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)

#     objects = SiswaLoginManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['nis']

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

