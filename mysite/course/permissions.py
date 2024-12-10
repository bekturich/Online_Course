from rest_framework import permissions


class CheckCreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'преподаватель'


class CheckTeacherCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class CheckCreateAssignment(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'преподаватель'


class CheckTeacherAssignmentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.created_by == request.user


class CheckCreateExam(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'преподаватель'


class CheckTeacherExamOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.created_by == request.user


class TeacherReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.course.created_by == request.user
        return False


#-----------------------student-----------------------

# class IsStudent(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role ==

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return False


class StudentLesson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_role == 'клиент'


class StudentExam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_role == 'клиент'


class StudentReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.method == 'POST' and request.user.role == 'клиент'


class StudentCertificate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user
