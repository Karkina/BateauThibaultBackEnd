from django.urls import path
from mytig import views

urlpatterns = [
    path('infoproducts/', views.RedirectionListeDeProduits.as_view()),
    path('infoproduct/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('putonsale/<int:pk>/<int:newprice>/', views.PutOnsale.as_view()),
    path('infopoissons/',views.RedirectionPoissons.as_view()),
    path('infocrustaces/',views.RedirectionCrustaces.as_view()),
    path('infofruitdemers/',views.RedirectionFruitDeMer.as_view()),
    path('incrementStock/<int:pk>/<int:number>/<int:prix>',views.RedirectionIncrementStock.as_view()),
    path('decrementStock/<int:pk>/<int:number>/<int:prix>', views.RedirectionDecrementStock.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('shipPoints/', views.RedirectionShipLists.as_view()),
    path('shipPoint/<int:pk>/', views.PromoDetail.as_view()),
    path('avaibleproducts/', views.AvaibleList.as_view()),
    path('avaibleproduct/<int:pk>/', views.AvaibleDetail.as_view()),
]
