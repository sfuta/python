# -*- coding: utf-8 -*-

import unittest
from lib.configure import Configure

class TestConfigure(unittest.TestCase):

    def setUp(self):
        path="../config/config.yml"
        self.configs = Configure.load_yaml(path)

    def test_get(self):
        """ test get
        """
        self.assertEqual("test value", Configure.get("test.a.b"))

if __name__=='__main__':
    unittest.main()
