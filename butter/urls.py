from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from butter.views import UserView, AgreementView, SignAgreementView, UserAgreementsView


class OptionalSlashRouter(SimpleRouter):
    def __init__(self, trailing_slash="/?"):
        self.trailing_slash = trailing_slash
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

router.register("users", UserView, "users")
router.register("agreements", UserAgreementsView, "agreements")

urlpatterns = [
    path('agreement/', AgreementView.as_view()),
    path('sign_agreement/', SignAgreementView.as_view()),
]

urlpatterns += router.urls