from concurrent import futures

import grpc
from django.core.management.base import BaseCommand

import payment_module.protos.account_pb2_grpc as payment_pb2_grpc
from payment_module.services import UserService  # Import your gRPC service implementation


class Command(BaseCommand):
    help = "Run gRPC server"

    requires_system_checks = []  # ✅ Fix: Ensure this is a list

    def handle(self, *args, **kwargs):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        payment_pb2_grpc.add_UserControllerServicer_to_server(UserService(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        print("✅ gRPC Server is running on port 50051...")
        server.wait_for_termination()
