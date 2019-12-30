from django.urls import path, include
from .views import home, celery


urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery')
]