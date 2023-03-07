import unittest

from utils.parsers import parseAsciiTable

class ParsersTest(unittest.TestCase):

  def test_parseAsciiTable(self):
    

    asciiTable = '  Current |    ID     | Name  \n----------+-----------+-------\n          | env-62jx8 | hml   \n          | env-zx2ry | prd   \n  *       | env-ovwrp | dev   \n'
    header, data = parseAsciiTable(asciiTable)
    self.assertNotEqual(header, None)
    self.assertNotEqual(data, None)


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
