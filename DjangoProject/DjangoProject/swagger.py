from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SWAGGER_DESCRIPTION = """
Documentation page for describing, visualizing and testing endpoints
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Receipt API",
      default_version='v1',
      description=SWAGGER_DESCRIPTION,
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)