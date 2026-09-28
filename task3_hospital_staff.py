class Staff:
    def __init__(self,name,staff_id):
        self.name = name
        self.staff_id = staff_id
    def work(self):
        print(f"Staff {self.name} is working")
class Doctor(Staff):
    def __init__(self,name,staff_id,specialization):
        super().__init__(name,staff_id)
        self.specialization = specialization
    def work(self):
        print(f"Dr. {self.name} is examining patients.")
class Nurse(Staff):
    def __init__(self,name,staff_id,ward):
        super().__init__(name,staff_id)
        self.ward = ward
    def work(self):
        print(f"Nurse {self.name} is caring for patients.")
class Receptionist(Staff):
    def __init__(self,name,staff_id,shift):
        super().__init__(name,staff_id)
        self.shift = shift
    def work(self):
        print(f"{self.name} is managing appointments.")

Doctor1 = Doctor("Sara","D001","Heart")
Nurse1 = Nurse("Ali","N001","Emergency")
Receptionist1 = Receptionist("Mia","R001","Morning")
staff_list = [Doctor1,Nurse1,Receptionist1]
for staff in staff_list:
    staff.work()