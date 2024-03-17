# ailaysa task 1
from rest_framework import generics, filters
from ailaysaapp.models import UserProfile,Category,PostModel
from ailaysaapp.api.serializer import UserProfileSerializer,CategorySerializer,PostSerializer
from rest_framework.pagination import PageNumberPagination
# ailaysa task 2
from django.http import StreamingHttpResponse
import time
# ailaysa task 3
from django.http import JsonResponse
from ailaysaapp.celery.tasks import count_words_in_file


# ailaysa task 1
class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# ailaysa task 2


def stream_sentence(request):
    def generate_sentence():
        sentences = [
"om namashivaya namaha. AAAAleelooo ailaysaa aaaleeeloo......aaaleeloo ailaysaa aaaleeloo ailaysaaa"
        ]
        for sentence in sentences:
            yield sentence + '\n'
            time.sleep(2)  

    return StreamingHttpResponse(generate_sentence(), content_type="text/plain")



# ailaysa task 3
def process_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        # Save the uploaded file to a temporary location
        with open('temp_file.txt', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        # Call the Celery task to count words in the file asynchronously
        result = count_words_in_file.delay('temp_file.txt')
        return JsonResponse({'task_id': result.id}, status=202)
    else:
        return JsonResponse({'error': 'File not provided or invalid method.'}, status=400)
    
    
    
    
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
    

class PostListAPIView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostFilterTitleNoneAPIView(generics.ListAPIView):
    queryset = PostModel.objects.filter(title=None)
    serializer_class = PostSerializer

class PostFilterRecentCommentsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all().order_by('-comments__publication_date')
    serializer_class = PostSerializer

class PostFilterCreatedAtAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        comments_count = instance.comments.count()
        instance.delete()
        if comments_count == 0:
            return
        instance.comments.all().delete()