# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from payment_module.protos import (
    account_pb2 as payment__module_dot_protos_dot_account__pb2,
)

GRPC_GENERATED_VERSION = "1.70.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + " but the generated code in payment_module/protos/account_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class UserControllerStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
            "/account.UserController/List",
            request_serializer=payment__module_dot_protos_dot_account__pb2.UserListRequest.SerializeToString,
            response_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            _registered_method=True,
        )
        self.Create = channel.unary_unary(
            "/account.UserController/Create",
            request_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            response_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            _registered_method=True,
        )
        self.Retrieve = channel.unary_unary(
            "/account.UserController/Retrieve",
            request_serializer=payment__module_dot_protos_dot_account__pb2.UserRetrieveRequest.SerializeToString,
            response_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            _registered_method=True,
        )
        self.Update = channel.unary_unary(
            "/account.UserController/Update",
            request_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            response_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            _registered_method=True,
        )
        self.Destroy = channel.unary_unary(
            "/account.UserController/Destroy",
            request_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True,
        )


class UserControllerServicer:
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_stream_rpc_method_handler(
            servicer.List,
            request_deserializer=payment__module_dot_protos_dot_account__pb2.UserListRequest.FromString,
            response_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            response_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
        ),
        "Retrieve": grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=payment__module_dot_protos_dot_account__pb2.UserRetrieveRequest.FromString,
            response_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            response_serializer=payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
        ),
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=payment__module_dot_protos_dot_account__pb2.User.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "account.UserController", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("account.UserController", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class UserController:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/account.UserController/List",
            payment__module_dot_protos_dot_account__pb2.UserListRequest.SerializeToString,
            payment__module_dot_protos_dot_account__pb2.User.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.UserController/Create",
            payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            payment__module_dot_protos_dot_account__pb2.User.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Retrieve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.UserController/Retrieve",
            payment__module_dot_protos_dot_account__pb2.UserRetrieveRequest.SerializeToString,
            payment__module_dot_protos_dot_account__pb2.User.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.UserController/Update",
            payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            payment__module_dot_protos_dot_account__pb2.User.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Destroy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.UserController/Destroy",
            payment__module_dot_protos_dot_account__pb2.User.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
