from rest_framework import exceptions, serializers

from users.models import AuthToken, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует.'
            )
        return username
    
    def create(self, validated_data):
        user = User(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = AuthToken
        fields = ['username', 'password', 'token']
        read_only_fields = ['token']

    def validate_username(self, username):
        if not User.objects.filter(
            username=username).exists():
            raise exceptions.ValidationError(
                'Пользователь с таким именем не существует')
        return username

    def create(self, validated_data):
        user = User.objects.get(username=validated_data.get('username'))
        token = AuthToken(user=user)
        token.save()
        return token

    def to_representation(self, instance):
        return {
            "username": instance.user.username,
            "token": instance.token
        }
