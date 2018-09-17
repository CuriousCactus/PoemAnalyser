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


def split ( dict_line, xcode ): #defining a function that splits up the line:
    stop1 = dict_line.find ("|")
    stop2 = dict_line.find("|",stop1+1)
    temp_stop3a = dict_line.find("|",stop2+1)
    temp_stop3b = dict_line.find(" ",stop2+1)
    if temp_stop3a < temp_stop3b:
        stop3 = temp_stop3a
        stop4 = temp_stop3a
    else:
        stop3 = temp_stop3b
        stop4 = temp_stop3a
    stop5 = dict_line.find(" ",stop3+1)
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
    STRESS = dict_line[stop4+1:stop5]
    result = eval(xcode)
    return [result]

counter = 0
for line in f: #reading input file into 'line'
    import re
    temp = re.split("[ ,.;:!?\s-]|\*|\n|'*|'S",line) #splitting 'line' into words
    words = [x.upper() for x in temp] #raising case of words
    words = [x for x in words if x !='']#getting rid of null words
    print ("line " + str(counter))
    print(words)
    counter = counter + 1
    for word in words: #looping over words in line
        test1 = 0
        test2 = 0 #initializing negative test results
        dict = open("data\mrc2.dct","r") #opening dictionary
        while test1 != 1 and test2 != 1: #reading dictionary line by line while tests are negative
            templine = dict.readline() 
            tempstop = templine.find("|")
            tempword = templine[51:tempstop] #finding word from line
            if tempword == word: #positive test
                test1 = 1 # if found word then assign parts of dictionary
                if split (templine, code)[0] == "": #second test
                    test1 = 0
                    test2 = 0
                else:
                    dict.close()
                    print ( split (templine, code)[0] )
                    g.write( split (templine, code)[0] ) #print positive ouput
                    g.write(" ")
                    test2 = 1
                    break
            elif tempword == "ZYMURGY": #end of dictionary file
                dict.close()
                false_result = word.lower() #print negative output, original word
                g.write( false_result + " ")
                test1 = 1
                test2 = 1
                break
            else: #negative test
                test1 = 0                
    g.write ("\n")

print ("output file: " + loc_outfile )




