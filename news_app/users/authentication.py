
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)
from rest_framework.exceptions import AuthenticationFailed

from users.models import AuthToken


class TokenAuthentication(BaseAuthentication):
    keyword = 'Token'
    model = AuthToken

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        if not len(auth) == 2:
            raise AuthenticationFailed('Использован не правильный токен')
        try:
            token = auth[1].decode()
        except UnicodeError:
            raise AuthenticationFailed('Использован не правильный токен')

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        model = self.model
        try:
            token = model.objects.select_related('user').get(token=token)
        except model.DoesNotExist:
            raise AuthenticationFailed('Использован не правильный токен')
        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword
