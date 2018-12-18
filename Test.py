if __name__ == "__main__":
    import DataProcessing, Customers
else:
    raise Exception("This file was not created to be imported")

# import DataProcessing, Employees

ObjC = Customers.Customer()
ObjC.ID = 1
ObjC.FirstName = "Sam"
ObjC.LastName = "Kanaps"
ObjC.EmailId = "samk@hm.com"
strCustData = ObjC.ToString()
# print(ObjE.ToString())
print(strCustData)

Customers.CustomerList.AddCustomer(ObjC)

print(Customers.CustomerList.ToString())