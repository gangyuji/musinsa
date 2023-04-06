from django.db import models

class Product(models.Model):

    code = models.IntegerField(verbose_name="상품 코드")
    name = models.CharField(max_length=24, verbose_name="상품 이름")
    description = models.TextField(verbose_name="상품 설명")
    price = models.IntegerField(verbose_name="상품 가격")
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return self.code

