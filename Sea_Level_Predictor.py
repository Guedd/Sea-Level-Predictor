#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("C:/Users/DJEF/Downloads/epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(df['Year'].min(), 2050)
    fit = years * line.slope + line.intercept
    plt.plot(years, fit)

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    line = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    years = range(2000, 2050)
    fit = years * line.slope + line.intercept
    plt.plot(years, fit)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

