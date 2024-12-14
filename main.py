import phonenumbers  
from phonenumber import number  
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode  
import folium 


pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

service_provider = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_provider)

key = '-------------------------------------------------------------' #the api key that gets from the opencage.com site . For getting the api key u need to login and then u get a api key from the dashboard .
open_cage_geocoder = OpenCageGeocode(key)

query = str(location)
results = open_cage_geocoder.geocode(query)

if results:  
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat)
    print("Longitude:", lng)

  
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)

    mymap.save("mylocation.html")
    print("Map saved as 'mylocation.html'")
else:
    print("No results found for the location.")


# ( pip install phonenumbers opencage folium ) enter the cmd line on the terminal to install pkg or libraries .
