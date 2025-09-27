from django.shortcuts import render
from .serializers import ProfileSerializer,TechnologySerializer,ProjectSerializer,WorkHistorySerializer
from .models import Profile,Technology,Project,WorkHistory
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer

@api_view(['GET'])
def ProfileApi(request, name):
    print(name)
    if request.method == "GET":
        try:
            profile = Profile.objects.filter(user__username=name).first()
            if profile is None:
                return Response(
                    {'detail': 'Profile not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            data = ProfileSerializer(profile).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def TechnologyApi(request, name,tid):
        if request.method == "GET":
            try:
                technology = Technology.objects.filter(profile__user__username=name,category_id=tid)
                data = TechnologySerializer(technology,many=True).data
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def ProjectApi(request, name):
        if request.method == "GET":
            try:
                project = Project.objects.filter(profile__user__username=name).order_by('sortorder')
                data = ProjectSerializer(project,many=True).data
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            




@api_view(['GET'])
def WorkHistoryApi(request, name):
        if request.method == "GET":
            try:
                workhistory = WorkHistory.objects.filter(profile__user__username=name)
                data = WorkHistorySerializer(workhistory,many=True).data
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def Portfolioview(request):
     return render(request,'app/Portfolioview.html')







        

