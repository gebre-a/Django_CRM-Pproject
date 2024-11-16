from django.urls import path
from . import views

urlpatterns = [
    # path("", admin.site.urls),
    path('', views.home, name='home'),
    path('logout/',views.logout_user , name ='logout'),
     path('register/', views.register_user, name='register'),
     path('record/<int:pk>', views.custemer_record,name='record'),
     path('delet_record/<int:pk>', views.delet_record, name='delet_record'),
     path('add_record/', views.add_record, name ='add_record'),
     path('Update_record/<int:pk>',views.Update_record,name='Update_record')
    ]
