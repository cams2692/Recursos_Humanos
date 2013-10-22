from django.db import models
from publico.models import Persona

class TipoPermiso(models.Model):
	idTipo= models.AutoField(primary_key=True)
	nombrePermiso= models.CharField(max_length=50,null=False)
	def __unicode__(self):
		return self.nombrePermiso

class Permiso(models.Model):
	idPermiso= models.AutoField(primary_key=True)
	descripcion= models.CharField(max_length=100,null=False)
	fechaInicial= models.DateTimeField(auto_now=False, null=False)
	fechaFinal= models.DateTimeField(auto_now=False, null=False)
	tipo= models.ForeignKey(TipoPermiso)
	persona=models.ForeignKey(Persona)
	def __unicode__(self):
		return self.tipo

class TipoPago(models.Model):
	idTipo= models.AutoField(primary_key=True)
	nombrePago= models.CharField(max_length=40, null=False)
	def __unicode__(self):
		return self.nombrePago

class OtroPago(models.Model):
	idPago= models.AutoField(primary_key=True)
	valor= models.FloatField(null=False)
	fecha= models.DateField(auto_now=False)
	tipo= models.ForeignKey(TipoPago)
	def __unicode__(self):
		return self.tipo			

class Memorando(models.Model):
	idMemorando= models.AutoField(primary_key=True)
	memorandoFile= models.FileField(upload_to="docs/", null=False)
	fechaImpuesto= models.DateField(auto_now=False)
	persona= models.ForeignKey(Persona)
	def __unicode__(self):
		return self.Persona			
