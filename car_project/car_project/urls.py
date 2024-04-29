from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('car_app.urls')),
    # Add the following line for the root path
    path('', include('car_app.urls')),  # You can change 'car_app.urls' to the appropriate app
]
