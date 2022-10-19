from cgitb import lookup
from rest_framework_nested import routers
from  . import views

router = routers.DefaultRouter()
router.register('school', views.SchoolViewSet)
router.register('unit', views.UnitViewSet)
router.register('hostel', views.HostelViewSet, basename='hostel')

school_router = routers.NestedDefaultRouter(router, 'school' ,lookup='school')
school_router.register('department', views.DepartmentViewSet, basename='department')

unit_router = routers.NestedDefaultRouter(router, 'unit', lookup='unit')
unit_router.register('result', views.UnitResultViewSet, basename='result')


urlpatterns = router.urls + school_router.urls + unit_router.urls