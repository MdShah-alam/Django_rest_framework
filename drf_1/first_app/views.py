from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models , serializers
from rest_framework import generics , viewsets

# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerializers

# class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializers
    
class  CourseListCreateView(generics.ListCreateAPIView):
    queryset = models. Course.objects.all()
    serializer_class = serializers.CourseSerializers

class  CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models. Course.objects.all()
    serializer_class = serializers.CourseSerializers

# class StudentView(APIView):
#     def get(self, request):
#         student_data = models.StudentData.objects.all()
#         serializer = serializers.StudentSerializers(student_data, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = serializers.StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StudentDetailView(APIView):
#     def get(self, request, pk):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         snippet = models.StudentData.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)