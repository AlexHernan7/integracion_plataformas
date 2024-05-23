from rest_framework import serializers
from .models import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'usuario', 'nombre_completo', 'motivo', 'mensaje']
        read_only_fields = ['usuario']

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['usuario'] = request.user
        return super().create(validated_data)
