"""
@author: da2el
@title: D2 Steps
@description: Calculate the steps for the refiner
"""

from .D2_RefinerSteps import D2_RefinerSteps
from .D2_RefinerStepsA1111 import D2_RefinerStepsA1111
from .D2_RefinerStepsTester import D2_RefinerStepsTester

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
  "D2 Refiner Steps": D2_RefinerSteps,
  "D2 Refiner Steps A1111": D2_RefinerStepsA1111,
  "D2 Refiner Steps Tester": D2_RefinerStepsTester,
}

NODE_DISPLAY_NAME_MAPPINGS = {
  "D2 Refiner Steps": "D2 Refiner Steps",
  "D2 Refiner Steps A1111": "D2 Refiner Steps A1111",
  "D2 Refiner Steps Tester": "D2 Refiner Steps Tester",
}

print("D2 steps init.py")
print(WEB_DIRECTORY)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]