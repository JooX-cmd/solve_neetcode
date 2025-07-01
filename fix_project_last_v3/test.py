class Employee:
    def __init__(self, name, age, job, id, phone, bank_account, hours_worked=160, hour_rate=19):
        self.name = name
        self.age = age
        self.job = job
        self.id = id
        self.phone = phone
        self.bank_account = bank_account
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        Employee.all_employee.append(self)

    @property
    def hours_worked(self):
        