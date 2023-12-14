from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def check_username(self, username):
        return self.filter(username=username).exists()
