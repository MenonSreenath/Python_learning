travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(a,b,c):
    new_country={}
    new_country["country"] = a
    new_country["visits"] = b
    new_country["cities"] = c
    travel_log.append(new_country)



add_new_country("russia",2,["Moscow","Saint Petersburg"])
print(travel_log)