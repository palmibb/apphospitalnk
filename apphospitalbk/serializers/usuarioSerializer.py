from apphospitalnk.apphospitalbk.models import usuario
from rest_framework import serializers
from apphospitalbk.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'name', 'email',]
 
    def create (self, validated_data):
        useruarioInstance = Usuario.objects.create(**validated_data)
        return useruarioInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id)
        return {
            'id': usuario.id,
            'username':usuario.username, 
            'password': usuario.password, 
            'name': usuario.name, 
            'email': usuario.email,
        }