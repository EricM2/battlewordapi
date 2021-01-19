from django.urls import include, path
from rest_framework import routers
from . import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

#router = routers.DefaultRouter()
#router.register(r'orders', views.OrderViewSet, basename='orders')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('openapi/', get_schema_view(
        title="selira API",
        description="battleword developer API"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('word/add/', views.addWord),
    path('subscriber/add/', views.addSubscriber),
    path('subscribers/', views.listSubscriber),
    path('words/<int:stage>/<int:limit>/<str:language>/', views.listWord),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]