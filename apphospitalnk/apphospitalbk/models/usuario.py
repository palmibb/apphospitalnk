from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        
        user = self.create_user(
            username = username,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField('NombreUsuario', max_length = 15, unique=True)
    password = models.CharField('Contraseña', max_length = 256)
    name_user = models.CharField('Nombre', max_length = 30)
    email_user = models.EmailField('Correo', max_length = 100)
    create_date_user = models.DateTimeField('FechaCreacion')
    estado_user = models.BooleanField(default=True)
    apellido_user = models.CharField('Apellido',max_length = 30)
    cargo_user = models.CharField('Cargo', max_length=15)
    direccion_user = models.CharField('Direccion', max_length=50)
    telefono_user =models.CharField('Telefono', max_length=15)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'