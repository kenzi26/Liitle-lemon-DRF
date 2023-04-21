from django.urls import path 
from .import views 

from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('groups/manager/users', views.managers)
] 

# david "2df1144edeca6cc7008284d534debe37f1468574"
# kika "666c2471fef66fe16a9972c23f311fcbff070234"
#     path('menu-items/<int:pk>', views.single_item()),
# path('ratings', views.RatingsView.as_view()), 
