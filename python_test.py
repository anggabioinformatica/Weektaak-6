##Wie dit leest, is een retard

def main():
    naam = "sequence_pep.gb"
    sequence = leesBestand(naam)
    print(sequence,"\n")
    gc_perc = bepaalGCpercentage(sequence)
    schrijfHTMLrapport(gc_perc, sequence, naam)
    #JOELS SHIT

def leesBestand(bestandsnaam):
    bestand = open(bestandsnaam)
    raw_data = ""
    lees = False
    for regel in bestand:
        if "ORIGIN" in regel:
            lees = True
        if lees == True:
            raw_data += regel[10:]
    sequence = raw_data.replace(" ", "").replace("\n", "").replace("\r", "")
    return sequence


def bepaalGCpercentage(sequence):
    x = sequence.upper()
    total = len(x)
    #print (total)
    c = x.count("C")
    #print (c)
    g = x.count("G")
    #print (g)
    gc_total = g+c
    #print (gc_total)
    gc_perc = (gc_total / total)*100
    print ("GC:","{:.2f}".format(gc_perc)+"%")
    return gc_perc


def schrijfHTMLrapport (gc_perc, sequence, naam):
##    JOEL MOFO, THIS IS YOUR SHIT
    html_file = open("pep_rapport.html", "w")
    gcperc = str(gc_perc)
    html_file.write(gcperc)
    html_file.write(sequence)
    html_file.write(naam)
    html_file.close()

main()
