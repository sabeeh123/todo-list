
from django.urls import path , include
from.import views

app_name = "activity"
urlpatterns = [
    path('list',views.activity_list,name='list')
]