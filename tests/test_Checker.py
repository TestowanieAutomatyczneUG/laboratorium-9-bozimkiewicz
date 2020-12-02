from src.Checker import Checker
from unittest.mock import *
import unittest


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.temp = Checker()

    def test_checker_played_after_17(self):
        file = 'file.wav'
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.getTime.return_value = 18
        self.temp.env.wavWasPlayed = Mock(name='wavWasPlayed')
        self.temp.env.wavWasPlayed.return_value = True
        self.assertEqual(self.temp.env.wavWasPlayed(file), True)

    def test_checker_not_played_before_17(self):
        file = 'file.wav'
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.getTime.return_value = 16
        self.temp.env.wavWasPlayed = Mock(name='wavWasPlayed')
        self.temp.env.wavWasPlayed.return_value = False
        self.assertEqual(self.temp.env.wavWasPlayed(file), False)

    def tearDown(self):
        self.temp = None
