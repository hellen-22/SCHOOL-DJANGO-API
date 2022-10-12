from rest_framework_nested import routers
from  . import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)
router.register('lecturer', views.LecturerViewSet)


urlpatterns = router.urls
