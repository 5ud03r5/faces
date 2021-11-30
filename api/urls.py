from django.urls import path, include
from .views import PostViewSet
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title="API")
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [

    path('', include(router.urls)),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema', schema_view),
    path('docs/', include_docs_urls(title='API docs'))



]