from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^games/$', views.GameListView.as_view(), name='games'),
    url(r'^my_games/$', views.UserGamesList.as_view(), name='my-games'),
    url(r'^games/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='game-detail'),
    url(r'^games/(?P<pk>\d+)/update/$', views.GameUpdateView.as_view(), name='update-game'),
    url(r'^games/(?P<pk>\d+)/delete/$', views.GameDeleteView.as_view(), name='delete-game'),
    url(r'^games/add/$', views.GameCreateView.as_view(), name='add-game'),
]
