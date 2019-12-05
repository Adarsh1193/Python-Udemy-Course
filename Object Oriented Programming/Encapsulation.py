class Myclass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(5)
# Cannot access hidden variable outside the class
# print(objectone.__hiddenvariable)

