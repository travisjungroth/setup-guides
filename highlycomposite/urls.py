from django.contrib import admin
from django.urls import path, include

from highlycomposite import views as highly_composite_views
from guides import views as guide_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', highly_composite_views.Home.as_view(), name='home'),
    path('heartbeat/', highly_composite_views.heartbeat, name='heartbeat'),
    path('guides/', guide_views.GuideList.as_view(), name='guide-list'),
    path('guides/<slug:slug>/', guide_views.GuideDetail.as_view(), name='guide-detail'),
    path('steps/', guide_views.StepList.as_view(), name='step-list'),
    path('steps/<slug:slug>/', guide_views.StepDetail.as_view(), name='step-detail'),
]
