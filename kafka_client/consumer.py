from kafka import KafkaConsumer
from database import db
from json import loads
import time

#import threading
class Callconsumer:
    dats = {}
    def __init__(self):
         print("consumer constructor called")
    def consumerhere(self):                             
        consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                                 group_id=None,
                                 value_deserializer=lambda x:loads(x.decode('utf-8')),
                                 auto_offset_reset = 'latest')
        consumer.subscribe(['mytopic1'])
        # print(f"subscribed to--> {consumer.subscription()}")
        current = time.time()
        for msg in consumer:
            current2 = time.time()
            if(current+current2 > 1000):
                break
            self.dats= msg.value
            print(msg.value)
           
    print(dats)
    async def data_adding(self):
            await db.add_content(self.dats)
        



