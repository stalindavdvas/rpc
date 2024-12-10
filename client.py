from flask import Flask, render_template
import grpc
import name_pb2
import name_pb2_grpc

app = Flask(__name__)

# Cliente gRPC que obtiene el nombre desde el servidor gRPC
def get_name_from_grpc():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = name_pb2_grpc.NameServiceStub(channel)
        response = stub.GetName(name_pb2.Empty())
        return response.name

@app.route('/')
def index():
    # Obtiene el nombre desde el servidor gRPC
    name = get_name_from_grpc()
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
