'''
Author: Andrew Hostetler
Created: 4/13/21
Version Py: 3
Notes: This script has been developed for a class assigment in the Spring 2021
  session of Python Programming. The script takes inputs of the length and
  width of a space as well as rainfall amount. Calculations using these
  variables produce measures of rainfall runoff in cubic inches and gallons.
  The input variables and output of rainfall in gallons are printed upon
  executing the script.
'''

#Define variables, assign values
length_ft = 50 #surface side length
width_ft = 20 #surface side width
rain = 1 #rainfall amount in inches


#Calculate area in feet and inches
area_sqft = length_ft * width_ft
area_sqin = area_sqft*(12**2)

#Calculate volume of rain water runoff in cubic inches and gallons
runoff_cuin = area_sqin*rain #cubic inches
runoff_gl = runoff_cuin/231 #gallons

#Print results
print ("plot_length is:",length_ft)
print ("plot_width is:",width_ft)
print ("rainfall_inches is:",rain)
print ("runoff_gallons is:",runoff_gl)