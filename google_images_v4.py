#import modules
import numpy as np
import pandas as pd 


''' set of tools for manipulating image data from google. 
It should work best when using pandas as a dataframe structure 
but that can be rewritten.
'''

def find_class (class_name,array,column):
    ''' find a specific class in an array'''
    
    #check for length of input 
    if len(class_name)>1.:
    	numbers = []
    	for i in class_name:
    		index = array[array[column]==i].index[0]
    		numbers.append(index)
		filtered_array=cl_des.iloc[numbers]

	else:
    	filtered_array = array[array[column]==class_name]#would work better if column was defined
    return filtered_array


    #Needs section on how to lead in data