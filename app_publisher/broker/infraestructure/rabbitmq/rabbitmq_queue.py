from ...domain.broker_object import BrokerObject

class RabbitmqQueue(BrokerObject):

    def __init__(self,
                 channel,
                 name:str,
                 durable:bool):
        self.name = name
        self.channel = channel
        self.durable = durable
        self.bindings = []

    def create(self)-> bool:
        try:
            self.channel.queue_declare(queue=self.name,
                                        durable=self.durable)
            return True
        except Exception as e:
            raise e
