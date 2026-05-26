from abc import ABC, abstractmethod

# --- 1. THE PRODUCT BLUEPRINT ---
class MinecraftServer(ABC):
    @abstractmethod
    def start(self):
        pass

class OneBlockServer(MinecraftServer):
    def start(self):
        print("Starting One Block Map Server...")

class ShaderServer(MinecraftServer):
    def start(self):
        print("Starting High-Performance Shader Server...")

class VanillaServer(MinecraftServer):
    def start(self):
        print("Starting Vanilla Survival Server...")

# --- 3. THE FACTORY (The Manufacturer) ---
# This class has ONE job: build and return the correct server object.
class ServerFactory:
    def create_server(self, server_type: str) -> MinecraftServer:
        if server_type == "OneBlock":
            return OneBlockServer()
        elif server_type == "Shaders":
            return ShaderServer()
        elif server_type == "Vanilla":
            return VanillaServer()
        else:
            raise ValueError("Unknown Server")
    
class ServerSpawner:
    def __init__(self, factory: ServerFactory):
        self.factory = factory

    def launch(self, server_type: str):
        print(f"\n--- Initializing Backend Provisioning for {server_type} ---")
        server = self.factory.create_server(server_type)
        
        server.start()
my_factory = ServerFactory()
my_spawner = ServerSpawner(my_factory)

my_spawner.launch("OneBlock")
my_spawner.launch("Vanilla")