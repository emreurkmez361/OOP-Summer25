class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"Animal: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"


cat = Animal("Cat", "Mammals", 4, ["climbing", "hunting", "jumping"])
dog = Animal("Dog", "Mammals", 4, ["running", "swimming", "fetching"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "hunting"])
fish = Animal("Fish", "Aquatic", 0, ["swimming", "breathing underwater"])
snake = Animal("Snake", "Reptiles", 0, ["slithering", "hunting"])


print(cat)
print(dog)
print(eagle)
print(fish)
print(snake)
