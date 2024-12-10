import grpc
import name_pb2
import name_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = name_pb2_grpc.NameServiceStub(channel)
        response = stub.GetName(name_pb2.Empty())
        print("Nombre recibido: " + response.name)

if __name__ == '__main__':
    run()
