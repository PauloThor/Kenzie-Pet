from rest_framework import serializers

class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    scientific_name = serializers.CharField()

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    characteristics = CharacteristicSerializer(many=True)
    group = GroupSerializer()


    


