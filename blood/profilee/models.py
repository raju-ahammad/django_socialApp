from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save






class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    #username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email


class UserProfile(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHERS = 'others'

    GENDER_CHOICE = (
    (MALE, 'male'),
    (FEMALE, 'female'),
    (OTHERS, 'others'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=120, choices=GENDER_CHOICE, default=MALE)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    image = models.ImageField(default='default.png', blank = True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)



class Contact(models.Model):
    user_form = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_form_set', on_delete=models.CASCADE)
    user_to   = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_to_set', on_delete=models.CASCADE)
    created   = models.DateTimeField(auto_now_add=True, db_index=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False )


    def __str_(self):
        return '{} follows {}'.format(self.user_form, self.user_to)

User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
