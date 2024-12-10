from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('GymMembershipsApp.gym.urls')),
    path('users/', include('GymMembershipsApp.users.urls')),
    prefix_default_language=False
)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
