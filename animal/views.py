from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from animal.serializers import AnimalSerializer
from .models import Animal, Group, Characteristic

from rest_framework import status

class AnimalView(APIView):
    def post(self, request):
        data = request.data
        group = data.pop('group')
        characteristics = data.pop('characteristics')
        new_group = ''
        
        if Group.objects.filter(name=group['name']).exists():
            new_group = Group.objects.get(name=group['name'])
        else:
            new_group = Group.objects.create(**group)   

        new_animal = Animal.objects.create(**data, group=new_group)

        for char in characteristics:
            new_char = ''
            char_name = char['name']

            if Characteristic.objects.filter(name=char_name).exists():
                new_char = Characteristic.objects.get(name=char_name)
            else:
                new_char = Characteristic.objects.create(name=char_name)

            new_animal.characteristics.add(new_char) 
        
        
        new_animal.save()
        
        serializer = AnimalSerializer(new_animal).data 

        return Response(serializer,status=status.HTTP_201_CREATED)
    

    def get(self, request):
        animal = Animal.objects.all()
        serializer = AnimalSerializer(animal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnimalById(APIView):
    def get(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            serializer = AnimalSerializer(animal)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Animal.DoesNotExist:
            return Response({"msg": "Nenhum animal encontrado"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()
            return Response('', status=status.HTTP_204_NO_CONTENT)
        except Animal.DoesNotExist:
            return Response({"msg": "Nenhum animal encontrado"}, status=status.HTTP_404_NOT_FOUND)
