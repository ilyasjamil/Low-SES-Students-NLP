#import statements
from openie import StanfordOpenIE
import os

#paths to the folders where the texts are stored and where the triples will be stored
dataFolder = "C:\\Users\\IJ\\Desktop\\research2\\data"
triplesFolder = "C:\\Users\\IJ\\Desktop\\research2\\triples"

#script to get the triples from each file and storing them in new files
properties = properties = {'openie.affinity_probability_cap': 2 / 3,}
with StanfordOpenIE(properties=properties) as client:
    for file in os.listdir(dataFolder):
        with open(os.path.join(dataFolder, file),'r',encoding="utf-8",errors='ignore') as f:
            triplesFile = open(os.path.join(triplesFolder,"tripleOf"+file),'w')
            for line in f:
                for triple in client.annotate(line):
                    triplesFile.write(triple['subject']+" "+triple['relation']+" "+triple['object']+"\n")
            triplesFile.close()
        f.close()
