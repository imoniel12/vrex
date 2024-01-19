from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('vrexApp.urls')),

  
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    
]
