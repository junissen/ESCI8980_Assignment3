#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:22:38 2017

@author: julianissen

rayleigh_run file plots four unique Rayleigh fractionation models. The first plots
condensate and vapor d18O values with varying fractions remaining and variable temperatures using a 
general moisture source. The second plots only condensate d18O values with varying fractions remaining 
and variable temperatures using a Gulf of Mexico moisture source. The third plots only condensate d18O values 
with varying fractions remaining and variable temperatures using a Pacific moisture source. The last plots 
only condensate d18O values with varying temperatures, using a set fraction remaining, and variable
moisture source compositions. 

Created 05/2017 by Julia Nissen
"""

import rayleigh_model
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#basic plot format
fig = plt.figure(figsize = (10,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

"""
Model runs
"""

#initial values
d_source_gen = 0.0 #in d18O VSMOW
dT = 2.0   #change in temperature
T_start = 340.0 #in K
T_end = 240.0 #in K
T_gen = 280.0 #avg temperature in Minneapolis ~ 281 K (7.86C)
d_source_GoM = 0.6 #in d18O VSMOW. Avg from Schmidt 1999
d_source_Pac = -0.5 #in d18O VSMOW. Avg from Schmidt 1999
dl_avg = -10.71 #avg d18O VSMOW of annual rainfall in Minneapolis from Ito et al. 

T_start_Hol = 285.0
T_end_LGM = 270.0
dT_plei = 0.1

#constructing model plots using rayleigh_model and rayleigh_frac modules. 

#gensource plots fraction remaining vs. d18O for both condensate and vapor using a general moisture source
#of 0.0 per mille (VSMOW) and changing temperature
wb_gensource = rayleigh_model.rayleigh_temp_model(d_source_gen, dT, T_start, T_end, T_gen, dl_avg, ax1, "y", "full")

temp_gensource = wb_gensource.temp_model()

fract_MN_gensource = wb_gensource.temp_source_print() #calculates the fraction remaining in MN rainfall using T and d18O averages

#GoMsource plots fraction remaining vs. d18O for condensate using an average Gulf of Mexico moisture source input value 
# of 0.6 per mille (VSMOW) and changing temperature
wb_GoMsource = rayleigh_model.rayleigh_temp_model(d_source_GoM, dT, T_start, T_end, T_gen, dl_avg, ax2, "n", "half")

temp_GoMsource = wb_GoMsource.temp_model()

fract_MN_GoMsource = wb_GoMsource.temp_source_print() #calculates the fraction remaining in MN rainfall using T and d18O averages

#Pacsource plots fraction remaining vs. d18O for condensate using an average Pacific moisture source input value
#of -0.5 per mille (VSMOW) and changing temperature 
wb_Pacsource = rayleigh_model.rayleigh_temp_model(d_source_Pac, dT, T_start, T_end, T_gen, dl_avg, ax3, "n", "half")

temp_Pacsource = wb_Pacsource.temp_model() 

fract_MN_Pacsource = wb_Pacsource.temp_source_print() #calculates the fraction remaining in MN rainfall using T and d18O averages

#variablesource plots temperature in K vs. d18O for condensate using average values of Gulf of Mexico and Pacific moisture sources
#and changing the percentage of each moisture source (from 100% GoM to 100% Pacific). The model is run at a set fraction remaining, 
#calculated from the fract_MN_gensource function.

wb_variablesource = rayleigh_model.rayleigh_source_model(0.378, d_source_GoM, d_source_Pac, dT_plei, T_start_Hol, T_end_LGM, T_gen, dl_avg, ax4, "source")

source = wb_variablesource.source_model()


"""
Plot formatting
"""

#tick formatting
yax1_major_ticks = np.arange(-70.0, 4.0, 10)
yax1_minor_ticks = np.arange(-70.0, 4.0, 5)
xax1_major_ticks = np.arange(0, 1.01, 0.2)
xax1_minor_ticks = np.arange(0, 1.01, 0.1)
ax1.set_yticks(yax1_major_ticks)
ax1.set_yticks(yax1_minor_ticks, minor = True) 
ax1.set_xticks(xax1_major_ticks)
ax1.set_xticks(xax1_minor_ticks, minor = True)
for tick in ax1.xaxis.get_major_ticks(): tick.label.set_fontsize(8)
for tick in ax1.yaxis.get_major_ticks(): tick.label.set_fontsize(8)

yax_major_ticks = np.arange(-25.0, 0.01, 5)
yax_minor_ticks = np.arange(-25.0, 0.01, 2.5)
xax_major_ticks = np.arange(0.3, 0.51, 0.05)
xax_minor_ticks = np.arange(0.3, 0.51, 0.025)
ax2.set_yticks(yax_major_ticks)
ax2.set_yticks(yax_minor_ticks, minor = True) 
ax2.set_xticks(xax_major_ticks)
ax2.set_xticks(xax_minor_ticks, minor = True)
ax3.set_yticks(yax_major_ticks)
ax3.set_yticks(yax_minor_ticks, minor = True) 
ax3.set_xticks(xax_major_ticks)
ax3.set_xticks(xax_minor_ticks, minor = True)
for tick in ax2.xaxis.get_major_ticks(): tick.label.set_fontsize(8)
for tick in ax2.yaxis.get_major_ticks(): tick.label.set_fontsize(8)
for tick in ax3.xaxis.get_major_ticks(): tick.label.set_fontsize(8)
for tick in ax3.yaxis.get_major_ticks(): tick.label.set_fontsize(8)

yax4_major_ticks = np.arange(-13.0, -8.9, 1.0)
yax4_minor_ticks = np.arange(-13.0, -8.9, 0.5)
xax4_major_ticks = np.arange(270.0, 285.1, 5.0)
xax4_minor_ticks = np.arange(270.0, 285.1, 2.5)
ax4.set_yticks(yax4_major_ticks)
ax4.set_yticks(yax4_minor_ticks, minor = True) 
ax4.set_xticks(xax4_major_ticks)
ax4.set_xticks(xax4_minor_ticks, minor = True)
for tick in ax4.xaxis.get_major_ticks(): tick.label.set_fontsize(8)
for tick in ax4.yaxis.get_major_ticks(): tick.label.set_fontsize(8)

#axis labeling
d18o = r'$\delta^{18}\!O$'

ax1.set_ylabel(d18o + ' (VSMOW)', fontsize = 8, labelpad = -0.5)
ax2.set_ylabel(d18o + ' (VSMOW)', fontsize = 8, labelpad = -0.5)
ax3.set_ylabel(d18o + ' (VSMOW)', fontsize = 8, labelpad = -0.5)
ax4.set_ylabel(d18o + ' (VSMOW)', fontsize = 8, labelpad = -0.5)

ax1.set_xlabel('Fraction of moisture remaining', fontsize = 8, labelpad = 0.5)
ax2.set_xlabel('Fraction of moisture remaining', fontsize = 8, labelpad = 0.5)
ax3.set_xlabel('Fraction of moisture remaining', fontsize = 8, labelpad = 0.5)
ax4.set_xlabel('Temperature in K', fontsize = 8, labelpad = 0.5)


#plot titles
ax1.set_title('General Source Rayleigh fractionation model', fontsize = 10)
ax2.set_title('Gulf of Mexico Source Rayleigh fractionation model', fontsize = 10)
ax3.set_title('Pacific Source Rayleigh fractionation model', fontsize = 10)
ax4.set_title('Variable Source model with changing T', fontsize = 10)


#compress image layout
fig.tight_layout()

#arrows
ax1.annotate("Decreasing temperature", xy=(0.7885, -63), xytext=(0.915, -48), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 6) 
ax2.annotate("Decreasing temperature", xy = (0.4650, -22.5), xytext = (0.490, -17.5),
             arrowprops = dict(arrowstyle = "->"), fontsize = 6)
ax3.annotate("Decreasing temperature", xy = (0.4650, -22.5), xytext = (0.490, -17.5),
             arrowprops = dict(arrowstyle = "->"), fontsize = 6)
ax4.annotate("Decreasing % of GoM moisture", xy = (281.4, -12.6), xytext = (279.0, -11.8),
             arrowprops = dict(arrowstyle = "->"), fontsize = 6)

#modified legend
ax1.add_patch(patches.Rectangle((0.02, -5.6), 0.33, 8.55, fill = False, edgecolor = '#808080'))
ax2.add_patch(patches.Rectangle((0.305, -3.7), 0.065, 3.25, fill = False, edgecolor = '#808080'))
ax3.add_patch(patches.Rectangle((0.305, -3.7), 0.065, 3.25, fill = False, edgecolor = '#808080'))
ax4.add_patch(patches.Rectangle((279.6, -9.6), 5.0, 0.53, fill = False, edgecolor = '#808080'))

ax1.text(0.25, 1.0, 'Condensate', fontsize = 7.0, color = 'b')
ax1.text(0.22, -1.37, 'Vapor', fontsize = 7.0, color = 'r')
ax1.text(0.24, -3.55, 'MN avg (T)',fontsize = 7.0, color = '#6495ED')
ax1.text(0.32, -5.465, "x : MN avg (T & " + u"\u03b4" + "18O)", fontsize = 7.0, color = 'k')

ax2.text(0.355, -1.48, 'Condensate', fontsize = 7.0, color = 'b')
ax2.text(0.352, -2.4, 'MN avg (T)',fontsize = 7.0, color = '#6495ED')
ax2.text(0.364, -3.2, "x : MN avg (T & " + u"\u03b4" + "18O)", fontsize = 7.0, color = 'k')

ax3.text(0.355, -1.48, 'Condensate', fontsize = 7.0, color = 'b')
ax3.text(0.352, -2.4, 'MN avg (T)',fontsize = 7.0, color = '#6495ED')
ax3.text(0.364, -3.2, "x : MN avg (T & " + u"\u03b4" + "18O)", fontsize = 7.0, color = 'k')

ax4.text(281.0, -9.3, 'Condensate', fontsize = 7.0, color = '#6495ED')
ax4.text(280.2, -9.45, "x : MN avg (T & " + u"\u03b4" + "18O)", fontsize = 7.0, color = 'k')

#final layout and save
plt.savefig('Rayleigh_model', dpi = 500)