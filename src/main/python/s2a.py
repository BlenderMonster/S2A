'''
The Sensor-To-Actuator library
==============================

This module provides functions to transfer results from sensors
to actuators, sets position or aligns to a vector
'''
__version__ = "2.0"
__author__ = "Monster"

import mbge
import mutil

def hitObjectToObject():
    hitObjects = mutil.sensors.hitObjects
    hitObject = min(hitObjects, key=lambda object: object.getDistanceTo(mbge.context.owner))

    for actuator in mbge.context.controller.actuators:
        try:
            actuator.object = hitObject
        except AttributeError:
            pass


def hitPositionToPosition():
    hitObjects = mutil.sensors.hitObjects
    hitObject = min(hitObjects, key=lambda object: object.getDistanceTo(mbge.context.owner))
    if not hitObject:
        return

    for actuator in mbge.context.controller.actuators:
        actuator.owner.worldPosition = hitObject.position

