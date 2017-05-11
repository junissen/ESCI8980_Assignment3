#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:06:41 2017

@author: julianissen

rayleigh_temp_model and rayleigh_source_model classes and accompanying functions
create and plot Rayleigh fractionation models using either variable temperature or 
variable moisture source values. 

Created 05/2017 by Julia Nissen
"""

import rayleigh_frac
import numpy as np


class rayleigh_temp_model():
    
    """
    Class to calculate changes in d18O condensate and fraction remaining resulting from varying temperatures.
    """
    
    def __init__(self, d_source_gen, dT, T_start, T_end, T_gen, dl_avg, ax, print_dv, limits):
        
        self.d_source_gen = d_source_gen
        self.dT = dT
        self.T_start = T_start
        self.T_end = T_end
        self.dl_avg = dl_avg
        self.T_source = T_gen 
        self.fract_GoM_start = 1.0
        self.fract_GoM_end = 0.0
        self.dfract = 0.05
        self.ax = ax
        
        if str(print_dv.lower()) == "y":
            self.print_dv = True
        else: self.print_dv = False
        
        if str(limits) == "full":
            self.x_lim = [1.0, 0.0] 
            self.y_lim = [-70, 4.0] 
        elif str(limits) == "half":
            self.x_lim = [0.5, 0.3] 
            self.y_lim = [-25, 0.0] 
        
        
    def temp_model(self):
        """
        Function changes the temperature, while keeping a constant moisture source 
        and altering the fraction of moisture remaining.

        """
        
        T = self.T_start
        
        while T >= self.T_end:
            
            alpha_evap = np.exp((1.137*((10**3)/(T**2))) - (0.4156/T) -(2.0667*(10**-3))) #from Majoube 1971, 
            
            dv_i = self.d_source_gen - ((10**3)*np.log(alpha_evap)) #from Rohling 2013
            
            alpha_precip = np.exp((-7.685 + 6.7123*((10**3)/T) - 1.6664*((10**6)/(T**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(T**3)))/1000)
            
            wb = rayleigh_frac.F_function(dv_i, alpha_precip, self.ax, self.x_lim, self.y_lim)
            
            if self.print_dv == True:
                wb.dv_function()
            
            wb.dl_function() 
            
            if self.print_dv == True:
            
                if T == self.T_start:
                    print "GENERAL SOURCE RAYLEIGH MODEL"
                    print "Highest Temperature Run: " + str(self.T_start - 273.15) + u"\u00b0" + "C"
                    print u"\u03b4" + "18Ov_i : " + str(wb.dv_function_print()) 
                    print u"\u03b4" + "18Ol_i : " + str(wb.dl_function_print()) 
                    print "Fractionation difference " + u"\u03b4" + "18O: " + str(wb.dv_function_print() - wb.dl_function_print())
             
                if T == self.T_end:
                    print "Lowest Temperature Run: " + str(self.T_end - 273.15) + u"\u00b0" + "C"
                    print u"\u03b4" + "18Ov_i : " + str(wb.dv_function_print()) 
                    print u"\u03b4" + "18Ol_i : " + str(wb.dl_function_print()) 
                    print "Fractionation difference in " + u"\u03b4" + "18O: " + str(wb.dv_function_print() - wb.dl_function_print())
             
            if T == self.T_source: #plots the rayleigh fractionion curve for condensate in Minneapolis, using the average yearly temperature
                F = 1.0
                dl_array = []
                F_array = []
                dF = 0.0001
                while F > 0.0:
                    dv = ((dv_i + 1000)*(F**(alpha_precip-1))) - 1000
                    dl = (alpha_precip*(dv + 1000)) - 1000
                    dl_array.append(dl)
                    F_array.append(F)
                    F = F - dF
                self.ax.set_xlim( self.x_lim )
                self.ax.set_ylim( self.y_lim )
                self.ax.plot(F_array, dl_array, '#6495ED', linewidth = 4, label = 'MN condensate')
            
            T = T - self.dT
            
    def temp_source_print(self):
        """
        Function calculates the fraction of moisture remaining to result in a condensate having the average yearly
        isotopic composition of Minneapolis moisture and at the average yearly temperature. Function calculates 
        for different moisture source compositions. 
        """
        
        T = self.T_source
        
        dl_avg = self.dl_avg
        
        alpha_evap = np.exp((1.137*((10**3)/(T**2))) - (0.4156/T) -(2.0667*(10**-3))) #from Majoube 1971, 
            
        dv_i = self.d_source_gen - ((10**3)*np.log(alpha_evap)) #from Rohling 2013
        
        alpha_precip = np.exp((-7.685 + 6.7123*((10**3)/T) - 1.6664*((10**6)/(T**2)) #from Dansgaard 1964, assuming constant alpha
                        + 0.35041*((10**9)/(T**3)))/1000)
        
        wb = rayleigh_frac.F_function_find(dv_i, alpha_precip, dl_avg, self.ax)
        wb.F_function_plot()
        if self.d_source_gen == 0.0:
            print "GENERAL SOURCE MODEL"
        elif self.d_source_gen > 0.0:
            print "GULF OF MEXICO SOURCE MODEL"
        elif self.d_source_gen < 0.0:
            print "PACIFIC SOURCE MODEL"
        print "Fraction remaining in MN (avg d18O, avg T) with source " + str(self.d_source_gen) + " : " + str(wb.F_function_find())


class rayleigh_source_model():
    """
    Class to calculate changes in d18O condensate and temperature resulting from variable varying source composition.
    """

    def __init__(self, fract_rem, d_source_GoM, d_source_Pac, dT, T_start, T_end, T_gen, dl_gen, ax, limits):
        
        self.F = fract_rem
        self.GoM = d_source_GoM
        self.Pac = d_source_Pac
        self.dT = dT
        self.T_start = T_start
        self.T_end = T_end
        self.T_gen = T_gen
        self.dl_gen = dl_gen
        self.ax = ax
        self.fract_GoM_start = 1.0
        self.fract_GoM_end = 0.0
        self.dfract = 0.1
        
        if limits == "source":
            self.x_lim = [self.T_end, self.T_start]
            self.y_lim = [-13.0, -9.0]
        
    def source_model(self):
        """
        Function changes the fraction of Gulf of Mexico and Pacific signatures in the original moisture source, while 
        keeping a constant fraction remaining and altering the temperature instead.

        """
        
        fract_GoM = self.fract_GoM_start
        
        while fract_GoM >= self.fract_GoM_end:
            
            fract_Pac = 1.0 - fract_GoM
            
            d_source = (fract_GoM * self.GoM) + (fract_Pac * self.Pac)
            
            wb = rayleigh_frac.T_function(d_source, self.F, self.T_start, self.T_end, self.dT, self.ax, self.x_lim, self.y_lim)
            
            wb.dl_function()
            
            fract_GoM = fract_GoM - self.dfract
        
        wb_2 = rayleigh_frac.T_function_find(self.T_gen, self.dl_gen, self.ax)
        
        wb_2.T_function_plot()
        
        

