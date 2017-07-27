from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/$', views.GameListView.as_view(), name='games'),
    url(r'^games/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='game-detail'),
]
