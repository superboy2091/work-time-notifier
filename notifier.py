import time
from win10toast import ToastNotifier

# Define the schedule
schedule = [
    {'activity': 'Work', 'duration': 30},
    {'activity': 'Break', 'duration': 5},
    {'activity': 'Time for bid', 'duration': 10},
    {'activity': 'Language Study', 'duration': 10},
    {'activity': 'Break', 'duration': 5}
]

# Define the total work hours
total_hours = 12

# Define the start time
start_time = time.time()

# Initialize the ToastNotifier object
toaster = ToastNotifier()

# Loop through the schedule for the total work hours
for i in range(total_hours * 2):
    # Get the current activity and duration
    current_activity = schedule[i % len(schedule)]['activity']
    current_duration = schedule[i % len(schedule)]['duration']
    
    # Print the current activity and duration
    print(f'{current_activity} for {current_duration} minutes')
    
    # Show a Windows notification for the current activity
    toaster.show_toast(
        title='Activity',
        msg=f'{current_activity} for {current_duration} minutes',
        duration=10
    )
    
    # Wait for the duration
    time.sleep(current_duration * 60)
