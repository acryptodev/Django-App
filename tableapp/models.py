from django.db import models
import uuid
from django.core.validators import validate_email
from ckeditor.fields import RichTextField
# Create your models here.
GENDER_CHOICES = (
       ('man','Man'),
       ('woman', 'Woman'),
    )
class Table1(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100, help_text="Enter The Name")
	phone = models.CharField(max_length=100, help_text="Enter the phone number")
	bday = models.DateField('Birthday')
	mail = models.EmailField(max_length = 254, help_text="Enter the e-mail")
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	updated_on = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
class Table2(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100, help_text="Enter The Name")
	gender = models.CharField(max_length=100, choices=GENDER_CHOICES, help_text="Select the Gender")
	interests = models.CharField(max_length=100, help_text="Enter the interests")
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	updated_on = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
class Table3(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100, help_text="Enter The Name")
	university = models.CharField(max_length=100, help_text="Enter the University")
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	updated_on = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
class Newsfeed(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	subject = models.CharField(max_length=300)
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	updated_on = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.subject
		