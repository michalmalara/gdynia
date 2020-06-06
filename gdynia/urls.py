from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import AttractionList, AttractionDetailView, RegisterUserView

from rest_framework import routers
from homepage.api_views import AttractionsAPIView, AttractionDetailAPIView, UsersAPIView, RegisterNewUser
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'attractions', AttractionsAPIView)  # list of all attractions
router.register(r'attractiondetail', AttractionDetailAPIView)  # Details about one attraction
router.register(r'users', UsersAPIView)
router.register(r'register', RegisterNewUser)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AttractionList.as_view(), name='atracje'),
    path('atrakcja/<int:id>', AttractionDetailView.as_view(), name='atrakcja-szczegoly'),

    path(r'zaloguj/', auth_views.LoginView.as_view(), name='login'),
    path(r'wyloguj/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'zarejestruj/', RegisterUserView.as_view(), name='sign_in'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/login', obtain_auth_token, name='api-login'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
