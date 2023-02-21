from django.db import models


# Create your models here.

class Bus(models.Model):
    numero_unidad = models.IntegerField(primary_key=True) 
    patente = models.CharField("patente", max_length=50)  
    fecha_compra = models.DateField() 
    estado = models.CharField("Estado",max_length=50)  
    
    def __str__(self):
        return self.patente

    
  
class Chofer(models.Model):
    nro_documento = models.IntegerField(primary_key=True)
    legajo = models.CharField("legajo", max_length=50)
    nombre= models.CharField("nombre", max_length=50) 
    apellido = models.CharField("apellido", max_length=50) 

    def __str__(self):
        return self.nombre

class Atractivo(models.Model):
    nombre = models.CharField("nombre",max_length=50)  
    calificacion = models.CharField("calificacion", max_length=50)  
    
    def __str__(self):
        return self.nombre

class Parada(models.Model):
    nombre = models.CharField("nombre", max_length=50)  
    descripcion = models.CharField("descripcion",max_length=100) 
    direccion = models.CharField("direccion",max_length=50)  


    def __str__(self):
        return self.nombre

class DetalleCadaParada(models.Model):
    estado_parada = models.CharField("estado_parada",max_length=50)
    numero_orden = models.IntegerField("numero_orden" ) 
    conexion = models.IntegerField("conexion")  
    parada = models.ForeignKey(Parada,on_delete=models.CASCADE)  

    def __str__(self):
        return self.estado_parada

class Recorrido(models.Model):
    numero_recorrido= models.IntegerField(primary_key=True) 
    dia = models.DateField()
    nombre = models.CharField("nombre",max_length=50,) 
    hora_inicio = models.TimeField() 
    hora_finalizacion = models.TimeField()  
    duracion_aprox = models.TimeField()  
    frecuencia = models.TimeField()
    color = models.CharField("color", max_length=50,)  
    lista_detalle_parada = models.ForeignKey(DetalleCadaParada, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre 
 
   
class Viaje(models.Model):
    nombre = models.CharField("nombre",max_length=50,) 
    dia = models.DateField()
    hora_inicio_prevista = models.TimeField()  
    hora_inicio = models.TimeField()  
    hora_fin = models.TimeField()
    numero = models.IntegerField(primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre


