from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name='api'

router=SimpleRouter()
router.register("users",views.UserViewSet,basename="users")
router.register("posts",views.PostViewSet,basename="posts"),
urlpatterns=router.urls