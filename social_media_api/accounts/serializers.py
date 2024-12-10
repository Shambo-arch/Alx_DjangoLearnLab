from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()  # Dynamically get the user model (default or custom)

class RegistrationSerializer(serializers.ModelSerializer):
    # Explicitly define fields using serializers.CharField
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        """
        Check that the passwords match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """
        Create a user instance after validating and removing unnecessary fields.
        """
        validated_data.pop('confirm_password')  # Remove confirm_password before creating the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

