from codecamp_3 import Data
import unittest
import unittest
from unittest.mock import Mock
import codecamp3main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Obj = Mock(
            Data("https://en.wikipedia.org/w/api.php?format=json&action=query&titles=SMALL&prop=revisions&rvprop=content"))

    def test_Validation(self):
        x = self.Obj.urlvalidation()
        self.assertTrue(x)

    def test_PageId(self):
        x = self.Obj.get_pageid()
        self.assertNotEqual(1808130,x)
        
    def test_SeeAlso(self):
        x = self.Obj.getSeeAlso()
        self.assertTrue(x)
    
    def test_generate_links(self):
        x = self.Obj.generate_links()
        self.assertTrue(x)



    
if __name__=='__main__':
    unittest.main()
