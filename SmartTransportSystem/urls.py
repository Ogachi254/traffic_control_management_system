from django.contrib import admin
from django.urls import path, include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('accounts/', include('accounts.urls')),
    path('smartTracking/', include('smartTracking.urls'))
]
