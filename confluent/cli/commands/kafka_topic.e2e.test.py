import unittest
from kafka_cluster import KafkaCluster
from environment import Environment
from kafka_topic import KafkaTopic
from utils.parsers import OutputEnum
from confluent.cli.commands.login import login


environment=Environment()
kafka_cluster=KafkaCluster()
kafka_topic=KafkaTopic()

class KafkaTopicTest(unittest.TestCase):
  e_header, e_data = [None, None]
  c_header, c_data = [None, None]
  env = None
  cluster = None
  
  def setUp(self):
    login()
    
    e_header, e_data = environment.list(parse=True)
    self.env = e_data[2][1]
    
    c_header, c_data = kafka_cluster.list(parse=True, env=self.env)
    self.cluster=c_data[0][1]

  def tearDown(self):
      print('tearDown')
      

  def test_00_list(self):
    
    self.topics = kafka_topic.list(parse=True, env=self.env, cluster=self.cluster, output=OutputEnum.json)
    self.assertNotEqual(self.topics, None)
    self.assertNotEqual(len(self.topics), 0)

  def test_01_describe(self):
    
    self.topic = kafka_topic.describe(parse=True, topic=self.topics[0]['name'], env=self.env, cluster=self.cluster, output=OutputEnum.json)
    self.assertNotEqual(self.topic, None)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
