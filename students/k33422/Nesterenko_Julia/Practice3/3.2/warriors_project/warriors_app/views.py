from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from .models import *
from .serializers import *


class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
   def post(self, request):
       profession = request.data.get("profession")
       serializer = ProfessionCreateSerializer(data=profession)

       if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()

       return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
   def get(self, request):
       skills = Skill.objects.all()
       serializer = SkillSerializer(skills, many=True)
       return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
   def post(self, request):
       skill = request.data.get("skill")
       serializer = SkillSerializer(data=skill)

       if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()

       return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorListProfessionAPIView(ListAPIView):
   serializer_class = WarriorProfessionSerializer
   queryset = Warrior.objects.all()


class WarriorListSkillAPIView(ListAPIView):
   serializer_class = WarriorSkillSerializer
   queryset = Warrior.objects.all()


class WarriorOneAPIView(RetrieveAPIView):
   serializer_class = WarriorFullSerializer
   queryset = Warrior.objects.all()


class WarriorDeleteAPIView(RetrieveDestroyAPIView):
   serializer_class = WarriorFullSerializer
   queryset = Warrior.objects.all()


class WarriorEditAPIView(RetrieveUpdateAPIView):
   serializer_class = WarriorFullSerializer
   queryset = Warrior.objects.all()