
from django.contrib import admin
from django.urls import path
from Python_crispyforms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base),
]
