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

		# code that auto matches and joins any frames



	def matching_columns(frames):
    '''assumes consistent labeling of columns '''
    col =[]
    for i in frames[0]:
        for j in frames[1]:
            if (i==j):
                col.append(i)
    if len(np.array(col))>1:
        print ('more then one matching column')
    return col


	def combining(frames):
		''' combines data frames into large master frame
		is however reliant on feeding in data frames in the correct order
		could be fixed with a try and except statement that would put the incompatible dataframe 
		to the end of the list until enough have been maerged that it can fit in'''

		n_frames=len(frames) # number of frames
		master_frame=frames[0]

		def merge(frame1,frame2):
			col = matching_columns([frame1,frame2])[0] # just in case there are more then 1
			merged_frame = frame1.merge(frame2, on = col)
			return merged_frame

		for i in np.arange(1.,n_frames,1.):
			mer= merge(master_frame,frame[i])
			master_frame=mer

		return master_frame



