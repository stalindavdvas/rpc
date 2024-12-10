# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import name_pb2 as name__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in name_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NameServiceStub(object):
    """Definimos el servicio NameService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetName = channel.unary_unary(
                '/NameService/GetName',
                request_serializer=name__pb2.Empty.SerializeToString,
                response_deserializer=name__pb2.Name.FromString,
                _registered_method=True)


class NameServiceServicer(object):
    """Definimos el servicio NameService
    """

    def GetName(self, request, context):
        """El método GetName no recibe ningún dato (Empty) y devuelve un mensaje Name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetName,
                    request_deserializer=name__pb2.Empty.FromString,
                    response_serializer=name__pb2.Name.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('NameService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NameService(object):
    """Definimos el servicio NameService
    """

    @staticmethod
    def GetName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NameService/GetName',
            name__pb2.Empty.SerializeToString,
            name__pb2.Name.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)