from ...domain.broker_object import BrokerObject

class RabbitmqBinding(BrokerObject):

    def __init__(self,
                 channel,
                 queue:str,
                 exchange:str,
                 routing_key:str):
        self.queue = queue
        self.channel = channel
        self.exchange = exchange
        self.routing_key = routing_key

    def create(self)-> bool:
        try:
            self.channel.queue_bind(queue = self.queue,
                       exchange = self.exchange,
                       routing_key=self.routing_key)
            return True
        except Exception as e:
            raise e
