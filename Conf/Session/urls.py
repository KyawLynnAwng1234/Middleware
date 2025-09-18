# In your app's urls.py file
from django.urls import path
from . import views

urlpatterns = [
    # URL to set the session data.
    path('set_session/', views.set_session_data, name='set_session_data'),
    
    # URL to show the session data and increment the visit count.
    path('show_session/', views.show_session_data, name='show_session_data'),
]
