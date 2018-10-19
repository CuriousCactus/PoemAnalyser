import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

location = "./data/"
infile = input ("type filename (in ./data/) to convert:\n")
loc_infile = location + infile
f = open(loc_infile,"r")
code = input ("choose one of the following outputs by typing the uppercase code:\n" +
"NLET - Number of letters in the word\n" +
"NPHON - Number of phonemes in the word\n" +
"NSYL - Number of syllables in the word\n" +
"K_F_FREQ - Kucera and Francis written frequency\n" +
"K_F_NCATS - Kucera and Francis number of categories\n" +
"K_F_NSAMP - Kucera and Francis number of samples\n" +
"T_L_FREQ - Thorndike-Lorge frequency\n" +
"BROWN_FREQ - Brown verbal frequency\n" +
"FAM - Familiarity\n" +
"CONC - Concreteness\n" +
"IMAG - Imagery\n" +
"MEANC - Mean Colerado Meaningfulness\n" +
"MEANP - Mean Pavio Meaningfulness\n" +
"AOA - Age of Acquisition\n" +
"TQ2 - Type\n" +
"WTYPE - Part of Speech\n" +
"PDWTYPE - PD Part of Speech\n" +
"ALPHSYL - Alphasyllable\n" +
"STATUS - Status\n" +
"VAR - Phoneme\n" +
"CAP - Capitalised\n" +
"IRREG - Irregular Plural\n" +
"WORD - the actual word\n" +
"PHON - Phonetic Transcription\n" +
"DPHON - Edited Phonetic Transcription\n" +
"STRESS - Stress Pattern\n") #asking user for input file and code

outfile = code + infile
loc_outfile = location + outfile
g = open(loc_outfile,"a") #opening output file
g.truncate (0)

for line in f: #reading input file into 'line'
    import re
    temp = re.split("[ ,.;:!?\s-]|\*|\n|'*|'S",line) #splitting 'line' into words
    words = [x.upper() for x in temp] #raising case of words
    words = [x for x in words if x !='']#getting rid of null words
    print(words)

    for word in words: #looping over words in text
        test = 0 #initializing negative test result
        dict = open("./data/mrc2.dct","r") #opening dictionary
        while test == 0: #reading dictionary line by line while test is negative
            templine = dict.readline() 
            tempstop = templine.find("|")
            tempword = templine[51:tempstop] #finding word from line
            if tempword == word: #positive test
                test = 1
                dict.close()
                dict_line = templine
                break
            elif tempword == "ZYMURGY": #end of dictionary file
                test = 1
                dict.close()
                break
            else: #negative test
                test = 0
        if tempword == "ZYMURGY": #if end of dictionary return original word, in lower case
            result = word.lower()
            g.write(result + " ")
        else: # if found word then assign parts of dictionary
            stop1 = dict_line.find ("|")
            stop2 = dict_line.find("|",stop1+1)
            stop3 = dict_line.find("|",stop2+1)
            stop4 = dict_line.find(" ",stop3+1)
            NLET = dict_line[0:2]
            NPHON = dict_line[2:4]
            NSYL = dict_line[4:5]
            K_F_FREQ = dict_line[5:10]
            K_F_NCATS = dict_line[10:12]
            K_F_NSAMP = dict_line[12:15]
            T_L_FREQ = dict_line[15:21]
            BROWN_FREQ = dict_line[21:25]
            FAM = dict_line[25:28]
            CONC = dict_line[28:31]
            IMAG = dict_line[31:34]
            MEANC = dict_line[34:37]
            MEANP = dict_line[37:40]
            AOA = dict_line[40:43]
            TQ2 = dict_line[43:44]
            WTYPE = dict_line[44:45]
            PDWTYPE = dict_line[45:46]
            ALPHSYL = dict_line[46:47]
            STATUS = dict_line[47:48]
            VAR = dict_line[48:49]
            CAP = dict_line[49:50]
            IRREG = dict_line[50:51]
            WORD = dict_line[51:stop1]
            PHON = dict_line[stop1+1:stop2]
            DPHON = dict_line[stop2+1:stop3]
            STRESS = dict_line[stop3+1:stop4]
	    
            g.write(eval(code) + " ") #print positive ouput
    g.write ("\n")




