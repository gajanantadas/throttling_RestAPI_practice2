from django.contrib import admin
from django.urls import path,include
from employeeapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.EmployeeList.as_view()),
    path('create/',views.EmployeeCreate.as_view()),
    path('update/<int:pk>',views.EmployeeUpdate.as_view()),
    path('del/<int:pk>',views.EmployeeDestroy.as_view()),

]
