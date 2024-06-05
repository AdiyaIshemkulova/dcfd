from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    
    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='цена')

    in_stock = models.BooleanField(default=True) 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

