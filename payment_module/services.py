from django.contrib.auth.models import User
from django_grpc_framework import generics

from .serializers import UserProtoSerializer


class UserService(generics.ModelService):
    queryset = User.objects.all()
    print("It is being hit")
    serializer_class = UserProtoSerializer

    def List(self, request, context):
        for user in self.queryset:
            yield self.serializer_class(user).message

    def Retrieve(self, request, context):
        user = self.queryset.get(id=request.id)
        return self.serializer_class(user).message


# catch is: everytime you change the services or any other files, you need to create the proto files again
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. payment_module/protos/account.proto
