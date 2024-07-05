def calculate_salary_slip(basic_salary):
    # Calculating allowances and deductions based on percentages
    da = 0.02 * basic_salary
    ta = 0.03 * basic_salary
    hra = 0.1 * basic_salary
    pf = 0.15 * basic_salary
    
    # Calculating total salary
    total_salary = basic_salary + da + ta + hra + pf
    
    # Calculating net salary
    net_salary = total_salary - pf
    
    # Calculating bonus using shift operator (25% of salary)
    bonus = basic_salary << 2  # This is equivalent to basic_salary * 2^2
    
    # Printing the salary slip details
    print("Salary Slip")
    print("-----------")
    print(f"Basic Salary: {basic_salary}")
    print(f"Dearness Allowance (DA): {da}")
    print(f"Travel Allowance (TA): {ta}")
    print(f"House Rent Allowance (HRA): {hra}")
    print(f"Provident Fund (PF): {pf}")
    print(f"Total Salary: {total_salary}")
    print(f"Net Salary: {net_salary}")
    print(f"Bonus: {bonus}")

# Example usage:
basic_salary = float(input("Enter Basic Salary: "))
calculate_salary_slip(basic_salary)
