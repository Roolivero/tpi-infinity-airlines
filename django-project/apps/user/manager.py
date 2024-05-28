from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Invalid email"))
        
    def create_user(self, email, first_name, last_name, dni, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("email address is required"))
        if not first_name:
            raise ValueError(_("first name is required"))
        if not last_name:
            raise ValueError(_("last name address is required"))
        if not dni:
            raise ValueError(_("email address is required"))
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, dni=dni, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, first_name, last_name, dni, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(email, first_name, last_name, dni, password, **extra_fields)


    def get_by_id(self, id):
        try:
            return self.get(pk=id)
        except ObjectDoesNotExist:
            return None
    
    def update_by_id(self, id, **kwargs):
        try:
            instance = self.get(pk=id)
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
            return True
        except self.model.DoesNotExist:
            return False
    
    def delete_by_id(self, id):
        try:
            instance = self.get_by_id(id)
            instance.delete()
            return True
        except ObjectDoesNotExist:
            return False
        
    def get_by_email(self, emial):
        try:
            return self.get(emial=emial)
        except ObjectDoesNotExist:
            return None
        
    def get_by_password(self, password):
        try:
            return self.get(password=password)
        except ObjectDoesNotExist:
            return None

    def list_all(self):
        return self.all()