from django.urls import include, path
from rest_framework import routers
from . import  views

app_name="tickets"

router = routers.DefaultRouter()
router.register('Geust',views.viewset)
router.register('Moive',views.viewset_moive )
router.register('Restraion',views.viewset_reserivation )

urlpatterns = [
    path("api1/",views.firts_way,name='Firts_Way_Api'),
    path("api2/",views.seconed_way,name='Seconed_Way_Api'),
    path("api3/",views.RestWay,name='Rest_FrameWork_Way_Api'),
    path("api3/<int:pk>/",views.Rest_Framework_Way,name='Rest_FrameWork_Way_Api2'),
    path("api4/",views.Rest_FBV1.as_view(),name='Class_Based_views1'),
    path("api4/<int:pk>/",views.Rest_FBV2.as_view(),name='Class_Based_views2'),
    path("api5/",views.mixins_list_create.as_view(),name='mixins_list_create'),
    path("api5/<int:pk>/",views.mixins_retrive_update_destory.as_view(),name='mixins_retrive_update_destory'),
    path("api6/",views.generics.as_view(),name='generics'),
    path("api6/<int:pk>/",views.generics_pk.as_view(),name='generics_pk'),
    path('api7/', include(router.urls)),
    
]
