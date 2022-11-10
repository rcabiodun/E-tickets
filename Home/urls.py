from django.urls import path
from .views import init_payment, trans ,delete_trans, log_out,verify_payment,advert,delete_single
urlpatterns = [
   path("", init_payment, name="home"),
   path("place-ads/",advert, name="advert"),
   path("payment/", trans, name="payments"),
#   path("printout/",printout,name='print'),
   path("payment/verification/<ref>/",verify_payment,name="verify-payment"),
   path("payment/delete/<trans_id>/", delete_trans, name="payments_delete"),
   path("payment_single/delete/<cust_id>/", delete_single, name="single_delete"),
   path("logout/", log_out, name="logout"),

   ]
