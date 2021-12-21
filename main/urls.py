from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('Jewelry', views.jewelry_view, name='jewelry'),
    # path('jewelries', views.JewelryListView.as_view(), name='jewelry-list'),
    path('About', views.about_view, name='about'),
    path('jewelry_htmx/', views.jewelry_htmx, name='jewelry_htmx'),
    path('test_url/<str:param>', views.test_url, name='test_url'),
    path('jewelry_htmx/<int:jewel_id>/', views.jewel_view, name='jewel'),
]

# todo:
# complete dynamic query with htmx for jewelry todo by sunday
# real purchase integration
# shopping page todo by sunday
# dynamic account profile with htmx todo by sunday
# about page todo by sunday
# populate with real stock (Lucy)
# frontend design todo by sunday if have time
# homepage todo by sunday
