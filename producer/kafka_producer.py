import random
from random import Random
import sys
import time
import six
#from datetime import datetime
from kafka.client import SimpleClient
from kafka.producer import KeyedProducer

class Producer(object):

    def __init__(self, addr=None):
        self.isNone = True
        if addr is not None:
            self.client = SimpleClient(addr)
            self.producer = KeyedProducer(self.client)
            self.isNone = False

    def produce_msgs(self, source_symbol):
        random = Random(0);
        msg_cnt = 0
        start = 50
        for i in range(1000): #for observation groups 13 through 13+range
            #time.sleep(10) #waits between observation groups
            for x in range(300): #1500 means about 1000 per obs because there are 4 producers
                time.sleep(0.00001) # 0.2 waits this many seconds before producing another message about 1000 each obs each 5  min
                self.observationgroup_field = random.randint(start+i,start+i);
                self.observationorder_field = random.randint(1,6) 
                self.frequency_field = random.random()*10000
                self.snr_field = random.random()*100
                self.driftrate_field = random.random()-random.random()
                self.uncorrectedfrequency_field = random.random()-random.random()+self.frequency_field
                str_fmt = "{};{};{};{};{};{};{}"
                message_info = str_fmt.format(source_symbol,
                                              self.observationgroup_field,
                                              self.observationorder_field,
                                              self.frequency_field,
                                              self.snr_field,
                                              self.driftrate_field,
                                              self.uncorrectedfrequency_field)
                if not self.isNone:
                    self.producer.send_messages('gbthits', source_symbol, message_info)
                else:
                    break
                msg_cnt += 1
            if self.isNone:
                break 

if __name__ == "__main__":
    args = sys.argv
    ip_addr = str(args[1])
    partition_key = str(args[2])
    prod = Producer(ip_addr)
    prod.produce_msgs(partition_key) 
