
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import StudentViewSet
from auth_app.views import UserViewSet
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

router = DefaultRouter()
router.register('stu', StudentViewSet, 'student')
router.register('user', UserViewSet, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/', include(router.urls)),
    path('access/', token_obtain_pair),
    path('refresh/', token_refresh)
]
