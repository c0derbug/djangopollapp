from django.urls import path, include


from .v1 import urls

urlpatterns = [
    #v1
    path('v1/', include(urls))
]