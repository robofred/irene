# coding=utf-8
from __future__ import absolute_import

import flask
import RPi.GPIO as GPIO
import time
# from rpi_ws281x import *
# import argparse

import octoprint.plugin

panPin = 12  # Pin# on RasPi to control Panning
tiltPin = 13 # Pin# on RasPi to control Tilting

fc = 0      # initial duty cycle


GPIO.setmode(GPIO.BCM)          # Pins are all BCM
GPIO.setup(panPin, GPIO.OUT)    # Setup Pan Pin
GPIO.setup(tiltPin, GPIO.OUT)   # Setup Tilt Pin

p = GPIO.PWM(panPin, 50)        # Set pan Freq at 50 Hz
t = GPIO.PWM(tiltPin, 50)       # Set tilt Freq at 50 Hz

p.start(fc)                     # Initialize Panning Pin
t.start(fc)                     # Initialize Tilting Pin

dBounce = 0.5                   # Pause for debounce (in Seconds)


class IrenePlugin(
    octoprint.plugin.StartupPlugin,
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SimpleApiPlugin,
):

    ##~~ SettingsPlugin mixin



    def get_settings_defaults(self):
        return {
            # put your plugin's default settings here
        }

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/irene.js"],
            "css": ["css/irene.css"]
        }



    #########################################################################################################################################################
    #########################################################################################################################################################

    def get_api_commands(self):
        return dict(
            servoDc=["servoCmd"],
            tiltDc=["tiltCmd"]
            )
        self._logger.error("K1K we are in get_api_command")



    def on_api_command(self, command, data):
        # self._logger.info("K2KIn on_api_comm: {}".format(self.servoCmd))
        if command == "servoDc":
            dc = float(data.get('servoCmd'))
            p.ChangeDutyCycle(dc)
            time.sleep(dBounce)
        elif command == "tiltDc":
            dc = float(data.get('tiltCmd'))
            t.ChangeDutyCycle(dc)
            time.sleep(dBounce)


        
    
    # def on_api_command(self, command, data):
    #     dc = float(data.get('tiltCmd'))
    #     t.ChangeDutyCycle(dc)
    #     time.sleep(dBounce)
    



    ##########################################################################################################################################################

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "irene": {
                "displayName": "Irene Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "you",
                "repo": "OctoPrint-Irene",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/you/OctoPrint-Irene/archive/{target_version}.zip",
            }
        }

# def fClean():
#     for i in range(strip.numPixels()):
#     strip.setPixelColor(i, Color(0, 0, 0))
#     strip.show()
#     return




__plugin_name__ = "Irene Plugin"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = IrenePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
