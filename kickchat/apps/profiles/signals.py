from django.dispatch import receiver
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    import ipdb; ipdb.set_trace()