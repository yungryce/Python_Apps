from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    disco = serializers.SerializerMethodField(read_only=True )
    class Meta:
        model =   Product
    
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            # 'get_discount',
            'disco', 
        ]
    
    # to rename get_discount on model to disco in serializer
    def get_disco(self, obj):
        return obj.get_discount()

    
