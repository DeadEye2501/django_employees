from django.contrib import admin
from django.urls import path
from employees_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employees_list),
]
