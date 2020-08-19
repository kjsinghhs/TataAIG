
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'policyd', views.PolicyViewSet)
# router.register(r'policy_list', views.policy_list)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('policy_list/',views.policy_list),
    path('policy_list_user/<str:uname>',views.policy_list_user),
    path('policy_details/<int:policy_no>',views.policy_details),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]