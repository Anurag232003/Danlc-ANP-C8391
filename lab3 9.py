def generate_payslip():
    # Input details
    name = input("Enter name: ")
    experience = int(input("Enter experience (in years): "))
    basic_salary = float(input("Enter basic salary: "))

    # Calculate allowances and deductions
    da = 0.05 * basic_salary
    ta = 0.065 * basic_salary
    cca = 0.08 * basic_salary
    hra = 0.1 * basic_salary
    pf = 0.125 * basic_salary

    # Calculate bonus based on experience
    if experience > 25:
        bonus = 0.25 * basic_salary
    elif experience > 20:
        bonus = 0.2 * basic_salary
    elif experience > 15:
        bonus = 0.15 * basic_salary
    else:
        bonus = 0.1 * basic_salary

    # Calculate total and net salary
    total_salary = basic_salary + da + ta + cca + hra + bonus
    net_salary = total_salary - pf

    # Print payslip
    print("\n" + "-"*100)
    print(" " * 52 + "Pay Slip")
    print("-" * 100)
    print(f"Name: {name}")
    print(f"Experience: {experience} years")
    print(f"Basic Salary: {basic_salary:.2f}")
    print("-" * 100)
    print(f"DA: {da:.2f}")
    print(f"TA: {ta:.2f}")
    print(f"CCA: {cca:.2f}")
    print(f"HRA: {hra:.2f}")
    print(f"PF: {pf:.2f}")
    print(f"BONUS: {bonus:.2f}")
    print(f"TOTAL SALARY: {total_salary:.2f}")
    print(f"NET SALARY: {net_salary:.2f}")
    print("-" * 100)

# Run the function
generate_payslip()

