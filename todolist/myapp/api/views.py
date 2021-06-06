# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapp.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

@permission_classes((AllowAny, ))
class TaskListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo tasks for given requested user
        '''
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'), 
            'priority': request.data.get('priority'), 
            'description': request.data.get('description'),
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny, ))
class TaskFilterApiView(APIView):
    # add permission to check if user is authenticated
    def get_object(self, task_id):
        '''
        Helper method to get the object with given task_id
        '''
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

    def read_request(self, request):
        data = {}
        if request.data.get('name') != None:
            name = request.data.get('name')
            data["name"] = name

        if request.data.get('status') != None:
            status = request.data.get('status')
            data["status"] = status

        if request.data.get('description') != None:
            description = request.data.get('description')
            data["description"] = description

        if request.data.get('end_date') != None:
            end_date = request.data.get('end_date')
            data["end_date"] = end_date

        if request.data.get('priority') != None:
            priority = request.data.get('priority')
            data["priority"] = priority

        return data

    # 3. Retrieve
    def get(self, request, task_id, *args, **kwargs):
        '''
        Retrieves the Todo with given task_id
        '''
        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TaskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, task_id, *args, **kwargs):
        '''
        Updates the todo item with given task_id if exists
        '''
        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        data = self.read_request(request)
        serializer = TaskSerializer(instance = task_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, task_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        task_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )