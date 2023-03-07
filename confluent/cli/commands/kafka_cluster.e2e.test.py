import unittest
from kafka_cluster import KafkaCluster
from confluent.cli.commands.login import login

kafka_cluster=KafkaCluster()

class KafkaClusterTest(unittest.TestCase):

  def setUp(self):
    login()

  def tearDown(self):
    print('tearDown')

  def test_list(self):
    login()
    header, data = kafka_cluster.list(parse=True)
    self.assertNotEqual(header, None)
    self.assertNotEqual(data, None)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
