# -*- coding: utf-8 -*-
"""
Created on Sun June 25 11:41:03 2017

@author: shortcut team

function velocity_journey_point finds the incentive for the driver based on 
the current velocity. Driver gets .1 for good driving (velocity <= 100) and -.2 for bad 
driving (veocity > 100).  
"""

def velocity_journey_point(velocity):
    
    if velocity <= 100:
        return 0.1
    else:
        return -0.2
