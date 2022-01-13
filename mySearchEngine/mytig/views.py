import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from mytig.config import baseUrl
from rest_framework.exceptions import NotFound
from mytig.models import ProduitStock
from mytig.serializers import ProduitStockSerializer
# Create your views here.

class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):
                    val = serializer.data['inStock']
                    sale = serializer.data['sale']
                    discount = serializer.data['discount']
                    break
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            jsondata['inStock']=val
            jsondata['sale'] = sale
            jsondata['discount'] = discount
            return Response(jsondata)
        except:
            raise Http404


class RedirectionIncrementStock(APIView):
    def get(self, request, pk,number, format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):
                    ProduitStock.objects.filter(tigID=pk).delete()
                    val = serializer.data['inStock'] + number
                    serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': val})
                    if serializer.is_valid():
                        serializer.save()
                    break

            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            jsondata['inStock'] = val
            return Response(jsondata)
        except:
            raise Http404

class RedirectionDecrementStock(APIView):
    def get(self, request, pk,number, format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):
                    val = serializer.data['inStock'] - number
                    if(val <0):
                        raise NotFound('Plus de stock')
                    else:
                        ProduitStock.objects.filter(tigID=pk).delete()
                        serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': val})
                        if serializer.is_valid():
                            serializer.save()
                    break

            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            jsondata['inStock'] = val
            return Response(jsondata)
        except:
            raise Http404

class PutOnsale(APIView):
    def get(self, request, pk, newprice, format=None):
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if (serializer.data['tigID'] == pk):
                    if(newprice <0):
                        raise Http404
                    else:
                        ProduitStock.objects.filter(tigID=pk).delete()
                        serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': serializer.data['inStock'],'sale':True,'discount':newprice})
                        if serializer.is_valid():
                            serializer.save()
                    break
            return HttpResponse(status=200)
        except:
            raise Http404


class RedirectionShipLists(APIView):
    def get(self, request, format=None):
        try:
            response = requests.get(baseUrl+'shipPoints/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

class RedirectionDetailShipList(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'shipPoint/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class RedirectionPoissons(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==0:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404

class RedirectionCrustaces(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==1:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404

class RedirectionFruitDeMer(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==2:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404


from mytig.models import ProduitEnPromotion,ProduitIsAvaible
from mytig.serializers import ProduitEnPromotionSerializer,ProduitAvaibleSerializer
from django.http import Http404
from django.http import JsonResponse

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)


class AvaibleList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitIsAvaible.objects.all():
            serializer = ProduitAvaibleSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class AvaibleDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitIsAvaible.objects.get(pk=pk)
        except ProduitIsAvaible.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitAvaibleSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
