
try:
    # Function is used to input Employee Information
    def add_employee():
        
        # Takes information about the employee and insert into the file
        while True: 
            name=str(input("Employee Name or no data to exit: "))
            if len(name)==0:
                break
                
            id=input("Employee ID: ")
            salary=input("Employee Salary: ") 
            if len(salary)==0:
                break
            else:   
                salary=int(salary)
                
            with open("employees.txt", "a") as f:
                f.write(f"{name} | {id} | {salary} \n")
            print("Employee added sucessfully")   
          

    # Function is used to read Employee Information from file
    def read_employee_information():
        employee = []
        with open ("employees.txt","r") as emp:
            for line in emp:
                employee.append(line.strip())               
        return employee        
        

    # Function is used to display Employee Information
    def view_employees(employee):                       
        j=1
        for i in employee:
            if not i.strip():
                continue
                
            emp=i.strip().split("|") 
            name=emp[0].strip()
            id=emp[1].strip() 
            sal=emp[2].strip()
            
              
            print(f"Employee - {j}\n") 
            print(f"Employee Name: {name.title()}")
            print(f"ID: {id}")
            print(f"Salary: {sal} \n")
            print("-------------------")
            j=j+1
           
                        
    add_employee()  
    employee=read_employee_information()
    if employee:
        view_employees(employee)
        print("\nEmployee information added and display successfully.\n")
    else:
        print("\nNo employee information available.\n")
    

except ValueError:
    print("\nInvalid number. Input only number.\n")
except FileNotFoundError:
    print("\nFile not found.\n") 
except Exception as e:
    print(f"Invalid something: {e}")     
   
        
    
