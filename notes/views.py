from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User, Note
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Additional logic if needed, e.g., create a token
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            print("ERR:::",serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(f"Received data: {request.data}")
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will create a new note
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteRetrieveAPIView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDeleteAPIView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteUpdateAPIView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteUpdateSerializer