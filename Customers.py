import Persons #Imports the persond module from the same project
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class Customer(Persons.Person):

    """  Class for Cust data """

    # -------------------------------------#
    # Desc:  Hold customer details like emp id.
    # Dev:   Kanapalas
    # Date:  12/17/2018
    # ChangeLog:12/17/2018,SandeepK,added a emp details class
    # -------------------------------------#

    def __int__(self, ID = "", EmailId =""):
        self.__ID = ID
        self.__EmailId = EmailId

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, Value):
        self.__ID = Value

    @property
    def EmailId(self):
        return self.__EmailId
    @EmailId.setter
    def EmailId(self, Value):
        self.__EmailId = Value

        # --Methods--
    def ToString(self):
        # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strData = super().ToString()
        return str(self.ID) + ',' + self.EmailId + ',' + strData

    def __str__(self):
        # This overrides the original method as well
        """Implictly returns field data"""
        strData = super().__str__()
        return str(self.ID) + ',' + self.EmailId + ',' + strData
    # --End of Class --

class CustomerList(object):
    """ Static Class for Emp data """

    # -------------------------------------#
    # Desc:  Manages a list of employee data.
    # Dev:   Kanapalas
    # Date:  12/17/2018
    # ChangeLog:12/17/2018,SandeepK,added a emp details class
    # -------------------------------------#

    #Feilds
    __lstCustomers = []

    #constructor
    #def __init__(self):
        #attributes

    #properties
    #none

    #Methods
    @staticmethod
    def AddCustomer(Customer):
        print(Customer.__class__) #for testing class
        if(str(Customer.__class__) == "<class 'Customers.Customer'>"):
            CustomerList.__lstCustomers.append(Customer)
            print(CustomerList.__lstCustomers) #for testing
        else:
            raise Exception("Only Customer object can be added to this list")


    @staticmethod
    def ToString():
        # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strCustData = "ID,FirstName,LastName,EmailId\n"
        for item in CustomerList.__lstCustomers:
            strCustData += str(item.ID) + "," + item.FirstName + "," + item.LastName + "," + item.EmailId + "\n"
        return strCustData

    def __str__(self):
        # This overrides the original method
        """implictly returns field data"""
        strCustData = CustomerList.ToString()
        return strCustData