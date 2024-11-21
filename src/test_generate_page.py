import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")
    
    def test_extract_middle_title(self):
        title = extract_title("## This isn't the title\n# This is the title ")
        self.assertEqual(title, "This is the title")

if __name__ == "__main__":
    unittest.main()
