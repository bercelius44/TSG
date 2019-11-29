from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(max_length = 40, unique=True)
    telefono = models.CharField(max_length = 10, unique=True)
    AREA = 'Area'
    PERSONA = 'Persona'
    STATUS = [ (AREA, ('Area')), (PERSONA, ('Persona'))]
    tipo = models.CharField(max_length = 8, choices = STATUS)

    class Meta:
        verbose_name_plural = "Responsables"
    
    def __str__(self):
        return self.nombre

class Resources(models.Model):
    serial = models.IntegerField(primary_key = True)
    id_encargado = models.ForeignKey(Responsable, default = 0, verbose_name = "Responsables", on_delete = models.CASCADE)    
    marca = models.CharField(max_length = 40)

    TEC = 'Tecnologia'
    OFC = 'Oficina'
    CAF = 'Cafeteria'
    STATUS = [ (TEC, ('Tecnologia')), 
               (OFC, ('Oficina')), 
               (CAF, ('Cafeteria'))]    
    tipo = models.CharField(max_length = 12, choices = STATUS)

    proveedor = models.CharField(max_length = 40)
    valor_comercial = models.CharField(max_length = 40)
    fecha_compra = models.DateField()

    BE = 'Buen Estado'
    ME = 'Mal estado'
    N = 'Nuevo'
    ST = [ (BE, ('Buen Estado')), 
           (ME, ('Mal estado')), 
           (N, ('Nuevo'))]  
    estado = models.CharField(max_length = 40, choices = ST)

    fecha_asignacion = models.DateField()
