from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from core.settings import MODE
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView


api_info = openapi.Info(
    title=" AllNotify API",
    default_version="v1",
    contact=openapi.Contact(
        email="eliseugaspar4@gmail.com",
        name="Eliseu Gaspar",
        url="",
    ),
    license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
    api_info, public=True, permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Users.urls'))
]

if MODE == "Development":
    urlpatterns += [
        path("openapi-schema/", schema_view.as_view(), name="openapi-schema"),
        path(
            "docs/",
            TemplateView.as_view(
                template_name="swagger.html",
                extra_context={"schema_url": "openapi-schema"},
            ),
            name="swagger-ui",
        ),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
