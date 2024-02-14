
from dotenv import load_dotenv
import os
import sys

from ...application.broker_connector import BrokerConnection
from .rabbitmq_connection import RabbitmqConnection
from .rabbitmq_exchange import RabbitmqExchange
from .rabbitmq_queue import RabbitmqQueue
from .rabbitmq_binding import RabbitmqBinding


load_dotenv()
    
rabbit_mq = RabbitmqConnection(
                    os.environ.get("RABBITMQ_HOST"),
                    os.environ.get("RABBITMQ_PORT"),
                    os.environ.get("RABBITMQ_DEFAULT_USER"),
                    os.environ.get("RABBITMQ_DEFAULT_PASS")
)

rabbit_mq_connection = BrokerConnection.get_connection(rabbit_mq)

channel = rabbit_mq_connection.channel()

exchange_user_event = RabbitmqExchange(channel,
                            'user_event',
                            'topic',
                            True
                        )
exchange_user_event.create()

queue_user = RabbitmqQueue(channel,
                           'user',
                           True
                           )

queue_user.create()

binding_user = RabbitmqBinding(channel,
                               queue_user.name,
                               exchange_user_event.name,
                               'user.*')
binding_user.create()