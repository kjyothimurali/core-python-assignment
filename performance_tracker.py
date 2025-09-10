# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)

#track performance of student
def track_performance(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(calculate_average(marks), 2)  # rounded to 2 decimals
    
    #find top performer
    top_performer = max(averages, key=averages.get)
    return averages, top_performer



students = {}
num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    name = input("Enter student name: ")
    marks = list(map(int, input(f"Enter marks for {name} : ").split(",")))
    students[name] = marks

# Call function
averages, top = track_performance(students)

#output
print("\nAverage Marks:", averages)
print("Top Performer:", top)
