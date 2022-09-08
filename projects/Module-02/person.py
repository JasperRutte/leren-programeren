naam = input("Wat is je naam? ")
adres = input("Wat is je adres? ")
postcode = input("Wat is je postcode? ")
woonplaats = input("Wat is je woonplaats? ")
adreskaart = f"""
----------------------------------------------------
|  Naam      : {naam}                
|  Adres     : {adres}           
|  Postcode  : {postcode}                         
|  Woonplaats: {woonplaats}                         
 ----------------------------------------------------
"""
print(adreskaart)
