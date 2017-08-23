from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', 'contacts.views.splash', name='index'),
    #url(r'^$', views.splash, name='splash'),
    #url(r'^$', 'contacts.views.splash'),

    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details')
    #url(r'^details/(?P<mDetails>\w{0,50})/$', views.details, name='details')
    #url(r'^search/(?P<id>\w{0,50})/$', views.search, name='search')
    #url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details')
    #(r'^search/(\w+)/$', ProfileSearchListView.as_view()),
]
