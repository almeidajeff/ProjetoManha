from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjetoManha.views.home', name='home'),
    # url(r'^ProjetoManha/', include('ProjetoManha.foo.urls')),


    url(r'^concursos/', include('concursos.urls')),
    url(r'^empresa/', include('empresa.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
