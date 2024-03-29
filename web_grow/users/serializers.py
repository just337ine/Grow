from rest_framework import serializers
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('email','username','password','first_name')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        password=validated_data.pop('password', None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    """ 
        Returns info about users and current user through two different views, 
        1. one will be authenticated request
        2. another will be a non-authenticated request.
    """
    class Meta:
        model=CustomUser
        fields=('email','username','first_name')
