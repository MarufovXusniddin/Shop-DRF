from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    category = serializers.IntegerField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.name = validated_data.get('price', instance.price)
        instance.name = validated_data.get('category', instance.category)
        instance.description = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class ReviewSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    text = serializers.FloatField()
    pub_date = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('product', instance.product)
        instance.name = validated_data.get('author', instance.author)
        instance.name = validated_data.get('text', instance.text)
        instance.description = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

