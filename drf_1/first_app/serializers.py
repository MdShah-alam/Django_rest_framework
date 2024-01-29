from rest_framework import serializers
from . import models

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    # courses = CourseSerializers(many=True , read_only=True)
    # courses = serializers.StringRelatedField(many=True)
    # courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    courses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course_details'
    )

    class Meta:
        model = models.StudentData
        fields = '__all__'
        
