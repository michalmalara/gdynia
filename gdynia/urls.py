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
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += staticfiles_urlpatterns()
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
