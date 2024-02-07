from kafka import KafkaConsumer
from json import loads
class mainconsumer:
    data = {}
    def ret(self):	
        consumer = KafkaConsumer('mytopic1',bootstrap_servers=['localhost:9092'],
                                 group_id=None,value_deserializer=lambda x:loads(x.decode('utf-8')))
        msg = 0
        for i in consumer:
            msg+=1
            self.data = i.value
            if msg==1:
                 break
        print(self.data)
        return self.data
def caller(dats):
    dats.update(mainconsumer().data)
    print("---inside--function--")
    print(dats)
    
if __name__ == "__main__":
    data =  mainconsumer().ret()
    
