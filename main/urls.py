from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("auction/", views.AuctionView, name="auction"),
	path("account/", views.AccountView, name="account"),
	path("checkout/", views.CheckOutView, name="checkout"),

	path("find/", views.FindView, name="find"),
	path("result/<str:domain_name>/", views.ResultView, name="result"),
	path("buy/<str:domain_name>/", views.BuyView, name="buy"),
	path("finish/", views.FinishView, name="finish"),
	path("registered/", views.RegisteredView, name="registered"),
	path("docs/", views.DocsView, name="docs"),
	path("transfer/<str:domain_name>/", views.Transfer2View, name="transfer2"),
	
	path("transfer/", views.TransferView, name="transfer"),
]