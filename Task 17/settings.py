import os
import numpy as np
import configparser

# For the below to work added [VARIABLES] as heading in app.settings

class Settings():
	def __init__(self,filename):
		config = configparser.ConfigParser(inline_comment_prefixes="#") # Use ConfigParser to read variable names and values from app.settings 
		config.optionxform = str # This instruction preserves the case of keys (variable names)
		config.read('app.settings') # Reading app.settings
		for key in config['VARIABLES']: # key is variable name
			values = config['VARIABLES'][key] # variable values
			try:
				formated_values = float(values) # converting numerical keys to floats
			except:
				formated_values = values # non-numerical keys remain as strings
			
			setattr(self,key,formated_values)


     
