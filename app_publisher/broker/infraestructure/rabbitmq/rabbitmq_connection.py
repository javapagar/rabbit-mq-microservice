import pika
from ...domain.broker_connection import Connection

class RabbitmqConnection(Connection):
    
    def __init__(self, host, port,user,pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.connection = None

    def connect(self):
        if not self.connection or self.connection.is_closed:
        
            print(f"Connecting to {self.host}:{self.port}")
            credentials = pika.PlainCredentials(
                                            self.user, 
                                            self.pwd
                                            )
            
            connection_params = pika.ConnectionParameters(
                                            self.host,
                                            self.port,
                                            credentials=credentials
                                            )

            self.connection = pika.BlockingConnection(connection_params)
        
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed")