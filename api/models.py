from django.db import models

# Create your models here.
class Department(models.Model):
    
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Doctors(models.Model):

    
    name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    experience = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=15)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='doctor')


    def __str__(self):
        return self.name
    
class Patient(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(null=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Appointment(models.Model):

    doctor_id = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    patient_id =models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(null=True)

class MedicalRecord(models.Model):
    
    doctor_id = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    patient_id =models.ForeignKey(Patient,on_delete=models.CASCADE)
    disease = models.CharField(max_length=200)
    diagnosis_date = models.DateTimeField()
    treatment_plan = models.TextField(null =True)
    status = models.CharField(max_length=50, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')], default='ongoing')




