from django.urls import path, include
from .views import home, signup
from .views import MyLoginView, MylogoutView

urlpatterns = [
    path('', home, name='home' ),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
]
