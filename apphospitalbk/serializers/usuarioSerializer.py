from apphospitalbk.models import usuario
from rest_framework import serializers
from apphospitalbk.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_user', 'username', 'password', 'name_user', 'email_user',
        'create_date_user', 'estado_user', 'apellido_user', 'cargo_user', 'direccion_user','telefono_user']
 
    def create (self, validated_data):
        useruarioInstance = Usuario.objects.create(**validated_data)
        return useruarioInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id)
        return {
            'id_user':usuario.id_user, 
            'username':usuario.username, 
            'password':usuario.password, 
            'name_user':usuario.name_user, 
            'email_user':usuario.email_user,
            'create_date_user':usuario.create_date_user, 
            'estado_user':usuario.estado_user, 
            'apellido_user':usuario.apellido_user, 
            'cargo_user':usuario.cargo_user, 
            'direccion_user':usuario.direccion_user,
            'telefono_user':usuario.telefono_user,
        }