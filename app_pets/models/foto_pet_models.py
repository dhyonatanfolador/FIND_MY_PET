from django.db import models

# Create your models here.
class FotoPetModels(models.Model):
    pet = models.ForeignKey('PetModels', on_delete=models.CASCADE)
    caminho_imagem = models.ImageField(upload_to='fotos_pets/')
    descricao = models.CharField(max_length=255, blank=True)
    principal = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'FotoPetModels(pet="{self.pet.nome}", caminho_imagem="{self.caminho_imagem}")'
