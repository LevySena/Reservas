from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def checkin(day,occup):
    if occup.data_ini <= day <= occup.data_fim+timedelta(days=1):
        return True
    return False



