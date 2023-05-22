from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.core import exceptions
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ['phone', 'password', 'password1']

    def validate(self, attrs):
        password = attrs.get('password')
        password1 = attrs.get('password1')

        if password != password1:
            raise serializers.ValidationError(_('Passwords doesnt match!'))

        try:
            validate_password(password)
        except exceptions.ValidationError as error:
            raise serializers.ValidationError(list(error.messages))

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return CustomUser.objects.create_user(**validated_data)


class CustomAuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('phone')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
