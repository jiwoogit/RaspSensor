fileName = "dataAnalysis.py"

start = 4

end = 221

numEnter = 0

tabtab = '\t'

outputName = fileName[:fileName.rfind('.')] + "_chg" + fileName[fileName.rfind('.'):]

print(outputName)

with open(outputName, 'w') as g:

    with open(fileName, 'r') as f:

        temp = f.read(4096)

        while temp:

            for i in temp:

                g.write(i)
                
                if i == "\n":

                    numEnter += 1

                    if(numEnter >= start and numEnter < end):

                        g.write(tabtab)

            temp = f.read(1024)

