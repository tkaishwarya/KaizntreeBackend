# dashboard/views.py
from rest_framework import viewsets, permissions
from .models import Item, Category, Tag
from .serializers import ItemSerializer, CategorySerializer, TagSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Default queryset
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        """
        Optionally restricts the returned items to a given category,
        by filtering against a `category` query parameter in the URL.
        """
        queryset = Item.objects.all()
        category = self.request.query_params.get('category', None)
        tags = self.request.query_params.getlist('tags', None)
        stock_status = self.request.query_params.get('stock_status', None)
        
        if category is not None:
            queryset = queryset.filter(category__name=category)
        
        if tags:
            queryset = queryset.filter(tags__name__in=tags).distinct()
        
        if stock_status is not None:
            queryset = queryset.filter(stock_status=(stock_status.lower() == 'true'))

        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
