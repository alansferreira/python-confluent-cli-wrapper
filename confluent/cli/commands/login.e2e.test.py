import unittest

from confluent.cli.commands.login import login

class LoginTest(unittest.TestCase):

  def test_login_login(self):
    defaultLogin = login()
    self.assertNotEqual(defaultLogin, None)


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
