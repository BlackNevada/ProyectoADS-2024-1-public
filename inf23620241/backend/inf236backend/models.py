from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MecanicoManager(BaseUserManager):
    def create_user(self, rut, password=None, **other_fields):
        if not rut:
            raise ValueError('El RUT es obligatorio')
        user = self.model(rut=rut, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(rut, password, **other_fields)

class Mecanico(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField('RUT', max_length=12, primary_key=True)
    nombre = models.CharField(max_length=256)

    is_jefe_motor = models.BooleanField(default=False)
    # Otros campos necesarios
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MecanicoManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.rut

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    # id_motor = models.AutoField(primary_key=True)
    n_serie = models.CharField(max_length=256, primary_key=True)
    estado = models.CharField(max_length=256)
    anio = models.IntegerField()
    fecha_mantencion = models.DateField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=256)

class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    id_mecanico = models.ForeignKey(Mecanico, to_field='rut', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_termino = models.DateField(null=True, blank=True, default=None)
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)
    n_serie_motor = models.ForeignKey(Motor, to_field='n_serie', on_delete=models.CASCADE)

class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)
    fecha_mantencion = models.DateField()
    n_serie_motor = models.ForeignKey(Motor, on_delete=models.CASCADE)

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)
    fecha_mantencion = models.DateField()
    id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)

class Camion(models.Model):
    id_camion = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=256)
    patente = models.CharField(max_length=256)
    flota = models.CharField(max_length=256)

class Asignacion(models.Model):
    fecha = models.DateField()
    n_serie_motor = models.ForeignKey(Motor, to_field='n_serie', on_delete=models.CASCADE)
    id_camion = models.ForeignKey(Camion, on_delete=models.CASCADE)

class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=256)
    id_mecanico = models.ForeignKey(Mecanico, to_field='rut', on_delete=models.CASCADE)
    n_serie_motor = models.ForeignKey(Motor, to_field='n_serie', on_delete=models.CASCADE)
    detalles = models.CharField(max_length=512)
    posible_solucion = models.CharField(max_length=512)
