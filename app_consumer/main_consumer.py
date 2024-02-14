import os
import sys

from broker.infraestructure.rabbitmq.rabbitmq_init import (channel,queue_user)

def callback(ch, method, properties, body):
    print(f"Received {body}")

def main():   
   
    channel.basic_consume(
        queue= queue_user.name,
        auto_ack=True,
        on_message_callback= callback
    )

    print("Waiting for messages...")

    channel.start_consuming()

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
