from rest_framework import serializers
from .models import Liveroom,ManagerbUandL,ProhibitbUandL

class LiveroomSerializer(serializers.ModelSerializer):

    ownername = serializers.ReadOnlyField(source='Owner.NickName')
    class Meta:
        model = Liveroom
        fields = '__all__'

class ManagerbUandLSerializer(serializers.ModelSerializer):

    ownername = serializers.ReadOnlyField(source='Owner.NickName')
    class Meta:
        model = ManagerbUandL
        fields = '__all__'

class ProhibitbUandLSerializer(serializers.ModelSerializer):

    ownername = serializers.ReadOnlyField(source='Owner.NickName')
    class Meta:
        model = ProhibitbUandL
        fields = '__all__'