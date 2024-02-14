import os
import sys
import time

from broker.infraestructure.rabbitmq.rabbitmq_init import (rabbit_mq,
                                                           channel,
                                                           exchange_user_event)
def main():
    rabbit_mq_connection = rabbit_mq.connect()
    
    channel = rabbit_mq_connection.channel()
    
    message = "main_producer registered"

    channel.basic_publish(exchange=exchange_user_event.name,
                          routing_key='user.register', 
                          body=message
                          )

    print(f"Sent message:{message}")

    rabbit_mq_connection.close()

if __name__ == "__main__":
    try:
        time.sleep (8)
        count = 0
        main()


    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)