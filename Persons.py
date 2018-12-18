# Create a Customer Class that has a Customer Id, FirstName, and LastName properties by inheriting code from your Person class.
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
# --- Make the class ---
class Person(object):
    """ Base Class for Personal data """

    # -------------------------------------#
    # Desc:  Hold Persons details like first name and last name.
    # Dev:   Kanapalas
    # Date:  12/17/2018
    # ChangeLog:12/17/2018,SandeepK,added a person details class
    # -------------------------------------#

    # --Fields--
    # FirstName = ""
    # LastName = ""

    # --Constructor--
    def __init__(self, FirstName = "", LastName = ""):
        # Attributes
        self.__FirstName = FirstName
        self.__LastName = LastName

    # --Properties--
    #FristName property
    @property #(getter or accessor)
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter #(Setter or amulator)
    def FirstName(self, Value):
        self.__FirstName = Value

    #LastName property
    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, Value):
        self.__LastName = Value

    def ToString(self):
        return self.__FirstName + ","  + self.__LastName

    def __str__(self):
        return self.ToString()


# End of class
