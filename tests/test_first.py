import unittest


class FirstTestCase(unittest.TestCase):
    def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")
