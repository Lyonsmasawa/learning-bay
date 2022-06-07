from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupSerializer
from learning.models import Group

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/groups',
        'GET /api/groups/:id',
    ]

    return Response(routes)

@api_view(['GET'])
def getGroups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getGroup(request, pk):
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(group, many=False)

    return Response(serializer.data)