from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from User.authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from User.serializers import UserSerializer 

from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from User.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .task import send_password_reset_email





class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            token = user.token

            return Response({'user_id': user.id, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token = user.token

            return Response({'user_id': user.id, 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class AuthTestView(APIView):
    
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        username = user.get_name()
        
        return Response({'username':username, 'logged_in':True}, status=status.HTTP_200_OK)
    



class PasswordResetAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'If the user is found, reset link should be emailed by now.'})

        # Generate a reset token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        reset_url = request.build_absolute_uri(reset_url)

        # Send the reset email
        send_password_reset_email.delay(user.id, reset_url)
        return Response({'detail': 'If the user is found, reset link should be emailed by now.'})

class PasswordResetConfirmAPIView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            # Valid token, allow user to reset password
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password reset successfully'})

        return Response({'detail': 'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)