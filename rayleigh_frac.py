#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:07:15 2017

@author: julianissen

F_function, F_function_find, T_function, and T_function_find classes and accompanying 
functions generate loops for creating Rayleigh fractionation models. 

Created 05/2017 by Julia Nissen
"""

import numpy as np

class F_function(): 
    """
    Class includes loops to change the fraction of moisture remaining and calculate the resultant 
    d18O of vapor or condensate.
    """
    def __init__ (self, dv_i, alpha, ax, xlim, ylim):
        self.dv_i = dv_i
        self.F = 1.0
        self.dF = 0.0001
        self.alpha = alpha
        self.ax = ax
        self.dv_array = []
        self.dl_array = []
        self.x_lim = xlim
        self.y_lim = ylim

    def dv_function(self):
        """
        Function calculates the d18O of vapor due to changing moisture fraction
        """
        ax = self.ax
        F = self.F
        F_array = []
        while F > 0.0:
            dv = ((self.dv_i + 1000)*(F**(self.alpha-1))) - 1000
            self.dv_array.append(dv)
            F_array.append(F)
            F = F - self.dF
        ax.set_xlim( self.x_lim )
        ax.set_ylim( self.y_lim )
        vapor = ax.plot(F_array, self.dv_array, 'r-', linewidth = 1)
        return vapor 
    
    def dv_function_print(self):
        """
        Function outputs the initial value for d18O of vapor
        """
        return self.dv_array[0]
        
    def dl_function(self):
        """
        Function calculates the d18O of condensate due to changing moisture fraction
        """
        ax = self.ax
        F = self.F
        F_array = []
        while F > 0.0:
            dv = ((self.dv_i + 1000)*(F**(self.alpha-1))) - 1000
            dl = (self.alpha*(dv + 1000)) - 1000   
            self.dl_array.append(dl)
            F_array.append(F)
            F = F - self.dF
        ax.set_xlim( self.x_lim )
        ax.set_ylim( self.y_lim )
        liquid = ax.plot(F_array, self.dl_array, 'b-', linewidth = 1)
        return liquid
    
    def dl_function_print(self):
        """
        Function outputs the initial value for d18O of condensate 
        """
        return self.dl_array[0]
    
    
class F_function_find():
    """
    Class calculates the fraction of moisture remaining for a specific alpha and condensate value.
    """
    
    def __init__(self, dv_i, alpha, dl_avg, ax):
        self.dv_i = dv_i
        self.dl = dl_avg
        self.alpha = alpha
        self.ax = ax
    
    def F_function_find(self):
        """
        Function calculates the fraction of moisture remaining for a specific alpha and condensate value.
        """
        dv = ((self.dl + 1000)/self.alpha) - 1000
        F = np.exp((np.log(dv + 1000) - np.log(self.dv_i + 1000))/(self.alpha - 1))
        return F
    
    def F_function_plot(self):
        """
        Function plots the fraction of moisture remaining for a specific alpha and condensate value
        on chosen axis as a black 'x'.
        """
        ax = self.ax
        dv = ((self.dl + 1000)/self.alpha) - 1000
        F = np.exp((np.log(dv + 1000) - np.log(self.dv_i + 1000))/(self.alpha - 1))
        return ax.plot(F, self.dl,'xk')
    
class T_function():
    """
    Class includes loops to change the temperature and calculate the resultant 
    d18O of vapor or condensate.
    """
    
    def __init__ (self, d_source, F, T_start, T_end, dT, ax, xlim, ylim):
        self.F = F
        self.d_source = d_source
        self.T_start = T_start
        self.T_end = T_end
        self.dT = dT
        self.ax = ax
        self.x_lim = xlim
        self.y_lim = ylim
        self.dl_array = []
        
    def dl_function(self):
        """
        Function calculates the d18O of condensate due to changing temperature
        """
        T_array = []
        T = self.T_start
        
        while T >= self.T_end:
            alpha_evap = np.exp((1.137*((10**3)/(T**2))) - (0.4156/T) -(2.0667*(10**-3))) #from Majoube 1971
            dv_i = self.d_source - ((10**3)*np.log(alpha_evap)) #from Rohling 2013
            alpha_precip = np.exp((-7.685 + 6.7123*((10**3)/T) - 1.6664*((10**6)/(T**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(T**3)))/1000)
            dv = ((dv_i + 1000)*(self.F**((alpha_precip)-1))) - 1000
            dl = ((alpha_precip)*(dv + 1000)) - 1000
            self.dl_array.append(dl)
            T_array.append(T)
            T = T - self.dT 
            
        self.ax.set_xlim( self.x_lim )
        self.ax.set_ylim( self.y_lim )
        return self.ax.plot(T_array, self.dl_array, '#6495ED', linewidth = 1)
    
class T_function_find():
    """
    Class plots the temperature and d18O of condensate on the specified axis
    """
    
    def __init__(self, T_gen, dl_gen, ax):
        self.T_gen = T_gen
        self.dl_gen = dl_gen
        self.ax = ax
    
    
    def T_function_plot(self):
        """
        Function plots the temperature and d18O of condensate on the specified axis
        """
        return self.ax.plot(self.T_gen, self.dl_gen, 'xk')
        
    