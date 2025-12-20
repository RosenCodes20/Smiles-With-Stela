
from mother_gift.common.views import send_mail_ssl


class VisitorNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        if not request.session.get('visitor_notified', False):
            try:
                send_mail_ssl(
                    subject='Нов посетител на сайта',
                    message=f'IP адрес: {ip}\nПосетен път: {request.path}',
                    from_email='rrirrirri08@gmail.com',
                    recipient_list=['rrirrirri08@gmail.com'],
                )
                request.session['visitor_notified'] = True
            except:
                pass

        response = self.get_response(request)
        return response