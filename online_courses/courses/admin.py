from django.contrib import admin
from .models import Product, Lesson, Subscription, UserBalance

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(UserBalance)
