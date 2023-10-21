from rest_framework import serializers
from partner.models import Partner, Nearest_Partner

class PartnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Partner
        fields = '__all__'
        


class Nearest_PartnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Partner
        fields = '__all__'