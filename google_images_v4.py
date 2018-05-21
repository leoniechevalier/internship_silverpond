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


# Needs section on how to lead in data
# find where data is stored

# read in data    
test_im = pd.read_csv(path+filename, header=0)
cl_des = pd.read_csv('class-descriptions-boxable.csv', names=['LabelName','name'])

def read_file(filename, path):
	filename = np.array(filename)
	dataframe_name = np.array(dataframe_name)
	'''reads in data files in various formats 
	(txt and csv so far, expand as neccecary)'''

	if len(filename)>1:
		frames = []
		for i in filename:
			ending = i[-3:]
			
			if ending == 'csv':
				dataframe = pd.read_csv(path+i)
				frames.append(dataframe)
			elif ending == 'txt':
				dataframe = pd.read_table(path+i)
				frames.append(dataframe)
	
			else :
				raise NameError('Invalid data type. Please review input or add to script.')
	
		return frames
	else:
		ending = filename[-3:]
	
		if ending == 'csv':
			dataframe = pd.read_csv(path+filename)
		elif ending == 'txt':
			dataframe = pd.read_table(path+filename)
	
		else :
			raise NameError('Invalid data type. Please review input or add to script.')
	
		return dataframe



