# This tag for comments 
# print code 
#print("Hello, World!")
# End of the code
# This is a simple Python script that prints "Hello, World!" to the console.

# Variables and Data Types in Python
#x = 5
#y = 10
#sum = x + y
#print("This sum of x = ",x, " and the y = ",y, "this is the sum =",sum)

# Variable naming conventions in Python
#myvar = "John"
#my_var = "John"
#_my_var = "John"
#myVar = "John"
#MYVAR = "John"
#myvar2 = "John"


# Multiple variable assignment
#x, y, z = "Orange", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)

# One value to multiple variables
#x = y = z = "Orange"
#print(x)
#print(y)
#print(z)


# Unpack a collection
#fruits = ["apple", "banana", "cherry"]
#x, y, z = fruits
#print(x)
#print(y)
#print(z)


# Output variables

#x = 22

#def myfunc():
 #   y = 300
  #  print(x + y)

#myfunc()




# while True:
#     num = input ("enter a int or string ")

#     num2 = random.randint(1,100)
    
#     try:
#         val = int(num)
#         if val == num2:
#             print ("you win", " the random number was: ", num2)
#             break
#         else:
#             if val > num2:
#                 print ("too high")
#             elif val < num2:
#                 print ("too low")        
#         continue
#     except ValueError:
#         print ("you entered a strintg ")


# import random
# num2 = random.randint(1,100)
# while True:
#     num = input ("you have to enter a int number ")
   
#     try:
#         val = int(num)
#         if val == num2:
#             print ("you win")
#             break
#         elif val > num2:
#             print ( "too high", num2)
#         elif val < num2:
#             print ("too low", num2)
#             continue
#     except ValueError:
#         print ("you have to enter a int number")






# import datetime

# resor = []

# while True:
#     print("\n=== RESEPLANERARE ===")
#     print("1. Lägg till resa")
#     print("2. Visa alla resor")
#     print("3. Sök resa")
#     print("4. Beräkna totalkostnad")
#     print("5. Sortera resor")
#     print("0. Avsluta")

#     val = input("Välj ett alternativ: ")

#     if val == "1":
#         # === Lägg till resa ===
#         datum = input("Datum (YYYY-MM-DD): ")
#         destination = input("Destination: ")

#         aktiviteter = []
#         print("Lägg till aktiviteter (skriv 'klar' när du är färdig):")
#         while True:
#             aktivitet = input("> ")
#             if aktivitet.lower() == "klar":
#                 break
#             aktiviteter.append(aktivitet)

#         kostnader = {}
#         print("Lägg till kostnader (skriv 'klar' för att avsluta):")
#         while True:
#             kategori = input("Kategori (t.ex. flyg, boende, mat): ")
#             if kategori.lower() == "klar":
#                 break
#             try:
#                 belopp = float(input(f"Kostnad för {kategori}: "))
#                 kostnader[kategori] = belopp
#             except ValueError:
#                 print("Fel: Ange ett numeriskt värde.")

#         resa = {
#             "info": (datum, destination),
#             "aktiviteter": aktiviteter,
#             "kostnader": kostnader
#         }

#         resor.append(resa)
#         print(f"Resa till {destination} har lagts till!")

#     elif val == "2":
#         # === Visa alla resor ===
#         if not resor:
#             print("Inga resor registrerade ännu.")
#         else:
#             for i, resa in enumerate(resor, start=1):
#                 datum, destination = resa["info"]
#                 print(f"\n{i}. {destination} ({datum})")
#                 print("  Aktiviteter:", ", ".join(resa["aktiviteter"]))
#                 print("  Kostnader:", ", ".join([f"{k}: {v} kr" for k, v in resa["kostnader"].items()]))

#     elif val == "3":
#         # === Sök resa ===
#         term = input("Ange sökterm (destination eller aktivitet): ").lower()
#         hittade = []
#         for resa in resor:
#             datum, destination = resa["info"]
#             if term in destination.lower() or any(term in akt.lower() for akt in resa["aktiviteter"]):
#                 hittade.append(resa)

#         if not hittade:
#             print("Inga resor hittades.")
#         else:
#             print(f"\nHittade {len(hittade)} resor:")
#             for i, resa in enumerate(hittade, start=1):
#                 datum, destination = resa["info"]
#                 print(f"\n{i}. {destination} ({datum})")
#                 print("  Aktiviteter:", ", ".join(resa["aktiviteter"]))
#                 print("  Kostnader:", ", ".join([f"{k}: {v} kr" for k, v in resa["kostnader"].items()]))

#     elif val == "4":
#         # === Totalkostnad ===
#         if not resor:
#             print("Inga resor registrerade ännu.")
#         else:
#             total = sum(sum(resa["kostnader"].values()) for resa in resor)
#             print(f"\nTotala kostnader för alla resor: {total:.2f} kr")

#     elif val == "5":
#         # === Sortera resor ===
#         if not resor:
#             print("Inga resor att sortera.")
#         else:
#             print("\nSortera efter:")
#             print("1. Datum")
#             print("2. Destination")
#             sort_val = input("> ")

#             if sort_val == "1":
#                 resor.sort(key=lambda r: datetime.datetime.strptime(r["info"][0], "%Y-%m-%d"))
#                 print("Resorna har sorterats efter datum!")
#             elif sort_val == "2":
#                 resor.sort(key=lambda r: r["info"][1].lower())
#                 print("Resorna har sorterats efter destination!")
#             else:
#                 print("Ogiltigt val.")

#     elif val == "0":
#         print("Avslutar programmet...")
#         break

#     else:
#         print("Ogiltigt val, försök igen!")