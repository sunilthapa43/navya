#
# from django.urls import path, include
#
# from payment_module.views import EsewaPaymentTestView
#
# urlpatterns = [
#     path('', EsewaPaymentTestView.as_view(), name='esewa_payment_test'),
# ]
from payment_module.protos import account_pb2_grpc
from payment_module.services import UserService

urlpatterns = []


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(
        UserService.as_servicer(), server
    )
