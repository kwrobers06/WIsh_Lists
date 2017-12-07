from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^create$',views.create),
    url(r'^logout$', views.logout),
    url(r'^home$',views.home),
    url(r'^add$', views.add),
    url(r'^add_to_wishlist/(?P<item_id>\d+)$', views.add_to_wishlist),
    url(r'^remove_from_wishlist/(?P<item_id>\d+)$', views.remove_from_wishlist),
    url(r'^delete/(?P<item_id>\d+)$',views.delete),
    url(r'^show_item/(?P<item_id>\d+)$', views.show_item),

    
   
]