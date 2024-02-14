from ..domain.broker_connection import Connection


class BrokerConnection:
    @staticmethod
    def get_connection(connection:Connection):
        return connection.connect()