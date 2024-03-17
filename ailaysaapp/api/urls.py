from django.urls import path
from ailaysaapp.api.views import UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView, stream_sentence,CategoryListAPIView,    PostListAPIView,  PostDetailAPIView,    PostFilterTitleNoneAPIView,   PostFilterRecentCommentsAPIView,  PostFilterCreatedAtAPIView,     PostDeleteAPIView
    
 
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update-destroy'),
    path('stream-sentence/', stream_sentence, name='stream-sentence'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/filter/title-none/', PostFilterTitleNoneAPIView.as_view(), name='post-filter-title-none'),
    path('posts/filter/recent-comments/', PostFilterRecentCommentsAPIView.as_view(), name='post-filter-recent-comments'),
    path('posts/filter/created-at/', PostFilterCreatedAtAPIView.as_view(), name='post-filter-created-at'),
    path('posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
]
