from ...domain.broker_object import BrokerObject

class RabbitmqExchange(BrokerObject):
    def __init__(self,
                 channel,
                 name:str,
                 exchange_type:str,
                 durable:bool):
        self.name = name
        self.channel = channel
        self.exchange_type = exchange_type
        self.durable = durable

    def create(self)-> bool:
        try:
            self.channel.exchange_declare(exchange= self.name,
                                        exchange_type= self.exchange_type,
                                        durable= self.durable)
            return True
        except Exception as e:
            raise e
        