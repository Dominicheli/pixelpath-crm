from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    """
    Modelo de usuário customizado que estende o padrão do Django.
    A base para autenticação no sistema.
    """
    pass  # Por enquanto, não precisamos de campos adicionais aqui.

class Profile(models.Model):
    """
    Armazena dados adicionais do usuário, como seu papel no sistema.
    Cada usuário terá um, e apenas um, perfil.
    """
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        PHOTOGRAPHER = 'PHOTOGRAPHER', 'Photographer'
        # No futuro, podemos adicionar 'CLIENT', 'EDITOR', etc. aqui.

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(
        max_length=15,
        choices=RoleChoices.choices,
        default=RoleChoices.PHOTOGRAPHER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile - {self.get_role_display()}"