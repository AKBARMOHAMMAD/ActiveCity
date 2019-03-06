from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from ActiveCity import settings

urlpatterns = [
    path('ac_admin/', TemplateView.as_view(template_name='index.html'), name='ac_officer/index')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)