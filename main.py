class ParkingLot:
    def __init__(self):
        self.lot = []
        self.details = {}

    def print_lot(self):
        return self.lot

    def print_details(self):
        return self.details

    def create_parking_lot(self, number):
        self.lot = [0 for i in range(number)]
        return f'Created parking of {number} slots'

    def park_car(self, registration_number, age):
        for i, item in enumerate(self.lot):
            if item == 0:
                self.lot[i] = registration_number
                self.details[registration_number] = {"age": age}
                return f'Car with vehicle registration number "{registration_number}" has been parked at slot number {i+1}'
        return "No Slots Available"

    def slot_numbers(self, age):
        slots = []
        for i, item in enumerate(self.lot):
            if item in self.details and age == self.details[item]["age"]:
                slots.append(i+1)
        return slots

    def slot_number(self, registration_number):
        parking_lot = self.lot
        for i, item in enumerate(parking_lot):
            if item == registration_number:
                return i+1
        return f'No vehicle Was Found in Parking Lot with Registration Number {registration_number}'

    def vacate(self, lot_number):
        if lot_number < 1:
            return "Incorrect Position To Vacate"
        lot_number -= 1
        if self.lot[lot_number]:
            registration_number = self.lot[lot_number]
            age = self.details[self.lot[lot_number]]["age"]
            del self.details[self.lot[lot_number]]
            self.lot[lot_number] = 0
            return f'Slot number {lot_number} vacated, the car with vehicle registration number "{registration_number}" left the space, the driver of the car was of age {age}'
        return "Slot already vacant"

    def vehicle_registration_age(self, age):
        registration_numbers = []
        registration_details = self.details
        for item in registration_details:
            if registration_details[item]["age"] == age:
                registration_numbers.append(item)
        return registration_numbers

    def run_file(self):
        with open("input.txt", "r") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            for line in lines:
                line_items = line.split(" ")
                if line_items[0] == "Create_parking_lot":
                    self.create_parking_lot(int(line_items[1]))
                else:
                    if not self.lot:
                        return "No Parking Lot has been Created Please Create One"
                    if line_items[0] == "Park" and line_items[2] == "driver_age":
                        print(self.park_car(line_items[1], int(line_items[3])))
                    elif line_items[0] == "Slot_numbers_for_driver_of_age":
                        print(*self.slot_numbers(int(line_items[1])), sep=",")
                    elif line_items[0] == "Slot_number_for_car_with_number":
                        print(self.slot_number(line_items[1]))
                    elif line_items[0] == "Leave":
                        print(self.vacate(int(line_items[1])))
                    elif line_items[0] == "Vehicle_registration_number_for_driver_of_age":
                        print(self.vehicle_registration_age(int(line_items[1])))


p1 = ParkingLot()
p1.run_file()
