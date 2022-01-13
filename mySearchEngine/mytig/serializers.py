from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion, ProduitIsAvaible,ProduitStock

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')

class ProduitAvaibleSerializer(ModelSerializer):
    class Meta:
        model = ProduitIsAvaible
        fields = ('id', 'tigID')

class ProduitStockSerializer(ModelSerializer):
    class Meta:
        model = ProduitStock
        fields = ('tigID','inStock','sale','discount')