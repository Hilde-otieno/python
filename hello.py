def hello():
    print("Hello  Akirachix")
def hello(name):
        print(f" Hello {name}")
def year_of_birth(name, age):
     print(f"Hello {name}, you were just born in {2024-age}")
def study(school):
    print(f" I am in {school} school")
def town(name):
    print(f" I come from {name} center")
def date_of_birth(name, age):
    print(f" Hello {name}, you  were born in {2024-age}")
def my_country(country = "Uganda"):
    print(f" Hello AkiraChix from {country}")
def greet(*names):
    for name in names:
     print(f" Hello {name}")
def create_sentence(**words):
    print(words)
    sentence = ""
    for word in words.values():
        sentence+= word
        sentence+= " "
        return sentence

