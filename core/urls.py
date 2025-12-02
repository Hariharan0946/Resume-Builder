from django.contrib import admin
from django.urls import path
from home.views import home, gen_resume

urlpatterns = [
    path('', home, name='home'),
    path('resume/', gen_resume, name='resume'),
    path('admin/', admin.site.urls),
]