import unittest
from unittest.mock import patch
import server



class TestServer(unittest.TestCase):
   
    def test_user_loader(self):
        self.assertEqual(server.user_loader('johndoe'),None)
        self.assertTrue(server.user_loader('foo@bar.tld'))
    

    def test_unauthorized_handler(self):
        self.assertEqual(server.unauthorized_handler(),'Unauthorized')

    def test_welcome(self):
        self.assertTrue(server.welcome)

    def test_donate(self):
        self.assertTrue(server.donate)

    def test_members(self):
        self.assertTrue(server.members)

    def test_alumni(self):
        self.assertTrue(server.alumni)

    def test_calendar(self):
        self.assertTrue(server.calendar)

    def test_instagram(self):
        self.assertTrue(server.instagram)
    
    def test_about(self):
        self.assertTrue(server.about)

    def test_join(self):
        self.assertTrue(server.join)

    def test_contact(self):
        self.assertTrue(server.contact)

    def test_contact_post(self):
        self.assertTrue(server.contact_post)

    def test_recruitment(self):
        self.assertTrue(server.recruitment)

    def test_login(self):
        self.assertTrue(server.login)

    def test_login_otp(self):
        self.assertTrue(server.login_otp)
                        
if __name__ == '__main__':
    unittest.main()