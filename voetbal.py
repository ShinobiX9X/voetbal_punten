import datetime # voor het berekenen van finale data

# Funcie om ploegen toe te voegen
def ploeg_toevoegen(ploegen, nieuwe_ploeg):
	ploegen.append(nieuwe_ploeg)

# Het aantal ploegen ingeven en dan x aantal ploegen naam vragen
aantal_ploegen = int(input("Geef het aant ploegen in: "))
lijst_ploegen=[]
i = 1
while i <= aantal_ploegen:
    ploeg_toevoegen(lijst_ploegen,input('{}{}{}'.format("Naam ploeg #", (i),(": "))))
    i =(i+1)

# De scorelijst initialiseren
lijst_totalen=[0] * aantal_ploegen

#print ("Punten op: ", *lijst_totalen, " voor ploegen ", *lijst_ploegen) #debug

pt = 0 # Zet de positieteller op 0
for ploeg in lijst_ploegen:
    ploeg2idx = (pt+1) # Zet ploeg 2 index op positieteller +1
    while ploeg2idx < aantal_ploegen: # Nu door de overgebleven ploegen loopen
        print ("Ploeg ", lijst_ploegen[pt], " speelt tegen ", lijst_ploegen[ploeg2idx])
        ploeg1doelpunten=int(input('{}{}'.format(lijst_ploegen[pt], " score: ")))
        ploeg2doelpunten=int(input('{}{}'.format(lijst_ploegen[ploeg2idx], " score: ")))
        # Bereken en voeg scores toe
        if ploeg1doelpunten > ploeg2doelpunten:
        	lijst_totalen[pt]= (lijst_totalen[pt] + 3)
        elif ploeg2doelpunten >ploeg1doelpunten:
            lijst_totalen[ploeg2idx]= (lijst_totalen[ploeg2idx] + 3)
        elif ploeg1doelpunten == ploeg2doelpunten:
            lijst_totalen[pt]= (lijst_totalen[pt] + 1)
            lijst_totalen[ploeg2idx]= (lijst_totalen[ploeg2idx] + 1)
        #else:
            #print ("Doelpunt error conditie:") #debug
        #print ("Huidige scorelijst: ", *lijst_totalen, " voor ploegen ", *lijst_ploegen) #debug
        # Increment ploeg 2 tot de volgende
        ploeg2idx = (ploeg2idx+1)
    pt = (pt+1) # Op naar de volgende ploeg

# Lijsten samen sorteren
lijst_samen_gesorteerd = sorted(zip(lijst_totalen,lijst_ploegen), reverse=True)

#print (lijst_samen_gesorteerd) #debug

# Resultaten printen
j = 0 # zet teller op nul voor gesorteerde lijst
for item in lijst_samen_gesorteerd:
	print (f"Komt op plaats {j+1}: {lijst_samen_gesorteerd[j][1]} met {lijst_samen_gesorteerd[j][0]} punten")
	#print(lijst_samen_gesorteerd[j][0]) #Debug
	#print(lijst_samen_gesorteerd[j][1]) #Debug
	j += 1

print("\n") #een lijntje tussen laten

# Hier volgen 2 lijnen, wie wanneer finale en halve finale spelen
print (f"{lijst_samen_gesorteerd[0][1]} speelt de finale op {(datetime.date.today()+datetime.timedelta(days=2))} om 20:00")
print (f"{lijst_samen_gesorteerd[1][1]} speelt de halve finale op {(datetime.date.today()+datetime.timedelta(days=3))} om 20:00")
