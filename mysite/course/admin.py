from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(Webinar)