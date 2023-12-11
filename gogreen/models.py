from django.db import models
from django.contrib.auth.models import User

class Plants(models.Model):
    #seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    # seller = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    botanical_name = models.CharField(max_length=30)
    cost = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.cost}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plants = models.ManyToManyField(Plants)  # Change to ManyToManyField
    quantity = models.IntegerField(default=1)
    total_cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
