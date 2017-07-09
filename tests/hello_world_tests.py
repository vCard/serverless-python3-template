from lib.hello import HelloService
import unittest

class HelloWorldTests(unittest.TestCase):


    def test_hello_returns_world(self):
        result = HelloService.hello()
        self.assertTrue(result == "world")

if __name__ == '__main__':
    unittest.main()

