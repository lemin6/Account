from rest_framework import serializers
from .models import *


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['first_name', 'last_name', 'birth_date']
