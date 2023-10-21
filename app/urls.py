from django.contrib import admin
from django.urls import path
from partner.views import PartnerCreateListView, PartnerRetrieveUpdateDestroyView, Nearest_PartnerCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('partner/', PartnerCreateListView.as_view(), name= 'partner-create-list'),
    path('partner/<int:pk>', PartnerRetrieveUpdateDestroyView.as_view(), name= 'partner-detail-view'),
    
    path('nearest_partner/', Nearest_PartnerCreateListView.as_view(), name= 'nearest-partner-create-list'),
]
