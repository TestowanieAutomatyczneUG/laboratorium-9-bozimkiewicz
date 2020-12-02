from src.Car import Car
from unittest.mock import *
from unittest import TestCase


class TestCar(TestCase):
    def setUp(self):
        self.temp = Car()

    def test_needs_fuel_true(self):
        # prepare mock
        self.temp.needsFuel = Mock(name='needs_fuel')
        self.temp.needsFuel.return_value = True

        # testing
        self.assertEqual(self.temp.needsFuel(), True, 'return value from needsFuel incorrect')

    def test_needs_fuel_false(self):
        # prepare mock
        self.temp.needsFuel = Mock(name='needs_fuel')
        self.temp.needsFuel.return_value = False

        # testing
        self.assertEqual(self.temp.needsFuel(), False, 'return value from needsFuel incorrect')

    def test_get_engine_temperature(self):
        self.temp.getEngineTemperature = Mock(name='get_engine_temperature')
        self.temp.getEngineTemperature.return_value = 30
        self.assertEqual(self.temp.getEngineTemperature(), 30, 'return value from getEngineTemperature incorrect')

    @patch.object(Car, 'driveTo')
    def test_drive_to(self, mock_method):
        destination = 'Gdynia'
        mock_method.return_value = 'Driving to ' + destination
        self.assertEqual(self.temp.driveTo(destination), mock_method.return_value, 'return value from driveTo incorrect')

    def tearDown(self):
        self.temp = None
