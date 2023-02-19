from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Business_Mapping")

class pin_location:
    longitude = 0
    latitude = 0

    def __init__(self, name, address, priority, category):
        self.name = str(name)
        self.priority = int(priority)
        self.category = str(category)
        self.format_address(address)
        self.format_geo_coordinates()
        


    def format_address(self, address):
        while ("  " in address):
            address = address.replace("  ", " ")
            
        parsed_address_street = address.split(sep='\n')
        self.street = parsed_address_street[0].strip()
        parsed_address_city = parsed_address_street[1].split(sep=',')
        self.city = parsed_address_city[0].strip()
        parsed_address_state = parsed_address_city[1].strip().split(sep=' ')
        self.state = parsed_address_state[0]
        self.zip_code = str(parsed_address_state[1])

        self.address = self.street+" "+self.city+"\n"+self.state+", "+self.zip_code

    def format_geo_coordinates(self):
        coordinates = geolocator.geocode(self.address)
        self.longitude = coordinates.longitude
        self.latitude = coordinates.latitude

    def get_street(self):
        return self.street
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def __str__(self):
        return "Name: "+self.name+"\nCategory: "+self.category+"\nPriority: "+str(self.priority)+"\nAddress:\n"+self.address



