import unittest
from environment import Environment
from confluent.cli.commands.login import login
from utils.parsers import OutputEnum

environment=Environment()

class EnvironmentTest(unittest.TestCase):
  def setUp(self):
    login()

  def tearDown(self):
    print('tearDown')

  def test_list(self):
    header, data = environment.list(parse=True)
    self.assertNotEqual(header, None)
    self.assertNotEqual(data, None)

  def test_list_json(self):

    envs = environment.list(output=OutputEnum.json)
    self.assertNotEqual(envs, None)
    self.assertNotEqual(len(envs), 0)
    
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
