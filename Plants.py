import sys

arguments = sys.argv
#argument index 1 is input bestandsnaam, index 2 output bestandsnaam.
filename = "./data/" + arguments[1]
outputnaam = "./Fasta-Sequence/" + arguments[2]
results = []
file_object = open(filename)
file_content = file_object.read()
file_inhoud = file_content.split() #split de file content bij whitespaces zodat het aparte regels zijn
list_species = ["setosa", "versicolor", "virginica"]

#loop het voor alle species
for species in list_species:
    all_width = []
    width_average = 0
    width_total = 0
    
    #dit gedeelte verzamelt de width van de sepal in all_width
    for x in range(len(file_inhoud)):
        regel = file_inhoud[x].split(",")
        if regel[4] == species: 
            all_width.append(regel[1])

    #dit gedeelte berekent het totaal van alle width bij elkaar, en het gemiddelde.      
    for getallen in range(len(all_width)):
        width_total = width_total + float(all_width[getallen]) 
    width_average = width_total / len(all_width)
    
    #print resultaten
    results.append(species, "average sepal width is: ", round(width_average, 3))

with open(outputnaam,"w") as writefile:
    for regels in results:
        writefile.write(regels)
        writefile.write("\n") 
