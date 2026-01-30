# Q1

grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()

print(f"Sorted grades: {grades}")
print(f"Highest grade: {grades[-1]}")
print(f"Slowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")

#Q2

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")

milk_position = cart.index("milk")
print(f"Position of milk: {milk_position}")

cart.remove("apple") # using remove

removed_item = cart.pop()
print(f"Removed item using pop:  {removed_item}") # removes last item

print("Is banana in the cart? ", "banana" in cart)


# Q3

point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

print(f"X1 = {x1}, Y1 = {y1}")
print(f"X2 = {x2}, Y1 = {y2}")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance between points: ", distance)

# Q4

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")

print(f"Attended both classes: {monday_class & wednesday_class}") 
print(f"Attended either classes: {monday_class | wednesday_class}")
print(f"Only monday: {monday_class - wednesday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}")

allStudents = monday_class | wednesday_class
print("Is monday subset of all students? ", monday_class <= allStudents)


# Q5: dictionaries

print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

contacts = {
    "Alice": "555=1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"lice's number: {contacts['Alice']}")
contacts["Diana"] = "555-4321"

print(f"Contacts after adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")

del contacts["Charlie"]
print(f"Contacts aftter deleting Charlie: {contacts}")


print(f"All names {contacts.keys()}")
print(f"All numbers {contacts.values}")
print(f"Total contacts {len(contacts)}")

