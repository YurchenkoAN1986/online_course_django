from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def lesson_count(self):
        return self.lessons.count()

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    product = models.ForeignKey(Product, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    group = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def __str__(self):
        return f'{self.user.username} - {self.balance} бонусов'

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        super().save(*args, **kwargs)

def create_user_balance(sender, instance, created, **kwargs):
    if created:
        UserBalance.objects.create(user=instance)

models.signals.post_save.connect(create_user_balance, sender=User)
