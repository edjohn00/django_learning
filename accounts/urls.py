from django.urls import path
from . import views

urlpatterns = [
# unauthenticated users
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
# admin users
    path('', views.home, name='home'),

#customer users
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name="account"),

# admin users
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

]
'''
1 - Submit email form   for                 //PasswordResetView.as_view()
2 - Email sent successfuL message           //PasswordResetDoneView.as_view()
3 - Link to password resT form in email     //PasswordResetConfimView.as_view()
4 - Password successfuL message             //PasswordResetCompleteView.as_view()
'''