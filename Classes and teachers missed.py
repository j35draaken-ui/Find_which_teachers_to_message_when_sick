#enter name of teacher (if he/she has two topics enter the topic abreviation before the name) followed by = 0
Marletta = 0
ITMarletta = 0
Detken = 0
Kammermeier = 0
Hellinger = 0
Detken = 0
Francis = 0
BIOFranncis = 0
Long = 0
Conradt = 0
Johns = 0
Weyer = 0
POWIWeyer = 0
Mitten = 0
#now enter name of teacher (if they have two topics enter the topic abbreviation before the name) followed by day  = ""
Marlettaday = ""
ITMarlettaday = ""
POWIWeyerday = ""
BIOFrancisday = ""
Detkenday = ""
Kammermeierday = ""
Hellingerday = ""
Francisday = ""
Longday = ""
Conradtday = ""
Johnsday = ""
Weyerday = ""
Mittenday = ""

#do not change anything below this line untill the next comment
nrdays = int(input("Enter number of days: "))
days = input("Enter the names of the days separated by spaces: ").split()
for day in days: #add the teachers/topics you have on Monday and day missed in the same format as below
    if day == "Monday":
        Marletta += 1
        Marlettaday += " Monday "
        ITMarletta += 1
        ITMarlettaday += " Monday "
        POWIWeyer += 1
        POWIWeyerday += " Monday "
        Hellinger += 1
        Hellingerday += " Monday "
        Kammermeier += 1
        Kammermeierday += " Monday "
        Detken += 1
        Detkenday += " Monday "
    elif day == "Tuesday": #add the teachers/topics you have on Tuesday and day missed in the same format as below
        Marletta += 1
        Marlettaday += " Tuesday "
        ITMarletta += 1
        ITMarlettaday += " Tuesday "
        BIOFranncis += 1
        BIOFrancisday += " Tuesday "
        Long += 1
        Longday += " Tuesday "
    elif day == "Wednesday":#add the teachers/topics you have on Wednesday and day missed in the same format as below
        Kammermeier += 1
        Kammermeierday += " Wednesday "
        Mitten += 1
        Mittenday += " Wednesday "
        Weyer += 1
        Weyerday += " Wednesday "
    elif day == "Thursday":#add the teachers/topics you have on Thursday and day missed in the same format as below
        Hellinger += 1
        Hellingerday += " Thursday "
        Mitten += 1
        Mittenday += " Thursday "
        Johns += 1
        Johnsday += " Thursday "
        Marletta += 1
        Marlettaday += " Thursday "
    elif day == "Friday":#add the teachers/topics you have on Friday and day missed in the same format as below
        Kammermeier += 1
        Kammermeierday += "  Friday "
        Francis += 1
        Francisday += "  Friday "
        Conradt += 1
        Conradtday += "  Friday "
#underneath change the names and variables to the ones you have used above, do not change the structure of the lines, be ware of duplicates due to teachers with two (+) topics
if Marletta > 0:
    print(f"I have missed Marlettas Math classes  {Marletta}  times on days: {Marlettaday}")
if ITMarletta > 0:
    print(f"I have missed Marlettas IT classes  {ITMarletta}  times on days: {ITMarlettaday}")
if Detken > 0:
    print(f"I have missed Detkens Music classes  {Detken}  times on days: {Detkenday}")
if Kammermeier > 0:
    print(f"I have missed Kammermeiers German classes  {Kammermeier}  times on days: {Kammermeierday}")
if Hellinger > 0:
    print(f"I have missed Hellingers French classes  {Hellinger}  times on days: {Hellingerday}")
if Francis > 0:
    print(f"I have missed Francis' Physics classes  {Francis}  times on days: {Francisday}")
if BIOFranncis > 0:
    print(f"I have missed Franciss BIO  classes  {BIOFranncis}  times on days: {BIOFrancisday}")
if Long > 0:
    print(f"I have missed Longs  chemistry classes  {Long}  times on days: {Longday}")
if Conradt > 0:
    print(f"I have missed Conradts Ethics  classes  {Conradt}  times on days: {Conradtday}")
if Johns > 0:
    print(f"I have missed Johns Geography classes  {Johns}  times on days: {Johnsday}")
if Weyer > 0:
    print(f"I have missed Weyers History classes  {Weyer}  times on days: {Weyerday}")
if POWIWeyer > 0:
    print(f"I have missed  Weyers POWI classes  {POWIWeyer}  times on days: {POWIWeyerday}")
if Mitten > 0:
    print(f"I have missed Mittens English classes  {Mitten}  times on days: {Mittenday}")    
