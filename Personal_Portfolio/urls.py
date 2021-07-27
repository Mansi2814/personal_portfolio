from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Mansi Mehndiratta Admin"
admin.site.site_title = "Mansi Mehndiratta's Admin Portal"
admin.site.index_title = "Welcome to Mansi Mehndiratta's Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mansimehndiratta.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)