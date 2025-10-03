from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    """
    Modelo de usuário customizado que estende o padrão do Django.
    """
    class Meta:
        db_table = 'users' # Nome da tabela no plural

class Profile(models.Model):
    """
    Armazena dados adicionais do usuário, como seu papel no sistema.
    """
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        PHOTOGRAPHER = 'PHOTOGRAPHER', 'Photographer'

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

    class Meta:
        db_table = 'profiles' # Nome da tabela no plural

    def __str__(self):
        return f"{self.user.username}'s Profile - {self.get_role_display()}"

class Client(models.Model):
    """
    Representa um cliente de um fotógrafo.
    """
    photographer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='clients'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254) # unique=True foi removido temporariamente, veja a nota abaixo
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients' # Nome da tabela no plural
        # Garante que um fotógrafo não pode ter dois clientes com o mesmo email.
        unique_together = ('photographer', 'email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    class StatusChoices(models.TextChoices):
        PLANNED = 'PLANNED', 'Planejado'
        IN_PROGRESS = 'IN_PROGRESS', 'Em Andamento'
        EDITING = 'EDITING', 'Em Edição'
        COMPLETED = 'COMPLETED', 'Concluído'
        ARCHIVED = 'ARCHIVED', 'Arquivado'

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANNED
    )
    project_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2) # Ex: 99999999.99
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.title