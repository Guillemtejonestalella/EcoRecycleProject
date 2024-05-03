from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(verbose_name='Category', max_length=70, null=False, unique=True)
    CategoryPoints = models.IntegerField(verbose_name='Category Points', null = False)
    CategoryImage = models.ImageField(verbose_name="Category Image", upload_to="ecoApp/static/asstets/img", null=False, blank=False)
    CategoryBrands = models.JSONField(default=list)

    def __str__(self):
        return self.CategoryName
    
    class Meta:
        db_table = 'Categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']   