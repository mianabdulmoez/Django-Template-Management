from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]





# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('services/', views.services, name='services'),
#     path('pricing/', views.pricing, name='pricing'),
#     path('blog/', views.blog, name='blog'),
#     path('blog-details/', views.blog_details, name='blog-details'),
#     path('elements/', views.elements, name='elements'),
#     path('portfolio/', views.portfolio, name='portfolio'),
#     path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
#     path('team/', views.team, name='team'),
#     path('team-details/', views.team_details, name='team-details'),
#     path('faq/', views.faq, name='faq'),
#     path('404/', views.error_404, name='404'),
#     path('500/', views.error_500, name='500'),
# ]