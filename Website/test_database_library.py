import unittest
import database_library


class TestDatabase_library(unittest.TestCase):

    def test_get_db(self):
        self.assertTrue(database_library.get_db)  
    
    def test_get_db_no_flask(self):
        self.assertTrue(database_library.get_db_no_flask)

    def test_query_db(self):
        self.assertTrue(database_library.query_db)
    
    def test_get_players(self):
        self.assertTrue(database_library.get_players)

    def test_get_testimonial(self):
        self.assertTrue(database_library.get_testimonial)

    def test_get_alumni(self):
	    self.assertTrue(database_library.get_alumni)
         
    def test_get_team_members(self):
         self.assertTrue(database_library.get_team_members)

    def test_get_about(self):
	    self.assertTrue(database_library.get_about)

    def test_get_pages(self):
        self.assertTrue(database_library.get_pages)


if __name__ == '__main__':
    unittest.main()