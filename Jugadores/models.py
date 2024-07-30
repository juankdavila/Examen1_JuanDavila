from django.db import models

# Create your models here.
class Futbolista(models.Model):
    id_futbolista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=1)
    
    def __str__(self):
        return (f'{self.id_futbolista} {self.nombre} {self.apellidos} {self.edad}'
                f' {self.direccion} {self.mail} {self.fecha_nacimiento} {self.estado}')
                    
                
    class Meta:
        db_table = 'futbolista'           
                
class Equipos(models.Model):
    id_equipo =  models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return (f'{self.id_equipo} {self.nombre_equipo} {self.descripcion} {self.ubicacion}'
                f' {self.objetivo} {self.contacto} {self.estado}')
                
    class Meta:
        db_table = 'equipos' 

class Historico_Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    id_futbolista = models.ForeignKey(Futbolista, db_column='id_futbolista', on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipos, db_column='id_equipo', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
  
     
    def __str__(self):
        return (f'{self.id} {self.id_futbolista} {self.id_equipo} {self.fecha_inicio}'
                f' {self.fecha_fin}')
        
    class Meta:
        db_table = 'historico_equipo' 
                
    
        
 