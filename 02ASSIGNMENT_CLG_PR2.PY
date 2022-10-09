'''Q. B) Consider the basic pay of an employee as user input. AGP is 50% of the
basic pay. Company provides 50% DA and 15% HRA on the merged basic.
Write a python program to calculate and display total salary of the
employee.

Note: The value of basic pay can be integer or float
Total Salary=basic + AGP + DA + TA
i.e. Total Salary=basic + (basic*50%) + ((basic+agp)*50%) +
((basic+agp)**15%)

Output:
Enter the basic pay drawn by the employee:
Total salary drawn by the employee = <value up to 2 decimal points>'''

basic=eval(input("Enter the basic pay drawn by the employee :"))
 
agp=basic*0.5 
merged=agp+basic 
da=0.5*merged 
hra=0.15*merged 

total=merged+da+hra 

print("Total salary drawn by the employee:","%0.2f"% total)