from kafka import KafkaProducer
from json import dumps
from . import consumer
from fastapi import HTTPException,status

def send_one(data):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("topic sending")
    producer.send('mytopic1',dumps(data).encode('utf-8'))
    print("topic sent")
    producer.flush()
    print("topic flushed")
    producer.close()
    print("topic closed")
        # return {"Error":HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT)}
    
    



