# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 11:38:36 2017

@author: 

The function calculates the incentives of 2 drivers. 
"""

import velocity_incentive_calculation as incentive_1 # user defined function
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2 
import math
import operator

def main_function():
    
    df_a = pd.read_csv('./datasets/illinois/driver_a.csv')
    df_b = pd.read_csv('./datasets/illinois/driver_b.csv')
    cv2.namedWindow('Driver A')
    cv2.namedWindow('Driver B')
    loop_exit = min (len(df_a['LOCATION Speed ( Kmh)']), len(df_b['LOCATION Speed ( Kmh)']))
    iterator_a = 0
    iterator_b = 0
    flip_coins_initial_a = 49.5
    flip_coins_initial_b = 49.6
    journey_point_a = 0
    journey_point_b = 0
    velocity_a = []
    velocity_b = []
    
    plt.ioff()
    
    total_rank = {'driver d' : 76,
                  'driver z' : 73,
                  'driver a': 49.5, 
                  'driver b': 50}
    j = 0
    while (j <= loop_exit):
        
        cv2.waitKey(50)
        j += 1
        
        ## Incentive Calculation ###
        time_a = df_a['YYYY-MO-DD HH-MI-SS_SSS'][iterator_a]
        velocity = df_a['LOCATION Speed ( Kmh)'][iterator_a]
        if math.isnan(velocity):
            velocity = 0
#        print 'type', type(velocity)
        velocity_a.append(velocity) 
#        print 'vel', velocity_a
        time_axis_a = np.arange(iterator_a + 1) * 10
        journey_point_a += incentive_1.velocity_journey_point(velocity)
        flip_coins_a = flip_coins_initial_a + journey_point_a / 100.0
        iterator_a += 1
        
        time_b = df_b['YYYY-MO-DD HH-MI-SS_SSS'][iterator_b]
        velocity = df_b['LOCATION Speed ( Kmh)'][iterator_b]
        velocity_b.append(velocity)
        time_axis_b = np.arange(iterator_b + 1) * 10
        journey_point_b += incentive_1.velocity_journey_point(velocity)
        flip_coins_b = flip_coins_initial_b + journey_point_b / 100.0
        iterator_b += 1

        ## to draw graph of driver A ##
        fig_a = plt.figure()
        plt.xlabel('time (seconds)')
        plt.ylabel('velocity (km/hr)')
        plt.title('Velocity Graph')
        plt.ylim([0, 200])
        if iterator_a % 100 == 0:
            plt.xlim([0, 1000])
        else:
            plt.xlim([0, ((iterator_a / 100) +1) * 1000])
        plt.plot(time_axis_a, velocity_a)
        plt.axhline(y=100)
        fig_a.canvas.draw()
        # Now we can save it to a numpy array.
        data_a = np.fromstring(fig_a.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data_a = data_a.reshape(fig_a.canvas.get_width_height()[::-1] + (3,))
#        print data_a.shape  # 320, 480   160,300
        data_a = cv2.resize(data_a, (300, 160))
        
        ## to draw graph of driver B ##
        fig_b = plt.figure()
        plt.xlabel('time (seconds)')
        plt.ylabel('velocity (km/hr)')
        plt.title('Velocity Graph')
        plt.xlim([0, 1000])
        plt.ylim([0, 200])
        if iterator_b % 100 == 0:
            plt.xlim([0, 1000])
        else:
            plt.xlim([0, ((iterator_b / 100) +1) * 1000])
        plt.plot(time_axis_b, velocity_b)
        plt.axhline(y=100)
        fig_b.canvas.draw()
        # Now we can save it to a numpy array.
        data_b = np.fromstring(fig_b.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data_b = data_b.reshape(fig_b.canvas.get_width_height()[::-1] + (3,))
        data_b = cv2.resize(data_b, (300, 160))
        
        
        ### GUI part ###
        driver_a = np.ones((672, 378, 3), dtype = np.uint8) * 255 # 960, 540
        cv2.putText(driver_a, 'Driver A', (18, 26), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        cv2.putText(driver_a, str(time_a), (150, 26), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
        cv2.line(driver_a, (0, 50), (377, 50), (0, 255, 255), 2)
        cv2.line(driver_a, (112, 0), (112, 50), (0, 0, 255), 2)
        cv2.putText(driver_a, 'Flip Coins : ' + str(flip_coins_a), (95, 190), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255))
        cv2.putText(driver_a, 'Journey Points : ' + str(journey_point_a), (95, 228), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
        driver_a[270:270+160, 10:10+300, :] = data_a
        k = 0
        total_rank['driver a'] = flip_coins_a
        cv2.putText(driver_a, 'NAME' + '   ' + 'RANK FlipCoins', (180, 65), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0))
        
        for key in sorted(total_rank.items(), key=operator.itemgetter(1), reverse = True):
            k += 1
            cv2.putText(driver_a, key[0] + '  ' + str(k) + '   ' + str(key[1]), (180, 65 + 20*k), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0))
            if key[0] == 'driver a':
                rank = k
        cv2.putText(driver_a, 'RANK : ' + str(rank), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0))  
        cv2.imshow('Driver A', driver_a)
        
        driver_b = np.ones((672, 378, 3), dtype = np.uint8) * 255 # 960, 540
        cv2.putText(driver_b, 'Driver B', (18, 26), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        cv2.putText(driver_b, str(time_b), (150, 26), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
        cv2.line(driver_b, (0, 50), (377, 50), (0, 255, 255), 2)
        cv2.line(driver_b, (112, 0), (112, 50), (0, 0, 255), 2)
        cv2.putText(driver_b, 'Flip Coins : ' + str(flip_coins_b), (95, 190), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255))
        cv2.putText(driver_b, 'Journey Points : ' + str(journey_point_b), (95, 228), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
        driver_b[270:270+160, 10:10+300, :] = data_b
        k = 0
        total_rank['driver b'] = flip_coins_b
        cv2.putText(driver_b, 'NAME' + '   ' + 'RANK FlipCoins', (180, 65), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0))
        for key in sorted(total_rank.items(), key=operator.itemgetter(1), reverse = True):
            k += 1
            cv2.putText(driver_b, key[0] + '  ' + str(k) + '   ' + str(key[1]), (180, 65 + 20*k), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0))
            if key[0] == 'driver b':
                rank = k
        cv2.putText(driver_b, 'RANK : ' + str(rank), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0))        
        cv2.imshow('Driver B', driver_b)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main_function()
