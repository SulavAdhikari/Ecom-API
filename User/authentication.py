from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from User.models import User
from ecom.settings import JWT_SECRET
import jwt


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        auth_header = request.META.get('HTTP_AUTH', b'')
        if not auth_header:
            return None

        try:        
            _, token = auth_header.split()
            decoded_payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])            
            user_id = decoded_payload.get('user_id')
            user = User.objects.get(pk=user_id)
            return (user, None)
        except jwt.ExpiredSignatureError:
            # Token has expired
            raise AuthenticationFailed('Token has expired')
        except (jwt.InvalidTokenError, ValueError, User.DoesNotExist):
            # Invalid token or user not found
            raise AuthenticationFailed('Invalid token')



