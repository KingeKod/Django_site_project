from django.db import models

class TechDepartment(models.Model):
	technical_department =  models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	office = models.IntegerField()
	
	def __str__(self):
		return str(self.office)
		
	class Meta:
		verbose_name = 'Офис'
		verbose_name_plural = 'Офисы'
				
class Indicate(models.Model):
	group_indicator = models.CharField(max_length = 50)
	indicator = models.CharField(max_length = 50)
	
	def __str__(self):
		return " : ".join([self.group_indicator, self.indicator])
		
	class Meta:
		verbose_name = 'Показатель'
		verbose_name_plural = 'Показатели'

class DepartmentOffice(models.Model):
	office = models.ForeignKey(TechDepartment, on_delete = models.CASCADE)
	id_group = models.ForeignKey(Indicate, on_delete = models.CASCADE)
	value = models.IntegerField()
	date = models.DateTimeField()
	
	class Meta:
		verbose_name = 'Значение по показателю'
		verbose_name_plural = 'Значения по показателям'

	def __str__(self):
		return str(self.value)

