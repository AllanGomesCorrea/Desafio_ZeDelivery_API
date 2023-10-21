from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from partner.models import Partner, Nearest_Partner
from partner.serializers import PartnerSerializer, Nearest_PartnerSerializer
from math import sqrt
from shapely.geometry import Point, MultiPolygon, Polygon



class PartnerCreateListView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    #filterset_fields = ['id']
    filter_backends = (SearchFilter,)
    search_fields = ('tradingName', 'id')
    

    
    
class PartnerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    



class Nearest_PartnerCreateListView(generics.ListAPIView):
    serializer_class = Nearest_PartnerSerializer
    
    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        long = self.request.query_params.get('long')
        
        partners = Partner.objects.all()
        
        min_distance = float('inf')
        nearest_partner = None
        
        if lat and long:
            
            for partner in partners:
                partner_coordinates = partner.address.get("coordinates")

                # Crie um objeto Point para o ponto que você deseja verificar
                point = Point(lat, long)

                # Crie objetos Polygon para cada bloco com buracos
                polygons = []
                for polygon_coords in partner.coverageArea.get("coordinates"):
                    shell = polygon_coords[0]
                    holes = polygon_coords[1:]
                    polygon = Polygon(shell, holes=holes)
                    polygons.append(polygon)

                # Crie um objeto MultiPolygon com todos os polígonos
                multi_polygon = MultiPolygon(polygons)

                # Verifique se o ponto está dentro do MultiPolygon
                if point.within(multi_polygon):
                    
                    #Calcula a distância 
                    x1, y1 = float(lat),float(long)
                    x2, y2 = partner_coordinates
                    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                    if distance < min_distance:
                        min_distance = distance
                        nearest_partner = partner
            
            if nearest_partner:
                return [nearest_partner]
            else:
                return None
         
        return None  

             

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = self.get_serializer(queryset, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'detail': 'Nenhum estabelecimento encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    