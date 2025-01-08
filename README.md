
# Daily Habit Tracker  

## Description  
Welcome to Daily Habit Tracker! 🎯 This is a simple, no-fuss CLI application we built to help you stay on top of your daily habits. Whether it’s exercising, reading, or just remembering to drink water, this app has got you covered. It’s lightweight, quick to use, and perfect for people who don’t want complicated tools.  

## Installation Instructions  
Setting it up is super easy:  
1. First, clone the repo:  
   ```bash
   git clone https://github.com/your_username/habit-tracker.git
   ```  
2. Jump into the project directory:  
   ```bash
   cd habit-tracker
   ```  
3. Install the dependencies (we only need one, so it’s quick):  
   ```bash
   pip install -r requirements.txt
   ```  
4. Run the app and start tracking:  
   ```bash
   python habit_tracker.py
   ```  

That’s it. No rocket science here. 🚀  

## Usage Guide  
Here’s how you can use the app (it’s really simple):  
- `add <habit_name>`: Adds a new habit to your list.  
- `done <habit_name>`: Marks a habit as done for the day.  
- `delete <habit_name>`: Deletes a habit you no longer need to track.  
- `list`: Shows all your habits with their statuses (green = done, red = not done).  
- `exit`: Closes the app when you’re done.  

### Example:  
```bash
> add Drink Water  
Added habit: Drink Water  

> done Drink Water  
Marked 'Drink Water' as done.  

> list  
Your habits:  
Drink Water - ✅ Done  

> exit  
Goodbye! 👋  
```  

## Technical Stack  
We kept it simple because, honestly, that’s all you need:  
- **Python**: Because it’s great for projects like this.  
- **termcolor**: To make things look a little nicer with colors.  

## Features  
- Add, track, and delete your habits.  
- Colored status to make it obvious which habits are done (green) and which aren’t (red).  
- No fluff, just functionality.  

## Team Members  
We’re a small but mighty team:  
- **Azat**: The fearless team leader who kept us on track.  
- **Ibragim**: Tested everything like a pro and caught the sneaky bugs.  
- **Said**: Wrote this documentation and helped make the app shine.  

## Screenshots/Demo  
(We’ll add screenshots here soon. Imagine something awesome for now!)  

---

### Final Words  
We had fun building this project, and we hope it’s just as fun for you to use. If you spot anything weird or have ideas for improvements, let us know (or better yet, contribute to the code)! Happy habit tracking!  
