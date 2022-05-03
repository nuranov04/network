from django.utils import timezone

from apps.user.models import User


class LastActivity:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.last_activity = timezone.now()
            user.save()

# ==============ON FUNCTION===========(DON'T WORKING)


# def last_activity(get_response):
#     def middleware(request):
#         return get_response(request)
#
#     @staticmethod
#     def change_user_last_activity(request):
#         user = get_user(request)
#         if user.is_authenticated:
#             user = User.objects.get(id=request.user.id)
#             user.last_activity = timezone.now()
#             user.save()
#             # return user
#
#     middleware.change_user_last_activity = change_user_last_activity
#
#     return middleware
