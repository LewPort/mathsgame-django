from django.urls import path
from . import views  # Import the views from the same app

# Define URL patterns for this app
urlpatterns = [
    # Example: Map the root URL of the app to the `index` view
    path('', views.index, name='index'),
]
