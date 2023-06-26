from django import template

from userprofile.pseudonymize import pseudonymize

register = template.Library()

@register.filter
def formatted_first_name(first_name, pseudonymized):
    return pseudonymize('first_name', first_name) if pseudonymized else first_name

@register.filter
def formatted_last_name(last_name, pseudonymized):
    return pseudonymize('last_name', last_name) if pseudonymized else last_name

@register.filter
def formatted_email(email, pseudonymized):
    return pseudonymize('email', email) if pseudonymized else email

@register.filter
def formatted_username(username, pseudonymized):
    return pseudonymize('username', username) if pseudonymized else username
