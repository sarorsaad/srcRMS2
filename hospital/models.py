from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"




# Create your models here.
# Modalities=(
#     ('CT','CT'),
#     ('US','US'),
#     ('MRI','MRI'),
#     ('Mammogram','Mammogram'),
# )

# Study_part=(
#      ('Abdomen','Abdomen'),
#      ('KUB','KUB'),
#     ('OB less than 14 Weeks','OB less than 14 Weeks '),
#      ('OB  more than 14 Weeks','OB more than 14 Weeks '),
#     ('Brain','Brain'),
#      ('Neck','Neck'),
#     ('Chest','Chest'),
   
#      ('pelvis','pelvis'),
#      ('pan-CT','pan-CT'),
     
#     ('thyroid','thyroid'),
#      ('breast','breast'),
#     ('scrotal','scrotal'),

#      ('cervical spine','cervical spine'),
#      ('L/S spine','L/S spine'),
#     ('D/L spine','D/L spine'),

#     ('doppler-venous-lower','doppler-venous-lower'),
#     ('doppler-arterial-lower','doppler-arterial-lower'),
#     ('doppler-venous-upper','doppler-venous-upper'),
#     ('doppler-arterial-upper','doppler-arterial-upper'),
   
    
#     ('all spine','all spine'),
#      ('Shoulder','Shoulder'),
#      ('elbow','elbow'),
#        ('wrist&hand','wrist&hand'),
#      ('hip','hip'),
#        ('knee','knee'),
#      ('ankle&foot','ankle&foot'),
#        ('superficial-MSK','superficial-MSK'),
       
# )

# Side_label =(

#     ('right','right'),
#     ('left','left'),
#     ('all','all'),
# )


# Nationalty=(
#     ('Suadi','Suadi'),
#     ('Non Suadi','Non Suadi'),
# )

# SEX=(
#     ('Male','Male'),
#     ('Female','Female'),
# )

# Deparment=(
#     ('Surgery','Surgery'),
#     ('IMC','IMC'),
#     ('OBG','OBG'),
#     ('Pedia','Pedia'),
#     ('Ortho','Ortho'),
#     ('ENT','ENT'),
#     ('Opthalomo','Opthalomo'),
#     ('Others','Others'),
# )

# doctor_name=(
#     ('HAMID ALHADI','HAMID ALHADI'),
#     ('MOHAMED ALHADI','MOHAMED ALHADI'),
#     ('MOHMD A/GADER','MOHMD A/GADER'),
#     ('Pedia','Pedia'),
#     ('Ortho','Ortho'),
#     ('ENT','ENT'),
#     ('Opthalomo','Opthalomo'),
#     ('Others','Others'),
# ) 

# Unit_name =(
#     ('ER','ER'),
#     ('pedia_ward','pedia_ward'),
#     ('male_ward','male_ward'),
#     ('female_ward','female_ward'),
#     ('OB_ward','OB_ward'),
#     ('L&D_ward','L&D_ward'),
#     ('covid_ward','covid_ward'),
#     ('OPD','OPD'),
#     ('refferal','referral'),
    
# ) 

# Status_FLAG=(
#     ('Top_Emergency','Top_Emergency'),
#     ('Emergency','Emergency'),
#     ('Routine','Routine'),
  

# )


# class Patient(models.Model):
#     MRN = models.CharField(_(' MRN '),max_length=30, null=True)
#     name = models.CharField(_(' name '),max_length=30, null=True)
#     ID_number=models.CharField(_('ID_number') ,max_length=30 , null=True)
#     date=models.DateField(default=timezone.now)
#     age = models.CharField(_('  age '),max_length=30, null=True)
#     SEX = models.CharField(_('SEX'), max_length = 10,choices=SEX, null=True)
#     Nationality  = models.CharField(_('Nationalty'), max_length = 10,choices=Nationalty, null=True)
#     Unit_name = models.CharField(_('Unit_name'), max_length = 30,choices=Unit_name , null=True)
#     flag = models.CharField(_('Flag'), max_length = 30,choices=Status_FLAG, null=True)
#     Modalities = models.CharField(_('Modalities'), max_length = 30,choices=Modalities, null=True)
    
#     Study_part = models.CharField(_('Study_part'), max_length = 30,choices=Study_part , null=True)
#     Side_label = models.CharField(_('Side_label '), max_length = 30,choices=Side_label  , null=True)
#     Other_study = models.CharField(_(' Other_study'),max_length=30, null=True)
#     Deparment = models.CharField(_('Deparment'), max_length = 10,choices=Deparment, null=True)
#     doctor_name = models.CharField(_(' doctor_name '), max_length = 30,choices=doctor_name, null=True)
    
#     clinical_indication = models.TextField(_(' clinical_indication '),max_length=300, null=True)
#     provisional_diagnosis = models.TextField(_(' provisional_diagnosis '),max_length=30, null=True)
