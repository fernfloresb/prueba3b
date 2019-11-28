from django.test import TestCase

class testclase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: run once to set up non-modified data dor all class methods.")
        pass

    def setUp(self):
        print("setUp: run one for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1 ,2)  