from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_csrf_token
from .templatetags import custom_filters

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


ADMIN_ENABLED = False

def block_admin(request):
    return HttpResponseForbidden("Доступ запрещён")

def home(request):
    return HttpResponse("Главная страница сайта. Админка отключена или включена.")

def home(request):
    return HttpResponse("Xush Kelibsiz KRAFTO-AGENCY Admin   - http://127.0.0.1:8000/ <- yonidan admin/ shu sozmi yozing -- http://127.0.0.1:8000/admin/ javob shunday bolishi kerak")

class AdminAccessControlMiddleware:
    ALLOWED_IPS = ['127.0.0.1']  # разрешённые IP для доступа к админке

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META.get('REMOTE_ADDR') not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Доступ к админке запрещён")
        return self.get_response(request)

schema_view = get_schema_view(
    openapi.Info(
        title="DRF SHOP API",
        default_version='v1',
        description="Tash-Cleaning",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rizotoha1978@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

item_id_param = openapi.Parameter('id', openapi.IN_PATH, description="ID объекта", type=openapi.TYPE_INTEGER, example=123)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/get-csrf-token/", get_csrf_token),
    path('', home, name='home'),
    path("api/ckeditor5/", include('django_ckeditor_5.urls')),
    path("api/base/", include('base.urls')),
    path("api/slug_category/", include('slug_category.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/shop/", include('shop.urls')),
    path("api/locations/", include('locations.urls')),
    path("api/video/", include('video.urls')),
    path("api/comment/", include('comment.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("api/user/", include('user.urls')),
    path("api/category_card/", include('category_card.urls')),
    path("api/calendars/", include('calendars.urls')),
    path("api/inventory/", include('inventory.urls')),
    path("api/clientlogo/", include('clientlogo.urls')),
    path("api/blog/", include('blog.urls')),
    path("api/category/", include('category.urls')),
    path("api/notifications/", include('notifications.urls')),
    path('api/application', include('application.urls')),
    path('api/telegram_orders/', include('telegram_orders.urls')),
    path("api/card/", include('card.urls')),
    path("api/botmessages/", include('botmessages.urls')),
    path("api/category_title/", include('category_title.urls')),
    path("api/category_title_text/", include('category_title_text.urls')),
    path("api/company/", include('company.urls')),
    path("api/logo/", include('logo.urls')),
    path("api/promotions/", include('promotions.urls')),
    path("api/contact/", include('contact.urls')),
    path("api/language/", include('language.urls')), 
    path("api/telegram_notify/", include('telegram_notify.urls')),
    path("api/location/", include('location.urls')),
    path("api/services/", include('services.urls')),
    path("api/team/", include('team.urls')),
    path("api/myblogyourapp/", include('myblogyourapp.urls')),
    path("api/question_and_answer/", include('question_and_answer.urls')),
    path('api/token-auth/', obtain_auth_token),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # redirect to swagger
    path('', lambda request: redirect('schema-swagger-ui')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if ADMIN_ENABLED:
    urlpatterns.append(path('admin/', admin.site.urls))