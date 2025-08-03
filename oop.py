class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        if velocity < 0:
            self.velocity = 0
        elif velocity > 200:
            self.velocity = 200
        else:
            self.velocity = velocity

        consumed_fuel = distance * 10 / 100
        if consumed_fuel >= self.fuelRate:
            distance_possible = (self.fuelRate / 10) * 10 
            remain_distance = distance - distance_possible
            self.fuelRate = 0
            self.stop(remain_distance)
        else:
       
            self.fuelRate -= consumed_fuel
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Car stopped. Remaining distance: {remain_distance} km")
        else:
            print("You arrived at your destination.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)

    def send_mail(self, to, subject, body):
        print(f"Sending email to {to}:\nSubject: {subject}\nBody: {body}")


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
                print(f"Employee {emp.name} is late. Salary deducted.")
            else:
                self.reward(empId, 10)
                print(f"Employee {emp.name} is on time. Salary rewarded.")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True  
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num



#example
car1 = Car("Fiat 128", 20, 60)

samy = Employee(
    "Samy",
    500,
    "Neutral",
    100,
    1,
    car1,
    "samy@iti.com",
    3000,
    20
)

iti_office = Office("ITI Smart Village")
iti_office.hire(samy)

samy.sleep(6)
print(f"Samy's mood after sleep: {samy.mood}")

samy.eat(2)
print(f"Samy's health rate after eating: {samy.healthRate}%")

samy.buy(2)
print(f"Samy's money after buying items: {samy.money} L.E")

print("\n--- Samy is going to work ---")
samy.drive(20)

iti_office.check_lateness(1, 7.5)

print(f"\nSamy's final salary: {samy.salary} L.E")
print(f"Samy's final fuel rate: {samy.car.fuelRate}%")
print(f"Samy's final velocity: {samy.car.velocity} km/h")

