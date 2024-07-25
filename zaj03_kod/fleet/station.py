class Station:
    __max_id = 0
    __station_id = 100

    def __init__(self, location, ambulance, driver, employee):
        self.id = Station.__max_id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        self.id = Station.__station_id
        Station.__station_id += 1
        Station.__max_id += 1

    def check_location(self):
        
        if self.location == self.ambulance.location:
            print("Ambulance is in the station")
        else:
            print("Ambulance is somewhere else")