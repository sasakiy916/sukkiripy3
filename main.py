class Main:
    print()
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def introduceName(self):
        print(f"私の名前は{self.name}です")
    def introduceAge(self):
        print(f"私の年齢は{self.age}です")
