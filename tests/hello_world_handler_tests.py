from handlers import handler
from lambda_local import context
from lambda_local import event
import unittest
import os

event_content = os.path.join(os.path.dirname(__file__), 'event.json')
c = context.Context(10, "local", "local")
e = event.read_event(event_content)

class HandlerTests(unittest.TestCase):

    def test_hello_handlers(self):

        response = handler.handler(e, c)
        print(repr(response.get("body")))
        self.assertTrue(response.get("statusCode") == 200)
        self.assertTrue(response.get("body") == '"hello world"')

if __name__ == '__main__':
    unittest.main()

