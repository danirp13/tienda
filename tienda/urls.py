
from django.conf.urls import url,include
from django.contrib import admin
from productos.views import IndexView

urlpatterns = [
url(r'^productos/',include('productos.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('social_django.urls', namespace='social')),
 	url(r'^$', IndexView.as_view()),   
]

