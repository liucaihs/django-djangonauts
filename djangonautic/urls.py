from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.about),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)