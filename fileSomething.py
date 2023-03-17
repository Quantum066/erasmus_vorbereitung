#to edit the file if exists and already filled


#file name editable
file = open("/home/andrei/DataFromAnalytics/fileSomethingTesting", "r")

contents = file.read()
empty = ""

file.close()

#file name editable
file = open("/home/andrei/DataFromAnalytics/fileSomethingTesting", "w")
#Emptying the file 
file.write(empty)


#============================WANTED CODE UNDER HERE=============================

#                                 EXAMPLE CODE:

inde = ["Create", "Something", "Test"]
numberavg = 0;




file.write("Numbers:                inde:   " + "\n")

for x,y in enumerate(inde):

    file.write("    " + str(x) + "              " + y + "\n")
    numberavg += x

numberavg = numberavg / len(inde)
file.write("Number Average: " + str(numberavg))

file.close()


