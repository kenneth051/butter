from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.renderers import StaticHTMLRenderer
from butter.serializers import UserSerializer, AgreementSerializer
from butter.models import User, UserTermsAgreement
from rest_framework.views import APIView
from butter.constants import agreement
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class UserView(ModelViewSet):
    """view for users"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SignAgreementView(APIView):
    """view to sign agreement"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(
            data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class AgreementView(APIView):
    """Agreement view to get both signed and un signed agreement"""
    renderer_classes = (StaticHTMLRenderer, )
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        data = agreement.format("---firstname---", "---lastname---", "---street---", "---postcode---", "")
        if request.user and request.user.id:
            user_agreement= UserTermsAgreement.objects.get(signed_user=request.user) 
            data=user_agreement.signed_agreement           
        return Response(data)
    
class UserAgreementsView(ModelViewSet):
    serializer_class = AgreementSerializer
    queryset = UserTermsAgreement.objects.all()
    http_method_names = ["get"]
