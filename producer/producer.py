
import sys
from random import Random


class Producer():

    def produce_msgs(self,ran):
        #price_field = random.randint(800,1400)
        random = Random(ran)
        msg_cnt = 0
        start = 50
        for i in range(1): #for observation groups 13 through 13+range
            #time.sleep(10) #waits between observation groups
            for x in range(1): #1500 means about 1000 per obs because there are 4 producers
              #  time.sleep(4) # 0.2 waits this many seconds before producing another message about 1000 each obs each 5  min
                self.observationgroup_field = random.randint(start+i,start+i);
                self.observationorder_field = random.randint(1,6)
                self.frequency_field = random.random()*10000
                self.snr_field = random.random()*100
                self.driftrate_field = random.random()-random.random()
                self.uncorrectedfrequency_field = random.random()-random.random()+self.frequency_field
               # str_fmt = "{};{};{};{};{};{};{}"

                msg_cnt += 1
                


