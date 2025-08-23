class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"

# Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        if self.is_on:
            print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")
        else:
            print(f"{self.brand} {self.model} is OFF. Please power it on first.")

#Polymorphism
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")

# Test the Program
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S24", 256)
    print(phone)
    phone.power_on()

    gamer_phone = GamingPhone("Asus", "ROG Phone 7", 512, "Adreno 740")
    gamer_phone.power_on()
    gamer_phone.play_game("Genshin Impact")

    print("\n--- Polymorphism Demo ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
