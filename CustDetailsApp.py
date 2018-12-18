#-------------------------------------------------#
# Title: Customer Details App
# Dev:   Kanapalas
# Date:  12/17/2018
# Desc: This application manages employee data
# ChangeLog: (Who, When, What)
#-------------------------------------------------#

if __name__ == "__main__":
    import DataProcessing, Customers
else:
    raise Exception("This file was not created to be imported")

#Data
ObjCust = None
intID = 0 #an cust ID
intLastCustID = 0 #last cust ID
strFirstName = "" #cust first name
strLastName = "" #cust last name
strInput = "" #hols for user input

#Processing
#tasks fo perform
#Process new customer data that user inputs
def ProcessNewCustomerData(ID, FristName, LastName, EmailId):
    try:
        #create customer object
        ObjCust = Customers.Customer()
        ObjCust.ID = ID
        ObjCust.FirstName = FristName
        ObjCust.LastName = LastName
        ObjCust.EmailId = EmailId
        Customers.CustomerList.AddCustomer(ObjCust)
    except Exception as e: #catch all errors with exception handle
        print(e)

def SaveDatatoFile():
    try:
        ObjFile = DataProcessing.File()
        ObjFile.TextFile = "CustomerDetails.txt"
        ObjFile.TextData = Customers.CustomerList.ToString()
        print("it worked, Done!")
        ObjFile.SaveData()
    except Exception as e:
        print(e)

#I/O- Presentation

#get user input for customers details
strUserInput =""
while(True):
    strUserInput = input("Would you like to add customer data? (y/n)")
    if (strUserInput == "y"):
        #ask for emp ID
        intID = int(input("Enter the Emp ID(Last ID was " + str(intLastCustID) + "):" ))
        intLastCustID = intID
        strFirstName = str(input("Enter the first name of the customer: "))
        strLastName = str(input("Enter the last name of the customer:" ))
        strEmailId = str(input("Enter the email address of the customer:"))
        ProcessNewCustomerData(intID,strFirstName,strLastName,strEmailId)
    else:
        break

#print the output
print("The current customer data is: ")
print("=======================")
print(Customers.CustomerList.ToString())

#get user input to save the employee data
strInput = input("Would you like to save the data? (y/n):")
if(strInput == "y"):
    SaveDatatoFile()
    print("Customer Data is saved")
else:
    print("Customer Data is not saved")

print("The End! End of Module 9 :)")