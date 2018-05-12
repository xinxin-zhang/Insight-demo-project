#!/usr/bin/python2
import sys
from random import Random
import unittest
#import os
#sys.path.append(os.environ['WORKSPACE'])
#from kafka.client import Simpleclient 
import kafka_producer


class ProducerTest(unittest.TestCase):

    def setUp(self):
        global random
        random = Random(0)


    def test_observation(self):
        p = kafka_producer.Producer()
        p.produce_msgs(0)
        self.assertEqual(p.observationgroup_field, 50)
        self.assertEqual(p.observationorder_field, 5)
        self.assertEqual(p.frequency_field, 4205.71580830845)
        self.assertEqual(p.snr_field, 25.891675029296334)
        self.assertEqual(p.driftrate_field, 0.10634058391819423)
        self.assertEqual(p.uncorrectedfrequency_field, 4206.1962941714055)


if __name__ == "__main__":
    unittest.main()

