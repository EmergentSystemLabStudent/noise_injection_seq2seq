import os
import glob
import re
import pandas as pd
import sys

noisedata=["PI_0.05PS_0.9PD_0.05" ,"PI_0.0PS_0.0PD_0.0PS_S1.0" ,"PI_0.1PS_0.1PD_0.1PS_S0.7" ,"PI_0.2PS_0.2PD_0.2PS_S0.4" ,"PI_0.3PS_0.3PD_0.3PS_S0.1"]
datatypes =["phoneme","Noisy"]
attentions=["attention_","Noattention_"]
#Noattention_PI_0.3PS_0.3PD_0.3PS_S0.1_Noisy_model
filename = sys.argv[1]+"ResultmatomeBlue.csv"
ID = 0
for attetnion in attentions:
    for data in noisedata:
	for Type in datatypes:
            path=str(attetnion)+str(data)+"_"+str(Type)+"_model"
	    print("path:",path)
	    if (os.path.exists("./"+path)):
		print(glob.glob("./"+path+"/"+'log_*'))
		file=glob.glob("./"+path+"/"+'log_*')
		print("file:",file)
		sortdata=sorted([ x for x in file if os.path.isfile(x)], key=os.path.getmtime)
		print("sortdata :",sortdata)				
		latent_file=sortdata[-1]
		print(latent_file)
		with open(latent_file,"r") as f:
	            for line in f.readlines():
			if(line.find("Best bleu") > 0):
		            start=line.find("test ppl")
			    end=line.rfind(",")
			    testdata=line[start:end].replace(" test bleu","").replace("test ppl ","").split(",")
			    float_testdata=[float(s) for s in testdata]
			    frame =pd.DataFrame([[str(latent_file),float(float_testdata[0]),float(float_testdata[1])]],columns=["data","PPL","BLUE"])
			    if (ID ==0 ):
                                frame.to_csv(filename,index=False,mode='a')
				ID = 1
			    else:
				frame.to_csv(filename,index=False,header=False,mode='a')

