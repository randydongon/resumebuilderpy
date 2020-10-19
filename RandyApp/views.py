from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RandyApp.models import TypesOfResume, Profile
from RandyApp.serializers import TypesOfResumeSerializer, ProfileSerializer

from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def typesofresumeApi(request, id=0):
    if request.method == 'GET':
        typesofresume = TypesOfResume.objects.all()
        typesofresume_serializer = TypesOfResumeSerializer(
            typesofresume, many=True)
        return JsonResponse(typesofresume_serializer.data, safe=False)
    elif request.method == 'POST':
        typesofresume_data = JSONParser().parse(request)
        typesofresume_serializer = TypesOfResumeSerializer(
            data=typesofresume_data)
        if typesofresume_serializer.is_valid():
            typesofresume_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Unable to add new resume.", safe=False)

    elif request.method == 'PUT':
        typesofresume_data = JSONParser().parse(request)
        typesofresume = TypesOfResume.objects.get(
            ResumeId=typesofresume_data['ResumeId'])
        typesofresume_serializer = TypesOfResumeSerializer(
            typesofresume, data=typesofresume_data)
        if typesofresume_serializer.is_valid():
            typesofresume_serializer.save()
            return JsonResponse("updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        typesofresume = TypesOfResume.objects.get(ResumeId=id)
        typesofresume.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


@csrf_exempt
def profileApi(request, id=0):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        profiles_serializer = ProfileSerializer(
            profiles, many=True)
        return JsonResponse(profiles_serializer.data, safe=False)
    elif request.method == 'POST':
        profiles_data = JSONParser().parse(request)
        profiles_serializer = ProfileSerializer(
            data=profiles_data)
        if profiles_serializer.is_valid():
            profiles_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Unable to add new Profile.", safe=False)

    elif request.method == 'PUT':
        profiles_data = JSONParser().parse(request)
        profiles = Profile.objects.get(
            ProfileId=profiles_data['ProfileId'])
        profiles_serializer = ProfileSerializer(
            profiles, data=profiles_data)
        if profiles_serializer.is_valid():
            profiles_serializer.save()
            return JsonResponse("updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        profiles = Profile.objects.get(ProfileId=id)
        profiles.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
