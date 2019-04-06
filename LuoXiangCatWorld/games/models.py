from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Cat(models.Model):
    #Fields
    cat_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20, help_text="Enter this cat's name")
    sex = models.CharField(max_length=10)
    birth = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    breed = models.CharField(max_length=20)
    intimacy = models.IntegerField()
    mather = models.CharField(max_length=10)
    mother = models.CharField(max_length=10)
    mate = models.CharField(max_length=10)
    health_status = (
        ('h', 'Healthy'),
        ('c', 'Cough'),
        ('p', 'Pregnant'),
    )

    health = models.CharField(max_length=1, choices=health_status, blank=True, default='h')

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=20, help_text="Explore with a lovely name")
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    sex = models.CharField(max_length=10)
    money = models.IntegerField()
    password = models.CharField(max_length=20)
    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Food(models.Model):
    food_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    effect = models.CharField(max_length=100)

    class Meta:
        ordering = ["-price", "name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Market(models.Model):
    market_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Park(models.Model):
    park_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Site(models.Model):
    site_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Stay(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    site = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["site", "cat"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + "'s" + "favorite place"

class Adopt(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    park = models.ForeignKey('Park', on_delete=models.SET_NULL, null=True)
    time = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["master", "cat"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + " and " + self.master.name + "'s first encounter"

class Wild(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    park = models.ForeignKey('Park', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["park"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + "'s old home"

class Enjoy(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["cat"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + "'s" + "favorite food"

class Store(models.Model):
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField()
    class Meta:
        ordering = ["master"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.master.name + "'s" + "refrigerator"

class Purchase(models.Model):
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    market = models.ForeignKey('Market', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField()

    class Meta:
        ordering = ["-num", "master"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.master.name + "'s" + "shopping"

class Sell(models.Model):
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    market = models.ForeignKey('Market', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField()

    class Meta:
        ordering = ["-num"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.market.name + "'s" + "cates"