from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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