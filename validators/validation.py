from django.core.exceptions import ValidationError
def nameValidation(name):
    if len(name)<=1:
        raise ValidationError("Name must at least 2 characters")
    return name

def contactNoValidator(contact):
    if len(contact)<8 or not contact.isdigit():
        raise ValidationError("Please enter valid contact number")

