from rest_framework import routers
from .views import Top3Teachers
from django.urls import include, path


router = routers.SimpleRouter()
# router.register(r'teachers', Top3Teachers)
urlpatterns = [
    path('top/', Top3Teachers.as_view())
]