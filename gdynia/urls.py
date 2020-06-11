from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import (
    AttractionList,
    AttractionDetailView,
    RegisterUserView,
    user_detail_view,
    like_attraction,
    change_password
)

from rest_framework import routers
from homepage.api_views import (
    AttractionsAPIView,
    AttractionDetailAPIView,
    UsersAPIView,
    RegisterNewUser,
    LikeUnlikeAPIView,
)
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

# URLs for views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AttractionList.as_view(), name='atracje'),
    path('atrakcja/<int:id>', AttractionDetailView.as_view(), name='atrakcja-szczegoly'),
    path('zmien-haslo/', change_password),
    path('polub/', like_attraction, name='polub'),
]

# URLs for user management
urlpatterns += [
    path(r'zaloguj/', auth_views.LoginView.as_view(), name='login'),
    path(r'wyloguj/', auth_views.LogoutView.as_view(), name='logout'),
    # path(r'zmien-haslo/', , name='change-password'),
    path(r'zarejestruj/', RegisterUserView.as_view(), name='sign_in'),
    path('uzytkownik/', user_detail_view, name='dane-uzytkownika'),
]

# routers for API
router = routers.DefaultRouter()
router.register(r'attractions', AttractionsAPIView)  # list of all attractions
router.register(r'attractiondetail', AttractionDetailAPIView)  # Details about one attraction
router.register(r'users', UsersAPIView)
router.register(r'register', RegisterNewUser)
router.register(r'likeunlike', LikeUnlikeAPIView)

# URLs for API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/login', obtain_auth_token, name='api-login'),
]

# URLs for static, media etc.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
