#! /usr/bin/env python
def parseConfigFile(filename,defaultConfig={}):
	if __debug__:
		if not type(filename) == str: raise AssertionError
	if type(defaultConfig) == dict:
		config = defaultConfig
	else:
		config = {}
	with open(filename,"r") as f:
		for l in f: # for each line in file
			params = l.split() 
			if not len(params) > 0: continue # it was an empty line
			if params[0][0] == "#": continue # it was a comment
			if len(params) == 1 or params[1][0] == '#': # it should be a boolean value
				if params[0][0] == "!": config[params[0][1:]] = False
				else: config[params[0]] = True
			elif len(params) == 2 or params[2][0] == "#": # it has one property
				config[params[0]] = params[1]
			else: # it has at least two properties
				props = []
				for i in range(1,len(params)): # Is there a comment?
					if params[i][0] == "#": break # There is a comment 
					props.append(params[i]) 
				if not len(props) > 2: raise AssertionError
				config[params[0]] = props
	return config
	
def saveConfigFile(filename,config):
	if __debug__:
		if not type(filename) == str: raise AssertionError
		if not type(config) == dict: raise AssertionError
	with open(filename,"w") as f:
		for p in config: # for each parameter in configuration
			if type(config[p]) == bool:
				neg = ""
				if not config[p]: neg = "!" 
				f.write(neg+p+"\n")
			elif type(config[p]) == list: f.write(p+" "+" ".join(config[p])+"\n")
			elif type(config[p]) == str or type(config[p]) == int or type(config[p]) == float: f.write(p+" "+str(config[p])+"\n")
			#else: f.write(p+" "+str(config[p]))
			else: 
				f.close()
				raise NotImplementedError


if __name__ == '__main__': 
	cfg = parseConfigFile("test_input.txt")
	print(cfg)
	saveConfigFile("test_output.txt",cfg)

