from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import UserSerializer
from .login_serializer import LoginSerializer
from django.contrib.auth import authenticate
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=False, methods=['post'])
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            
            correo_electronico = data.get('correo_electronico', None)
            if correo_electronico is None:
                return Response({'message': 'El campo correo_electronico es requerido'}, status=status.HTTP_400_BAD_REQUEST)
            
            existing_user = User.objects.filter(correo_electronico=correo_electronico).first()
            if existing_user:
                return Response({'message': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        correo_electronico = serializer.validated_data['correo_electronico']
        contrasena = serializer.validated_data['contrasena']
        existing_user = User.objects.filter(correo_electronico=correo_electronico).first()
        print(correo_electronico)
        print(contrasena)
        #user = authenticate(correo_electronico="Huachimingo.colbunezco@gmail.com", contrasena="123456")
        #print(user)
        if existing_user and existing_user.contrasena == contrasena:
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)