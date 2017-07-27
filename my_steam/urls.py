from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/$', views.GameListView.as_view(), name='games'),
    url(r'^games/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='game-detail'),
    url(r'^games/(?P<pk>\d+)/update/$', views.GameUpdateView.as_view(), name='update-game'),
]
