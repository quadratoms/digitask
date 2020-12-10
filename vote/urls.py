from django.urls import path
from .views import entry, vote, home, logout


urlpatterns = [
    path('', home, name='home'),
    path('entry/', entry, name='entry'),
    path('vote/', vote, name='vote'),
    path('logout/', logout, name='logout')
]
