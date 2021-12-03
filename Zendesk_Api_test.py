#DO NOT CHANGE ANY CODE IN THIS FILE
#YOU DO NOT HAVE TO SUBMIT THIS FILE. IT IS MEANT FOR TESTING OF YOUR CODE
import unittest
from zendesk_challenge import Zendesk_Api as ZZ

class TestCases(unittest.TestCase):
	def testcase1(self):
		zendesk_instance = ZZ()
		print("checking view all tickets call")
		self.assertEqual(zendesk_instance.Zendesk_ticket_app(),1)

	def testcase2(self):
		zendesk_instance = ZZ()
		print("checking view a specific ticket function")

		self.assertEqual(zendesk_instance.Zendesk_ticket_app(),1)

	def testcase3(self):
		zendesk_instance = ZZ()
		print("check quit functioning")
		print("select menu and then enter quit)"
		self.assertEqual(zendesk_instance.Zendesk_ticket_app(),0)


if __name__ == '__main__':
    unittest.main()