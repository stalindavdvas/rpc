import grpc
from concurrent import futures
import name_pb2
import name_pb2_grpc

class NameService(name_pb2_grpc.NameServiceServicer):
    def GetName(self, request, context):
        return name_pb2.Name(name="Stalin Vasco")  # Aquí pones tu nombre

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    name_pb2_grpc.add_NameServiceServicer_to_server(NameService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC corriendo en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
