class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


# Quiz
# class Dog:
#     def __init__(self) -> None:
#         self.temperament = "loyal"
    
#     def bark(self):
#         print("Woof, woof!")
        
# class Labrador(Dog):
#     def __init__(self) -> None:
#         super().__init__()
#         self.is_a_good_boy = True
        
#     def bark(self):
#         super().bark()
#         print("Greetings, good sir. How do you do?")
        
# sparky = Labrador()
# sparky.bark()