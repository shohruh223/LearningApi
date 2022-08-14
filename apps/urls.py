from django.urls import path, include

urlpatterns = [
    path('', include('apps.billing.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.course.urls')),
]