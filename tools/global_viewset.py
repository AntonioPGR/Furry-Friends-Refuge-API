from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from tools.read_only_permission import ReadOnly

class GlobalViewSet(ModelViewSet):
  search_fields = ['nome']
  ordering = ['nome']
  permission_classes = [IsAdminUser|ReadOnly]