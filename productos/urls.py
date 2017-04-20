from django.conf.urls import url
from productos import views
from productos.views import IndexView

urlpatterns =[
url(r'^$',views.first_view, name='first_view'),
	url(r'^marca/$', views.marca, name='marca-list'),
	url(r'^marca/(?P<marca_id>[0-9]+)/detail/$', views.marca_detail, name='marca-detail'),

	url(r'^zapato/$', views.ZapatoListView.as_view(), name='zapato-list'),
	url(r'^zapato/(?P<pk>[0-9]+)/detail/$', views.ZapatoDetailView.as_view(), name='zapato-detail'),

	url(r'^zapato/(?P<pk>[0-9]+)/update/$', views.ZapatoUpdate.as_view(), name='zapato-update'),
	url(r'^zapato/(?P<pk>[0-9]+)/delete/$', views.ZapatoDelete.as_view(), name='zapato-delete'),

	url(r'^$', IndexView.as_view()),
]