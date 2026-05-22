from rest_framework.routers import DefaultRouter

from .views import (
    PromotionViewSet,
    InscriptionViewSet,
    CoursPlanifieViewSet,
    AnimerViewSet,
    FiliereViewSet,
    CursusViewSet,
    CoursViewSet,
    CursusCoursViewSet,
)

router = DefaultRouter()

router.register(r'promotions', PromotionViewSet)
router.register(r'inscriptions', InscriptionViewSet)
router.register(r'cours-planifies', CoursPlanifieViewSet)
router.register(r'animer', AnimerViewSet)

router.register(r'filieres', FiliereViewSet)
router.register(r'cursus', CursusViewSet)
router.register(r'cours', CoursViewSet)
router.register(r'cursus-cours', CursusCoursViewSet)

urlpatterns = router.urls
