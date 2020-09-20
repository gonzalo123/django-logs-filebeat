from django.urls import path

from app.views import Info, Debug, Error

urlpatterns = [
    path('info', Info.as_view(), name='info'),
    path('error', Error.as_view(), name='error'),
    path('debug', Debug.as_view(), name='debug'),
]
