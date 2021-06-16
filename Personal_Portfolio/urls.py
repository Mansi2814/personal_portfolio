from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mansi Mehndiratta Admin"
admin.site.site_title = "Mansi Mehndiratta's Admin Portal"
admin.site.index_title = "Welcome to Mansi Mehndiratta's Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mansimehndiratta.urls'))
]
