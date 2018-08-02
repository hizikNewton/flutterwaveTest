
from django.conf.urls import url
from shoes.views import shoeListView as Index
from shoes.views import shoeDetailView,shoeSlugDetailView

urlpatterns = [    
    url(r'^(?P<pk>\d+)/$',shoeDetailView.as_view()),
    
    url(r'^(?P<slug>[\w-]+)/$',shoeSlugDetailView.as_view()),

    url(r'^$',Index.as_view(),name = 'index'),

]
