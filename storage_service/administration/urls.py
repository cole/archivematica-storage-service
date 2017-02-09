from django.conf.urls import url
from administration import views

urlpatterns = [
    # Sorted by alphabetized categories

    url(r'^$', views.settings_edit,
        name='settings_edit'),

    url(r'^version/$', views.version_view,
        name='version'),

    url(r'^users/$', views.user_list,
        name='user_list'),
    url(r'^users/create/$', views.user_create,
        name='user_create'),
    url(r'^users/(?P<id>[-\w]+)/edit/$', views.user_edit,
        name='user_edit'),

    url(r'^keys/$', views.key_list, name='key_list'),
    url(r'^keys/create/$', views.key_create, name='key_create'),
    url(r'^keys/import/$', views.key_import, name='key_import'),

]
