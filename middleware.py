from django.core.mail import send_mail

from mother_gift.common.views import send_mail_ssl


class VisitorNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        send_mail_ssl(
            subject='Нов посетител на сайта',
            message=f'IP адрес: {ip}\nПът: {request.path}',
            from_email='rrirrirri08@gmail.com',
            recipient_list=['rrirrirri08@gmail.com'],
        )

        response = self.get_response(request)
        return response
