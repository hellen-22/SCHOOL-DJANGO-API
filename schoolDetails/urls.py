from rest_framework_nested import routers
from  . import views

router = routers.DefaultRouter()
router.register('school', views.SchoolViewSet)

school_departments_router = routers.NestedDefaultRouter(router, 'school' ,lookup='school')
school_departments_router.register('department', views.DepartmentViewSet, basename='department')

router.register('unit', views.UnitViewSet)

urlpatterns = router.urls + school_departments_router.urls
