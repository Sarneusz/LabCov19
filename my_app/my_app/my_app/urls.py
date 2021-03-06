"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app import views
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from api_app.views import SendResults,main,visitsList, NewVisit

# Create a router and register our viewsets with it.
router = DefaultRouter()



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', main),
    path('router', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout, name="logout"),
    path('signup/', views.Register.as_view(), name="signup"),
    path('dashboard', visitsList,name="dashboard"),
    path('results', SendResults,name="results"),
    path('main', main),
    path('newvisit', NewVisit,name="newvisit"), #rejestracja wizyty
]
