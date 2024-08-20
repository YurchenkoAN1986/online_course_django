from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, Lesson, Subscription, UserBalance
from .serializers import ProductSerializer, LessonSerializer, SubscriptionSerializer, UserBalanceSerializer
from django.contrib.auth.models import User
from django.db.models import Count

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        product = self.get_object()
        user = request.user
        try:
            balance = UserBalance.objects.get(user=user)
            if product.price > balance.balance:
                return Response({"detail": "Недостаточно средств"}, status=status.HTTP_400_BAD_REQUEST)

            balance.balance -= product.price
            balance.save()

            # Распределение в группу
            total_students = Subscription.objects.filter(product=product).count()
            group_number = (total_students % 10) + 1

            # Создание подписки
            Subscription.objects.create(user=user, product=product, group=group_number)

            return Response({"detail": "Оплата прошла успешно, доступ предоставлен"}, status=status.HTTP_200_OK)

        except UserBalance.DoesNotExist:
            return Response({"detail": "Пользователь не имеет баланса"}, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class UserBalanceViewSet(viewsets.ModelViewSet):
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer
    http_method_names = ['get', 'patch']
