from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        # Позволява автоматичен signup без форма
        return True

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        # Увери се, че имейлът се попълва
        if not user.email and data.get('email'):
            user.email = data['email']
        return user
