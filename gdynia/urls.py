"""gdynia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import AttractionList, AttractionDetailView

from rest_framework import routers
from homepage.api_views import AttractionsAPIView, AttractionDetailAPIView

router = routers.DefaultRouter()
router.register(r'attractions', AttractionsAPIView)  # list of all attractions
router.register(r'attractiondetail', AttractionDetailAPIView)  # Details about one attraction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('atrakcje', AttractionList.as_view(), name='atracje'),
    path('atrakcja/<int:id>', AttractionDetailView.as_view(), name='atrakcja-szczegoly'),
    path('api/', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
