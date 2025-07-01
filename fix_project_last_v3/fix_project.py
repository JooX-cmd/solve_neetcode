import csv

class Employee:
    company = "joox"
    all_employee = []

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

    @property  # why  i make property  for  privite attrubute  and for  change value   and validation
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, new_hours):
        if isinstance(new_hours, int) and new_hours > 0:
            self.__hours_worked = new_hours
        else:
            raise ValueError("Hours must be a positive integer!")

    @property
    def phone(self):
        return self.__phone

    @phone.setter # just for check valid phone or not ? 
    def phone(self, new_phone):
        if Employee.is_valid_phone(new_phone):
            self.__phone = new_phone
        else:
            print("Invalid phone number format")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str) and value.isdigit() and value.strip(): # here  i make this to check 3 thinks 1 string   , number  , not empty 
            self.__id = value
        else:
            raise ValueError("ID should be non-empty string composed only of digits")  # raise for  error or    follow the conditon    

    def calc_gross_salary(self):
        return self.__hours_worked * self.hour_rate
    
    def calc_net_salary(self):
        gross_salary = self.calc_gross_salary
        return finace.calc_net_salary(gross_salary)
    
    def update_work_detalis(self, new_hours, new_rate):
        self.hours_worked  = new_hours
        self.hour_rate = new_rate
# privite method 


    def get_bank_account(self, provided_id):
        if self.__id == provided_id:
            return self.__bank_account[-3:]
        else:
            return "You are not allowed to view the bank account number"

    def __str__(self):
        return f"{self.name} is {self.age} years old, and works as {self.job}."

    def __repr__(self):
        return f"Employee name = {self.name}, age = {self.age}, job = {self.job}"
    
    def __dir__(self):
        pass




    @staticmethod
    def is_valid_phone(phone):
        return phone.startswith("+20") and len(phone) == 12





    # @classmethod
    # def read_csv_data(cls, file_name):
    #     with open(file_name, 'r') as file:
    #         csv_reader = csv.DictReader(file)
    #         for row in csv_reader:
    #             name = row["name"]
    #             age = int(row["age"])
    #             job = row["job_title"]
    #             id = row["id"]
    #             phone = row["phone"]
    #             bank_account = row["bank_account"]
    #             hours_worked = int(row["hours_worked"])
    #             hour_rate = int(row["hour_rate"])
    #             cls(name, age, job, id, phone, bank_account, hours_worked, hour_rate)







# this part i must desine befor i start code   now let's make method  in other  class for every function 


class finace:  # الماليات 
    # make it varable   best prac
    #chanc without function


    TAX_THRESHOLD = 10000
    TAX_LOW = 0.1
    TAX_HIGH = 0.3
    health_insurance_cost = 100
    retirement_contribution = 0.05
    @staticmethod
    def calc_tax(salary):
        if salary < finace.TAX_THRESHOLD :
            return salary * finace.TAX_LOW   #.> make it varable
        else:
            return salary * finace.TAX_HIGH
        


    def calc_net_salary(self):
        tax = finace.calc_tax(gross_salary)
        retirement_contribution =  finace.retirement_contribution* gross_salary
        total_deduction = tax + finace.health_insurance_cost  + retirement_contribution
        gross_salary = self.calc_gross_salary()
        deductions = self.__calc_monthly_deduction(gross_salary)
        net_salary = gross_salary - deductions
        return net_salary