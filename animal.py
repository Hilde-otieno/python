# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def move(self):
#         pass
#     def make_noise(self):
#         pass
#         pass
# class Cat(Animal):
#     def move(self):
#         print("The cat is walking")
#     def make_noise(self):
#         print("meow")
# class Bird(Animal):
#     def move(self):
#         print("The bird is flying")
#     def make_noise(self):
#         print("chirp")
# class Fish(Animal):
#     def move(self):
#         print("The fish is swimming")
#     def make_noise(self):
#         print("boops")

class Design:
      def __init__(self,mood,temperature):
           self.mood = mood
           self.temperature = temperature

      def check_design(self,mood,temperature):
            if temperature <= 15 and mood =="Sad":
                  return "dark ankara patterns"
            elif temperature >15 and temperature<30 and mood =="Neutal":
                  return "circular ankara patterns"
            elif temperature >30 and mood =="Happy":
                  return "vibrant ankara patterns"
            else:
                  return "Dont change the designs on he ankara"

temperature = 22
mood = "Happy"  
    