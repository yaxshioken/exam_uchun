from cryptography.fernet import Fernet
from django.db import models
from rest_framework import serializers

from topshiriq1.models import Account


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


key = Fernet.generate_key()
cipher = Fernet(key)


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=255)

    def encrypt_fields(self):
        self.price = cipher.encrypt(str(self.price).encode()).decode()
        self.marja = cipher.encrypt(str(self.marja).encode()).decode()
        self.package_code = cipher.encrypt(self.package_code.encode()).decode()

    def decrypt_fields(self):
        self.price = float(cipher.decrypt(self.price.encode()).decode())
        self.marja = float(cipher.decrypt(self.marja.encode()).decode())
        self.package_code = cipher.decrypt(self.package_code.encode()).decode()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price", "marja", "package_code"]

    def create(self, validated_data):
        product = Product(**validated_data)
        product.encrypt_fields()
        product.save()
        return product

    def to_representation(self, instance):
        instance.decrypt_fields()
        return super().to_representation(instance)
