# Acadsmate v1 - Study Tracker

print("Welcome to Acadsmate 📚")

subjects = {}

while True:
    subject = input("\nEnter subject name (or type 'done' to finish): ")
    
    if subject.lower() == 'done':
        break
    
    try:
        hours = float(input(f"How many hours did you study {subject}? "))
        
        if subject in subjects:
            subjects[subject] += hours
        else:
            subjects[subject] = hours
            
    except ValueError:
        print("Please enter a valid number.")

print("\n📊 Study Summary:")
total = 0

for subject, hours in subjects.items():
    print(f"- {subject}: {hours} hours")
    total += hours

print(f"\nTotal study time: {total} hours")
print("\nStay consistent. 🚀")
