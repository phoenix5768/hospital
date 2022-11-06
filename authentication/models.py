from django.db import models
import uuid


class Patient(models.Model):

    STATUS_TYPE = (
        ('Married', 'Married'),
        ('Not Married', 'Not Married'),
    )

    BLOOD_TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    )

    date_of_birth = models.DateField('Date of birth')
    iin_number = models.CharField('IIN', max_length = 12)
    id_number = models.BigAutoField(primary_key = True)
    #id_number = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    fname = models.CharField('First Name', max_length = 50)
    mname = models.CharField('Middle Name', max_length = 50, null = True, blank = True)
    lname = models.CharField('Last Name', max_length = 50)
    blood_group = models.CharField('Blood group', max_length = 5, choices = BLOOD_TYPE)
    emergency_contact_number = models.CharField('Emergency contact number', max_length = 12)
    contact_number = models.CharField('Contact Number', max_length = 12)
    email = models.EmailField('Email address', max_length = 254)
    address = models.CharField('Physical address', max_length = 1024)
    martial_status = models.CharField('Martial status', max_length = 20, choices = STATUS_TYPE)
    registration_date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.fname + ' ' + self.lname


    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Doctor(models.Model):
    DEGREE_OF_EDUCATION = (
        ('No Education', 'No Education'),
        ('High School Diploma', 'High School Diploma'),
        ('Certificate or associate degree', 'Certificate or associate degree'),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ('Doctorate', 'Doctorate'),
    )

    RATING = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )


    date_of_birth = models.DateField('Date of birth')
    iin_number = models.CharField('IIN', max_length = 12)
    id_number = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    fname = models.CharField('First Name', max_length = 50)
    mname = models.CharField('Middle Name', max_length = 50, null = True, blank = True)
    lname = models.CharField('Last Name', max_length = 50)
    contact_number = models.CharField('Contact Number', max_length = 12)
    department_id = models.IntegerField('Department ID')
    specialization_details_id = models.IntegerField('Specialization Details ID')
    experience = models.CharField('Experience In Years', max_length = 4)
    #photo = models.ImageField(null = True, blank = True, upload_to = "images/")
    category = models.CharField('Category', max_length = 100)
    price = models.DecimalField('Price', max_digits = 10, decimal_places = 2)
    schedule_details = models.CharField('Schedule Details', max_length = 100)
    education = models.CharField('Degree of Education', max_length = 50, choices = DEGREE_OF_EDUCATION)
    rating = models.CharField('Rating', max_length = 3, choices = RATING)
    address = models.CharField('Address', max_length = 1024)


    def __str__(self):
        return self.fname + ' ' + self.lname 
    

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

