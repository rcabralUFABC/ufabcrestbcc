from django.conf.urls import url, include
from rest_framework import routers
from restUFABC.quickstart import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'banks', views.BanksViewSet)

router.register(r'turmas', views.TurmaViewSet)
router.register(r'alunosnotas', views.AlunoNotasViewSet)
router.register(r'alunoslistas', views.AlunoListaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]