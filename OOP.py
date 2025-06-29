import csv

class Employee:
    compnay = "joox"
    all_employees = []
    def __init__(self, nqme, age, job, id, phone, bank_account, h_worked, h_rate):
        self.name = __name__
        self.age = age
        self.job = job 
        self.h_worked = h_worked
        self.__h_rate = h_rate
        self.phone = phone
        self.bank_acc = bank_account
        Employee.all_employees.append(self)# add id for every emp


        def calc_salary(self, h_worked, h_rate):
            return(h_worked * h_rate)
        
        def __calc_monthly_deduction(self, salary ):
            tax = Employee.calc_tax(salary)
            health_insurance = 100
            retirement_contribution = 0.05 * salary
            total = tax + health_insurance + retirement_contribution
            return total
        
        def calc_net_salary(self, h_worked, h_rate):
            gross_salary = self.clac_gross_salary(h_rate, h_worked)
        def __str__(): #dunder method  user level
            pass
        def __repr__(self): #  magic dev level 
            ...
        
        @staticmethod  # check method
        def is_valid_phone( phone):
            return phone.satrtswith("+20") and len(phone) == 12

        @staticmethod
        def calc_tax(salary):
            if salary < 30000:



        @classmethod

        