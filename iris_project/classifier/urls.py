from django.urls import path
from .views import classify_iris, iris_form

urlpatterns = [
    path("", iris_form, name="iris_form"),
    path('predict/', classify_iris),
    

]
