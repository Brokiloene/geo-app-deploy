from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('createsession/', views.create, name='create_session'),
    path('getuser/<int:ses_id>/', views.getuser, name='get_user_cords'),    
    path('getzone/<int:ses_id>/', views.getzone, name='get_zone_cords'),
    path('gettarg/<int:ses_id>/', views.gettarg, name='get_target_cords'),
    path('adduser/<int:ses_id>/', views.adduser, name='add_user_cords'),
    path('addzone/<int:ses_id>/', views.addzone, name='add_zone_cords'),
    path('addtarg/<int:ses_id>/', views.addtarg, name='add_target_cords'),
    path('endsession/<int:ses_id>/', views.endsession, name='delete_session'),
]
