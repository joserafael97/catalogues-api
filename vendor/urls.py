from django.urls import include, path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register(r'vendors', views.VendorViewSet)

vendors_router = routers.NestedDefaultRouter(router, r"vendors", lookup="vendors")

vendors_router.register(r"products", views.ProductViewSet, basename="vendors-products")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path("api/", include(vendors_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]