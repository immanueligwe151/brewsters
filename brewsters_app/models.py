from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    categoryImage = models.CharField(max_length=100)

    class Meta:
        db_table = "category"
        managed = False

    def __str__(self):
        return self.categoryName

class ItemsList(models.Model):
    itemId = models.AutoField(primary_key=True)
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='itemslist')
    itemName = models.CharField(max_length=100)
    itemImage = models.CharField(max_length=100)
    itemDescription = models.CharField(max_length=100)
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "itemslist"
        managed = False

    def __str__(self):
        return self.itemName

#class Item(models.Model):
#    name = models.CharField(max_length=100)
#    description = models.TextField()
#    price = models.DecimalField(max_digits=10, decimal_places=2)

#    def __str__(self):
#        return self.name