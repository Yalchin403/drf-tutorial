from django.urls import include, path
from rest_framework import routers
from newApp.views import *
from snippets.views import *
from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]