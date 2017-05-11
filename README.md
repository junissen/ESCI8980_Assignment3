# ESCI8980_Assignment3
Assignment 3 for ESCI8980 created by Julia Nissen

Rayleigh fractionation describes the depletion in the d18O values of vapor and resulting condensate due to a decrease in the fraction of original moisture remaining. This can also change with temperature and moisture source composition. Assignment includes four unique Rayleigh fractionation models, exploring the changes in d18O of condensate due to varying temperature an due to varying moisture source compositions, and outputs a resulting .png file. 

##### rayleigh_frac.py
------
Requires numpy

* class F_function(): requires the value of the initial water vapor, the fractionation factor alpha, the axis to plot, and the x and y limits of the axis. 
Class includes loops to change the fraction of moisture remaining and calculate the resultant d18O of vapor or condensate.

  * def dv_function(): calculates the d18O of vapor due to changing moisture fraction and returns plotted curve
  * def dv_function_print(): outputs the initial value for d18O of vapor
  * def dl_function(): calculates teh d18O of condensate due to changing moisture fraction returns plotted curve
  * def dl_function_print(): outputs the initial value for d18O of condensate

* class F_function_find(): requires the value of the initial water vapor, the fractionation factor alpha, a specified value for d18O of condensate, and the axis to plot.
Class calculates and plots the fraction of moisture remaining for a specified alpha and condensate value.

  * def F_function_find(): calculates the fraction of moisture remaining for given alpha and condensate value
  * def F_function_plot(): plots the fraction of moisture remaining against the condensate value on the chosen axis
  
* class T_function(): requires the isotopic value for the moisture source, the fraction of moisture remaining, the initial temperature, the final temperature, dT, the axis to plot, and the x and y limits of the axis. 
Class includes loops to change the temperature and calculate the resultant d18O of condensate.

  * def dl_function(): calculates the d18 of condensate due to changing temperature at a specific fractino of moisture remaining.

* class T_function_find(): requires a specified temperature and d18O of condensate value, and the axis to plot.
Class plots the temperature and d18O of condensate on the specified axis.

  * def T_function_plot(): plots the temperature and 18O of condensate on the chosen axis.

##### rayleigh_model.py
-------
Requires rayleigh_frac and numpy

* class rayleigh_temp_model(): requires a general moisture source composition, dT, initial temperature, final temperature, specific temperature, specific d18O of condensate, axis to plot, an option to include d18O of vapor on plot, and the axis limit parameter. 
Class calculates changes in d18O of condensate (and vapor) and fraction remaining resulting from varying temperatures. 

  * def temp_model(): loop for varying temperature values. Plots fraction remaining versus d18O for varying temperatures.
  * def temp_source_print(): calculates and plots the fraction of moisture remaining for a specific average temperature and specific average isotopic composition of condensate, for varying  moisture sources.

* class rayleigh_source_model(): requires a specific fraction remaining, a Gulf of Mexico source composition, a Pacific source composition, dT, initial temperature, final temperature, specific temperature, specific d18O of condensate, axis to plot, and the axis limit parameters.
Class calculates the changes in d18O of condensate and temperature resulting from varying moisture source compositions. 

  * def source_model(): loop for varying composition values. Plots temperature versus d18O for moisture trajectories varying from 100% Gulf of Mexico moisture to 100% Pacific moisture. 


##### rayleigh_run.py
---------
Requires rayleigh_model, matplotlib.pyplot, matplotlib.patches, and numpy

This file includes input parameters and plotting commands for creating a 2 x 2 figure with 4 Rayleigh fractionation models. 
Input parameters and model parameters have been chosen to explore the potential changes in the d18O of condensate in Minneapolis, MN due to changing temperature or changing moisture source compositions. 

To run model, save rayleigh_frac.py, rayleigh_model.py, and rayleigh_run.py in the same folder. Guide to proper directory using terminal command line. Run program either by running rayleigh_run.py in Python text editor interface or by typing "python rayleigh_run.py" in Terminal command line. Program will provide some command line information, including fractionation effects due to temperature and fraction remaining in Minneapolis at specified values. Additionally, program will create a .png file of the created plot in the same folder.



