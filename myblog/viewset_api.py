from rest_framework import viewsets
from myblog.serializers import BlogPostSerializer
from myblog.models import BlogPost

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer