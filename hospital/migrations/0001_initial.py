# Generated by Django 3.2 on 2022-10-23 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MRN', models.CharField(max_length=30, null=True, verbose_name=' MRN ')),
                ('name', models.CharField(max_length=30, null=True, verbose_name=' name ')),
                ('ID_number', models.CharField(max_length=30, null=True, verbose_name='ID_number')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('age', models.CharField(max_length=30, null=True, verbose_name='  age ')),
                ('SEX', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name='SEX')),
                ('Nationality', models.CharField(choices=[('Suadi', 'Suadi'), ('Non Suadi', 'Non Suadi')], max_length=10, null=True, verbose_name='Nationalty')),
                ('Unit_name', models.CharField(choices=[('ER', 'ER'), ('pedia_ward', 'pedia_ward'), ('male_ward', 'male_ward'), ('female_ward', 'female_ward'), ('OB_ward', 'OB_ward'), ('L&D_ward', 'L&D_ward'), ('covid_ward', 'covid_ward'), ('OPD', 'OPD'), ('refferal', 'referral')], max_length=30, null=True, verbose_name='Unit_name')),
                ('flag', models.CharField(choices=[('Top_Emergency', 'Top_Emergency'), ('Emergency', 'Emergency'), ('Routine', 'Routine')], max_length=30, null=True, verbose_name='Flag')),
                ('Modalities', models.CharField(choices=[('CT', 'CT'), ('US', 'US'), ('MRI', 'MRI'), ('Mammogram', 'Mammogram')], max_length=30, null=True, verbose_name='Modalities')),
                ('Study_part', models.CharField(choices=[('Abdomen', 'Abdomen'), ('KUB', 'KUB'), ('OB less than 14 Weeks', 'OB less than 14 Weeks '), ('OB  more than 14 Weeks', 'OB more than 14 Weeks '), ('Brain', 'Brain'), ('Neck', 'Neck'), ('Chest', 'Chest'), ('pelvis', 'pelvis'), ('pan-CT', 'pan-CT'), ('thyroid', 'thyroid'), ('breast', 'breast'), ('scrotal', 'scrotal'), ('cervical spine', 'cervical spine'), ('L/S spine', 'L/S spine'), ('D/L spine', 'D/L spine'), ('doppler-venous-lower', 'doppler-venous-lower'), ('doppler-arterial-lower', 'doppler-arterial-lower'), ('doppler-venous-upper', 'doppler-venous-upper'), ('doppler-arterial-upper', 'doppler-arterial-upper'), ('all spine', 'all spine'), ('Shoulder', 'Shoulder'), ('elbow', 'elbow'), ('wrist&hand', 'wrist&hand'), ('hip', 'hip'), ('knee', 'knee'), ('ankle&foot', 'ankle&foot'), ('superficial-MSK', 'superficial-MSK')], max_length=30, null=True, verbose_name='Study_part')),
                ('Side_label', models.CharField(choices=[('right', 'right'), ('left', 'left'), ('all', 'all')], max_length=30, null=True, verbose_name='Side_label ')),
                ('Other_study', models.CharField(max_length=30, null=True, verbose_name=' Other_study')),
                ('Deparment', models.CharField(choices=[('Surgery', 'Surgery'), ('IMC', 'IMC'), ('OBG', 'OBG'), ('Pedia', 'Pedia'), ('Ortho', 'Ortho'), ('ENT', 'ENT'), ('Opthalomo', 'Opthalomo'), ('Others', 'Others')], max_length=10, null=True, verbose_name='Deparment')),
                ('doctor_name', models.CharField(choices=[('HAMID ALHADI', 'HAMID ALHADI'), ('MOHAMED ALHADI', 'MOHAMED ALHADI'), ('MOHMD A/GADER', 'MOHMD A/GADER'), ('Pedia', 'Pedia'), ('Ortho', 'Ortho'), ('ENT', 'ENT'), ('Opthalomo', 'Opthalomo'), ('Others', 'Others')], max_length=30, null=True, verbose_name=' doctor_name ')),
                ('clinical_indication', models.TextField(max_length=300, null=True, verbose_name=' clinical_indication ')),
                ('provisional_diagnosis', models.TextField(max_length=30, null=True, verbose_name=' provisional_diagnosis ')),
            ],
        ),
    ]