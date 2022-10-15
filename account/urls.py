from rest_framework_nested import routers
from  . import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)
router.register('lecturer', views.LecturerViewSet)

student_router = routers.NestedDefaultRouter(router, 'student', lookup='student')
student_router.register('units', views.UnitDetailsViewSet, basename='units')
student_router.register('hostel', views.StudentHostelViewSet, basename='hostel')



urlpatterns = router.urls + student_router.urls
