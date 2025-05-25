from django.urls import path
from .views import IndexView, RelatorioView, AposentadoView,CedidoView,FalecidoView,ServidorView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('relatorio/', RelatorioView.as_view(), name='relatorio'),
    path('aposentado/', AposentadoView.as_view(), name='aposentado'),
    path('servidor/', ServidorView.as_view(), name='servidor'),
    path('cedido/', CedidoView.as_view(), name='cedido'),
    path('falecido/', FalecidoView.as_view(), name='falecido'),
    
    
]
