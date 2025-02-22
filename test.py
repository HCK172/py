#from turtle import Turtle, Screen
#phil = Turtle()
#print(phil)

#phil.shape("turtle")
#phil.color("Darkgreen")
#phil.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

#from prettytable import PrettyTable
#table = PrettyTable()



#table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
#table.add_column("Type",["Electric","Water","Fire"])
#table.align = 'l'
#print(table)
#print(type(table))

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"user.")

