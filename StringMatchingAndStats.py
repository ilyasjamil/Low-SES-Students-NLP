import os

triplesPath = "C:\\Users\\IJ\\Desktop\\research2\\new_triples2topictopic1\\"
chosenTriplesPath = "C:\\Users\\IJ\\Desktop\\research2\\TriplesWithProbSol\\"

dict_matched = {}
dict_missed = {}
dict_extra = {}
list = os.listdir(triplesPath)
list2 = os.listdir(chosenTriplesPath)

for i in range(len(list)):
    file1 = open("TriplesWithProbSol/"+list2[i],"r")
    dict_matched[list2[i]] = 0
    for line in file1:
        file = open("new_triples2topictopic1/"+list[i],"r")
        for line1 in file:
            if line == line1 and line != '' and line != '\n':
                dict_matched[list2[i]] = dict_matched[list2[i]]+1
   
    # counting number of the LDA triples
    file2 = open("new_triples2topictopic1/"+list[i],"r")
    file = file2.read().splitlines()
    for k in range(len(file)):
        if file[k] == ' ' or file[k] == '' or file[k] == "\n":
            del file[k]
    fileSize = len(file)
    #counting number of selected triples
    file4 = open("TriplesWithProbSol/"+list2[i],"r")
    file3 = file4.read().splitlines()
    for j in range(len(file3)):
            if file3[j] == ' ' or file3[j] == '' or file3[j] == "\n":
                del file3[j]
    file1Size = len(file3)
    
    dict_missed[list2[i]] = file1Size - dict_matched[list2[i]]
    dict_extra[list2[i]] = fileSize - dict_matched[list2[i]]

file2.close()
file4.close()
fileToWrite = open("triplesInfo/"+"INFO_stories2.txt","w")

#writing the results in the text file
for el in dict_matched:
    fileToWrite.write(el+"\n ---- \n"+"matched: "+str(dict_matched[el])+"\nmissed: "+str(dict_missed[el])+"\nextra: "+str(dict_extra[el])+"\n \n")
    
fileToWrite.close()



