# Django Authentication Notes
- Django provides a default User model for authentication and basic user management.
- However, for applications requiring additional user-specific data or custom authentication methods, a custom user model is often implemented
--  
## Default Django User Model: 
-The default User model, found in django.contrib.auth.models, 
includes fields such as
``` username, password, email, first_name, last_name, is_active, is_staff, is_superuser, and date_joined```
--
It handles user creation, password hashing, and permissions management. 
## Custom User Model: 
- A custom user model allows modification of the default user structure. 
- This is typically done by inheriting from either AbstractUser or AbstractBaseUser and PermissionsMixin. 

• AbstractUser: Used when retaining most of the default fields and authentication behavior but adding or modifying specific fields. 

    # myapp/models.py
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class CustomUser(AbstractUser):
        # Add custom fields here
        phone_number = models.CharField(max_length=15, blank=True, null=True)
        bio = models.TextField(blank=True)

• AbstractBaseUser: Used when a complete overhaul of the user model and potentially the authentication process is required, for instance, using email as the primary identifier instead of a username. 

    # myapp/models.py
    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
    from django.db import models
    from django.utils import timezone

    class CustomUserManager(models.Manager):
        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(email, password, **extra_fields)

    class CustomUser(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=30, blank=True)
        last_name = models.CharField(max_length=30, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=timezone.now)

        objects = CustomUserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        def __str__(self):
            return self.email

Configuring Django to use the Custom User Model: 
After defining the custom user model, Django must be informed to use it by setting AUTH_USER_MODEL in settings.py: 
# myproject/settings.py
AUTH_USER_MODEL = 'myapp.CustomUser' # Replace 'myapp' with your app's name
```
Important Note: A custom user model should be defined and configured at the beginning of a Django project, before running any migrations, as changing it later can lead to significant database migration complexities. 
```