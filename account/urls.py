from rest_framework_nested import routers
from  . import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)
router.register('lecturer', views.LecturerViewSet)

student_unit_router = routers.NestedDefaultRouter(router, 'student', lookup='student')
student_unit_router.register('units', views.UnitDetailsViewSet, basename='units')


urlpatterns = router.urls + student_unit_router.urls
