from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("auction/", views.AuctionView, name="auction"),
	path("discount/", views.DiscountView, name="discount"),
	path("discount/finish/<str:domain_name>/", views.Discount2View, name="discount2"),
	path("all_discount/", views.AllDiscountView, name="all_discount"),
	path("account/", views.AccountView, name="account"),
	path("checkout/", views.CheckOutView, name="checkout"),

	path("find/", views.FindView, name="find"),
	path("result/<str:domain_name>/", views.ResultView, name="result"),
	path("buy/<str:domain_name>/", views.BuyView, name="buy"),
	path("finish/", views.FinishView, name="finish"),
	path("registered/", views.RegisteredView, name="registered"),
	path("manage/<str:domain_name>/", views.ManageView, name="manage"),
	path("docs/", views.DocsView, name="docs"),
	
	path("transfer/", views.Transfer1View, name="transfer1"),
	path("transfer/<str:domain_name>/<str:domain_namek>/finish/", views.Transfer2View, name="transfer2"),
	path("transfer/finish/", views.Transfer3View, name="transfer3"),
	
]