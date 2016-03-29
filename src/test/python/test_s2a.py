__author__ = 'Monster'

from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, MagicMock, call;
import sys

__author__ = 'Monster'


class TestS2A(TestCase):

    def test_hitObjectToObject(self):
        bge = Mock()
        mbge = Mock()
        mutil = Mock()

        class Actuator():
            def __init__(self):
                self.object = None

        closest = Mock()
        closest.getDistanceTo = Mock(return_value=1.0)
        next = Mock()
        next.getDistanceTo = Mock(return_value=2.0)
        mutil.sensors.hitObjects = [next, closest]

        actuatorWithObject = Actuator()
        actuatorWithoutObject = Mock(spec_set=[])
        controller = Mock()
        mbge.context.controller.actuators = [actuatorWithObject, actuatorWithoutObject]
        with patch.dict('sys.modules', {'mutil': mutil, 'mbge': mbge}):

            import s2a
            s2a.hitObjectToObject()

        self.assertEqual(actuatorWithObject.object, closest)