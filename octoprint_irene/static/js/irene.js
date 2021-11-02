/*
 * View model for OctoPrint-Irene
 *
 * Author: robofred
 * License: AGPLv3
 */
$(function() {
    function IreneViewModel(parameters) {
        var self = this;
        var cLocation = 6;          
        var sLocation = 6;          
        var sMin = 2;               
        var sMax = 12;   
        var sMove = 1;    
        var zLocation = 6;       
        var tLocation = 6;
        var zMin = 2;
        var zMax = 12;
        var zMove = 1;
        self.servoDc = ko.observable(6);
        self.servoLeft = ko.observable(2);
        self.servoRight = ko.observable(12);
        self.servoCenter = ko.observable(6);
        self.tiltLeft = ko.observable(2);
        self.tiltCenter = ko.observable(6);
        self.tiltRight = ko.observable(12);


        self.sUp = function() {
            if (zLocation > zMin) {
                zLocation = zLocation - zMove;
            } else {
                zLocation = zMin;
            }
            console.log('Tilting servo to: ' + zLocation);
            OctoPrint.simpleApiCommand("irene", "tiltDc", {tiltCmd: zLocation});
        }


        self.tiltCenter = function() {
            zLocation = tLocation
            console.log('Moving servo to: ' + sLocation);
            OctoPrint.simpleApiCommand("irene", "tiltDc", {tiltCmd: zLocation});
        }


        self.sDown = function() {
            if (zLocation < zMax) {
                zLocation = zLocation + zMove;
            } else {
                zLocation = zMax;
            }
            console.log('Tilting servo to: ' + zLocation);
            OctoPrint.simpleApiCommand("irene", "tiltDc", {tiltCmd: zLocation});
        }





        self.sRight = function() {
            if (sLocation > sMin) {
                sLocation = sLocation - sMove;
            } else {
                sLocation = sMin;
            }
            console.log('Moving servo to: ' + sLocation);
            OctoPrint.simpleApiCommand("irene", "servoDc", {servoCmd: sLocation});
        }

        self.sCenter = function() {
            sLocation = cLocation
            console.log('Moving servo to: ' + sLocation);
            OctoPrint.simpleApiCommand("irene", "servoDc", {servoCmd: sLocation});
        }


        self.sLeft = function() {
            if (sLocation < sMax) {
                sLocation = sLocation + sMove;
            } else {
                sLocation = sMax;
            }
            console.log('Moving servo to: ' + sLocation);
            OctoPrint.simpleApiCommand("irene", "servoDc", {servoCmd: sLocation});
        }







    }

    OCTOPRINT_VIEWMODELS.push({
        construct: IreneViewModel,
        dependencies: [],
        elements: [ "#sidebar_plugin_irene" ]
    });
});