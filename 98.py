#THE ENTERPRISE PAYROLL ENGINE
class employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        self._tax_rate = 0.10

    def calculate_net_pay(self):
        # net pay after tax
        return self.base_salary * (1 - self._tax_rate)


class manager(employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def calculate_net_pay(self):
        # managers get a 5000 bonus added to net pay
        standard_pay = super().calculate_net_pay()
        return standard_pay + 5000
class executive(employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
        self._tax_rate=0.20
    def calculate_net_pay(self):
        total_comp=self.base_salary+50000
        tax_decution=total_comp*self._tax_rate
        return total_comp-tax_decution
class department():
    def __init__(self,department_name):
        self.department_name=department_name
        self.staff_list=[]
    def hire_employee(self,employee):
        self.staff_list.append(employee)
        print(f"✅ Hired {employee.name} to the {self.department_name} department.")
    def run_payroll(self):
        total_company_expense=0
        print(f"🧾 ---{self.department_name} monthly payroll---")
        for staff in self.staff_list:
            net_pay = staff.calculate_net_pay()
            total_company_expense += net_pay
            print(f"{staff.name}: {net_pay}")
        print(f"💳 Total Department Payout: ₹{total_company_expense}")
if __name__ == "__main__":
    finance_dept = department("Corporate Finance")
    emp1 = employee("Kiran", 40000)      # Standard: 10% tax
    emp2 = manager("kushal", 60000)    # Manager: 10% tax + 5000 allowance
    emp3 = executive("Karthik", 100000)  # Exec: +50k bonus, then 20% tax
    
    print("\n--- Hiring Phase ---")
    finance_dept.hire_employee(emp1)
    finance_dept.hire_employee(emp2)
    finance_dept.hire_employee(emp3)
    print("\n")
    finance_dept.run_payroll()