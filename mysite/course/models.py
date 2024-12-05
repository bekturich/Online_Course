from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('преподаватель', 'преподаватель'),
        ('клиент', 'клиент'),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='клиент')
    full_name = models.CharField(max_length=32)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.CharField(max_length=32)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Lesson(models.Model):           #модели Уроков
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

class Assignment(models.Model):      #модели Заданий
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    students = models.ManyToManyField(UserProfile, related_name='assignmentss', blank=True)

    def __str__(self):
        return self.title

class Exam(models.Model):               #модели экзаменов
    title = models.CharField(max_length=52)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    passing_score = models.PositiveIntegerField()
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Certificate(models.Model):       #модели сертификатов
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f"{self.student} - {self.course}"

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Отзыв от {self.user} для {self.course}"

class Subscription(models.Model):             #модели подписки
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} подписался на {self.course}"

class Payment(models.Model):               #модели оплаты
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    STATUS_PAYMENT = (
        ('успешно', 'успешно'),
        ('неуспешно', 'неуспешно')
    )
    status = models.CharField(max_length=32, choices=STATUS_PAYMENT)

    def __str__(self):
        return f"Оплата по {self.user} для {self.course}"

class Webinar(models.Model):            #модели вебинары
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    title = models.CharField(max_length=52)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return f"Вебинар: {self.title} для {self.course}"

