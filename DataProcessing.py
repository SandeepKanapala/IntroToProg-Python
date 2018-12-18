if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class File(object):
    def __init__(self, TextFile = "SavedText", TextData = ""):
        self.__TextFile = TextFile
        self.__TextData = TextData

    @property
    def TextFile(self):
        return self.__TextFile
    @TextFile.setter
    def TextFile(self, TextFileValue):
        self.__TextFile = TextFileValue

    @property
    def TextData(self):
        return self.__TextData
    @TextData.setter
    def TextData(self, TextDataValue):
        self.__TextData = TextDataValue

    def SaveData(self):
        try:
            ObjF = open(self.TextFile, 'a')
            ObjF.write(self.TextData)
            ObjF.close()
        except Exception as e:
            print("Python reported th following error:", + str(e))
        return "Data Saved"
    def GetData(self):
        try:
            ObjF = open(self.TextData, 'r')
            ObjF.read(self.TextData)
            ObjF.close()
        except Exception as e:
            print("Python reported following error:", + str(e))
    def ToString(self):
        return self.SaveData + "," + self.TextData
    def __str__(self):
        return ToString()
    
