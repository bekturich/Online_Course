from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'lesson', LessonViewSet, basename='lesson_list')
router.register(r'assignment', AssignmentViewSet, basename='assignment_list')
router.register(r'exam', ExamViewSet, basename='exam_list')
router.register(r'certificate', CertificateViewSet, basename='certificate_list')
router.register(r'review', ReviewViewSet, basename='review_list')
router.register(r'subscription', SubscriptionViewSet, basename='subscription_list')
router.register(r'payment', PaymentViewSet, basename='payment_list')
router.register(r'webinar', WebinarViewSet, basename='webinar_list')

urlpatterns = [
    path('', include(router.urls)),
    path('', CourseListAPIView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
]
