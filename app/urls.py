from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="Product price monitoring API",
    ),
    public=True,
)

urlpatterns = [
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
