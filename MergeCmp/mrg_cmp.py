import re
import json
import database


class Empl():
    """
    Employee class
    """

    def __init__(self, first_name, last_name, role, annual_salary, feedback, years_employed, emailAddress):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.role = str(role).upper()
        self.annual_salary = int(annual_salary)
        self.years_employed = int(years_employed)
        self.feedback = int(feedback)
        self.emailAddress = str(emailAddress)

    @classmethod
    def create_empl(cls, new_empl):
        new_empl = str(new_empl)
        firs_name, last_name, role, annual_salary, feedback, years_employed, emailAddress = new_empl.split()
        if cls.check_email(emailAddress):
            return cls(last_name, annual_salary, role, annual_salary, feedback, years_employed, emailAddress)

    @staticmethod
    def check_email(email):
        if re.match(r".+@.+\..+", email):
            return True
        else:
            return False


with open("company_employees.json")as fl:
    cmp_empl_dict = json.load(fl)
    cmp_empl_list = cmp_empl_dict["Employees"]

with open("feedback_for_employees.json")as fl:
    fdb_empl_dict = json.load(fl)
    fdb_empl_list = fdb_empl_dict["Feedback"]

final_empl = []

for c_empl in cmp_empl_list:
    if Empl.check_email(c_empl["emailAddress"]) and c_empl["years_employed"] > 2:
        emp_email = c_empl["emailAddress"]
        for f_empl in fdb_empl_list:
            if emp_email == f_empl["emailAddress"]:
                # print(c_empl["firstName"],c_empl["lastName"],f_empl["role"],
                #       c_empl["annual_salary"],c_empl["years_employed"], f_empl["feedback"], emp_email)
                empl_inst = (Empl.create_empl(f"{c_empl['firstName']} {c_empl['lastName']} {f_empl['role']} "
                                              f"{c_empl['annual_salary']} {c_empl['years_employed']} "
                                              f"{f_empl['feedback']} {emp_email}"))
                final_empl.append(empl_inst)
            else:
                continue
    else:
        continue

database.create_employee_table()

for emp in final_empl:
    # def create_employee(first_name: str, last_name: str, role: str, annual_salary: float, feedback: int, years_employed:int, email: str):
    database.create_employee(emp.first_name, emp.last_name, emp.role, emp.annual_salary, emp.feedback,
                             emp.years_employed, emp.emailAddress)

for emp in final_empl:
    database.get_employees(emp.emailAddress)
