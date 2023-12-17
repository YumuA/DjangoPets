from django.urls import path, include
from rest_framework import routers
from .views import (
    ServicioViewSet, DuenoViewSet, LocalViewSet, MascotaViewSet,
    CitaViewSet, UserCreateViewSet, UserDetailViewSet,
    login_view
)

router = routers.DefaultRouter()
router.register('duenos', DuenoViewSet)
router.register('locales', LocalViewSet)
router.register('mascotas', MascotaViewSet)
router.register('citas', CitaViewSet)
router.register('servicios', ServicioViewSet)
router.register('users', UserDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/create_user/', UserCreateViewSet.as_view({'post': 'create'}), name='create_user'),
    path('api/login/', login_view, name='login'),
    path('api/citas/', CitaViewSet.as_view, name='Cita'),
]
