from unittest import TestCase
from io import StringIO
import sys
from main import hello_world

class TestMain(TestCase):
    def test_hello_world(self):
        captured_output = StringIO()  # Create a buffer the console slayer
        sys.stdout = captured_output  # capture output to buffer, the console slayer

        hello_world()  # call function

        sys.stdout = sys.__stdout__  # reverse back to standard
        self.assertEqual(captured_output.getvalue().strip(), "Hello World")  # check if catched Output is equal