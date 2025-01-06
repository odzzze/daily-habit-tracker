# System Design for Daily Habit Tracker

## Introduction
The Daily Habit Tracker is a simple CLI application to track and manage daily habits. It allows users to add, remove, list, and mark their habits as completed. The application consists of two main classes: `Habit` and `HabitTracker`.

## Class Descriptions

### 1. Habit Class
The `Habit` class represents a single habit.

#### Attributes:
- `name`: (str) The name of the habit (e.g., "Exercise").
- `status`: (bool) The status of the habit, either completed (`True`) or not completed (`False`).
- `reminder_time`: (str) The time when the user wants to be reminded about this habit (e.g., "08:00").

#### Methods:
- `add()`: Adds a new habit to the habit tracker.
- `remove()`: Removes the habit from the habit tracker.
- `update()`: Updates the habit's information (e.g., change reminder time).
- `display()`: Displays the habit's details (name, status, reminder time).

### 2. HabitTracker Class
The `HabitTracker` class manages the list of habits and operations on them.

#### Attributes:
- `habit_list`: (list) A list of `Habit` objects.

#### Methods:
- `add_habit()`: Adds a new `Habit` to `habit_list`.
- `remove_habit()`: Removes a `Habit` from `habit_list`.
- `list_habits()`: Displays all habits in the `habit_list`.
- `mark_done()`: Marks a habit as completed.

## Class Interaction
The `HabitTracker` class manages a list of `Habit` objects. Each `Habit` has attributes like name, status, and reminder time. The `HabitTracker` provides methods for adding, removing, listing, and updating habits, while `Habit` provides the details of each habit and the ability to update or display them.

1. The user can create a `Habit` using the `Habit` class and add it to the `HabitTracker` using `HabitTracker.add_habit()`.
2. The user can list all habits using `HabitTracker.list_habits()`.
3. The user can mark a habit as completed using `HabitTracker.mark_done()`.

## User Interface
The program works through a simple Command Line Interface (CLI) where the user can input the following commands:

- `add`: Adds a new habit.
- `remove`: Removes an existing habit.
- `list`: Lists all habits.
- `done`: Marks a habit as completed.

The user interacts with the application by typing commands, which are processed by the `main.py` file.

## Conclusion
This design outlines the basic structure of the Daily Habit Tracker application. The system is simple, with only two classes interacting with each other. The user interface is based on basic CLI commands, making it easy for the user to interact with the program.
