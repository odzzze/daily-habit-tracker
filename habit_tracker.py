class Habit:
    def __init__(self, name):
        self.name = name
        self.done = False
    
    def mark_done(self):
        self.done = True
    
    def __str__(self):
        return f"{self.name} - {'Done' if self.done else 'Not done'}"


class HabitTracker:
    def __init__(self):
        self.habits = []
    
    def add_habit(self, habit_name):
        # Добавляем новую привычку
        habit = Habit(habit_name)
        self.habits.append(habit)
        print(f"Added habit: {habit_name}")
    
    def mark_done(self, habit_name):
        # Отмечаем привычку как выполненную
        for habit in self.habits:
            if habit.name == habit_name:
                habit.mark_done()
                print(f"Marked '{habit_name}' as done.")
                break
        else:
            print(f"Habit '{habit_name}' not found.")
    
    def delete_habit(self, habit_name):
        # Удаляем привычку
        for habit in self.habits:
            if habit.name == habit_name:
                self.habits.remove(habit)
                print(f"Deleted habit: {habit_name}")
                break
        else:
            print(f"Habit '{habit_name}' not found.")
    
    def list_habits(self):
        # Показываем все привычки
        if not self.habits:
            print("No habits added yet.")
        else:
            print("\nYour habits:")
            for habit in self.habits:
                print(habit)
            print("")  # Пустая строка для улучшения читаемости


# Интерфейс команд
def main():
    tracker = HabitTracker()
    print("Welcome to the Daily Habit Tracker!")
    
    while True:
        print("\nCommands:")
        print("add <habit_name>   - Add a new habit")
        print("done <habit_name>  - Mark a habit as done")
        print("delete <habit_name> - Delete a habit")
        print("list                - List all habits")
        print("exit                - Exit the application")
        
        command = input("\nEnter a command: ").strip()
        
        if command.startswith('add '):
            habit_name = command[4:].strip()
            if habit_name:
                tracker.add_habit(habit_name)
            else:
                print("Please provide a habit name.")
        
        elif command.startswith('done '):
            habit_name = command[5:].strip()
            if habit_name:
                tracker.mark_done(habit_name)
            else:
                print("Please provide a habit name.")
        
        elif command.startswith('delete '):
            habit_name = command[7:].strip()
            if habit_name:
                tracker.delete_habit(habit_name)
            else:
                print("Please provide a habit name.")
        
        elif command == 'list':
            tracker.list_habits()
        
        elif command == 'exit':
            print("Goodbye!")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
