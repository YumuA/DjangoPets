from django.db import models


class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    duenos = models.ManyToManyField(Dueno, related_name='mascotas')

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio)
    notificacion_enviada = models.BooleanField(default=False)

    def __str__(self):
        return f'Cita para {self.mascota.nombre} el {self.fecha} a las {self.hora}'
