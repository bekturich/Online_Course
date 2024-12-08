from django.template.base import render_value_in_context
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['Category_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name']


class CourseListSerializer(serializers.ModelSerializer):
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    get_count_good_grade = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level', 'get_avg_rating', 'get_count_people',
                  'get_count_good_grade']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_count_good_grade(self, obj):
        return obj.get_count_good_grade()


class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'category', 'level']


class LessonSerializer(serializers.ModelSerializer):
    course = CourseLessonSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    course = CourseLessonSerializer()
    students = UserProfileCourseSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    course = CourseLessonSerializer()

    class Meta:
        model = Exam
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    course = CourseLessonSerializer()
    student = UserProfileCourseSerializer()

    class Meta:
        model = Certificate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileCourseSerializer()
    course = CourseLessonSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserProfileCourseSerializer()
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    course = CourseLessonSerializer()

    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    payment_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileCourseSerializer()
    course = CourseLessonSerializer()

    class Meta:
        model = Payment
        fields = '__all__'


class WebinarSerializer(serializers.ModelSerializer):
    course = CourseLessonSerializer()
    start_time = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    end_time = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Webinar
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    updated_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    created_by = UserProfileCourseSerializer()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level', 'price', 'created_by',
                  'created_at', 'updated_at']

