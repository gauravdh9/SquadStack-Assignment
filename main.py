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
        return "Parking Lot Created"

    def park_car(self, registration_number, age):
        for i, item in enumerate(self.lot):
            if item == 0:
                self.lot[i] = registration_number
                self.details[registration_number] = {"age": age}
                return f"Park car with vehicle registration number “{registration_number}”,\
                and the car is driven by the driver of age {age}"
        return "No Slots Available"

    # def custom(self, item, age):
    #     print(item)
    #     if item[1] in self.details and self.details[item[1]]["age"] == age:
    #         return item[0]+1
    #     return False

    def slot_numbers(self, age):
        slots = []
        for i, item in enumerate(self.lot):
            if item in self.details and age == self.details[item]["age"]:
                slots.append(i+1)
        return slots

    def slot_number(self, registration_number):
        for i, item in enumerate(self.lot):
            print(item)
            if item == registration_number:
                return i+1
        return f'No vehicle Was Found in Parking Lot with Registration Number {registration_number}'

    def vacate(self, lot_number=2):
        if self.lot[lot_number]:
            del self.details[self.lot[lot_number]]
            self.lot[lot_number] = 0
            return f'Car which was parked at slot number {lot_number} has left the space'
        return "Slot already vacant"

    def accept_commands(self):
        while True:
            print("List of Commands")
            print("1. Create_parking_lot `lot_number`(capacity)")
            print("2. Park `registration number` drive age `age`(age)")
            print("3. Slot_numbers_for_driver_of_age `age`(age)")
            print("1. Create_parking_lot `lot_number`(capacity)")
            print("1. Create_parking_lot `lot_number`(capacity)")


p1 = ParkingLot()


print(p1.create_parking_lot(6))
print(p1.park_car("PB-01-TG-2341", 40))
print(p1.print_lot())
print(p1.print_details())
print(p1.park_car("KA-90-YU-2342", 29))
print(p1.print_lot())
print(p1.print_details())
print(p1.park_car("GA-50-IO-5687", 35))
print(p1.print_lot())
print(p1.print_details())
print(p1.park_car("ER-23-KJ-9898", 45))
print(p1.print_lot())
print(p1.print_details())
print(p1.park_car("LI-90-NI-4562", 23))
print(p1.print_lot())
print(p1.print_details())
# print(p1.park_car("XC-23-NJ-1010", 27))
# print(p1.print_lot())
# print(p1.print_details())
# print(p1.park_car("ZV-77-DF-8723", 56))
# print(p1.print_lot())
# print(p1.print_details())


print(p1.slot_numbers(age=23), "number")

print(p1.slot_number("LI-90-NI-4562"))
print(p1.vacate(2))
print(p1.print_lot())
print(p1.print_details())
print(p1.vacate(2))
print(p1.print_lot())
print(p1.print_details())
