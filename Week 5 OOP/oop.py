# Assignment 1: Smartphone Class with Inheritance
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def show_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"

    def charge(self):
        return f"{self.model} is charging..."

# Inheritance - Advanced Smartphone with Extra Features
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_megapixels}MP camera!"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 24)
phone2 = AdvancedSmartphone("Apple", "iPhone 13 Pro", 20, 12)

# Test Smartphone Class
print(phone1.show_specs())
print(phone2.show_specs())
print(phone2.take_photo())

print("=" * 50)

# Activity 2: Polymorphism with Animals
class Animal:
    def move(self):
        pass  # Abstract method

class Bird(Animal):
    def move(self):
        return "Flying 🕊️"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

class Dog(Animal):
    def move(self):
        return "Running 🐶"

# Creating objects for each animal
animals = [Bird(), Fish(), Dog()]

# Test Polymorphism
for animal in animals:
    print(animal.move())
