from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from publication.views import PublicationsView, CommentView, LikesView, PostLikesView
from user.views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('signin', LoginView.as_view(), name='rest_login'),
    path('signup', RegisterView.as_view(), name='rest_register'),
    path('', PublicationsView.as_view({'get': 'list'})),
    path('silk/', include('silk.urls', namespace='silk')),
    path('post/create', PublicationsView.as_view({'post': 'create'})),
    path('post/<int:pk>', PublicationsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('post/<int:pk>/likes', PostLikesView.as_view()),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('like/<int:pk>', LikesView.as_view())
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
