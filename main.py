import json
import os
from datetime import datetime
from typing import List, Dict
import re

# File to store tasks
TASKS_FILE = "tasks.json"

# Priority levels
PRIORITY_LEVELS = {
    "1": "🔴 High",
    "2": "🟡 Medium", 
    "3": "🟢 Low"
}

PRIORITY_VALUES = {
    "high": "1",
    "medium": "2",
    "low": "3"
}


class TodoApp:
    """Professional To-Do List Application"""
    
    def __init__(self):
        self.tasks: List[Dict] = self.load_tasks()
    
    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file."""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self):
        """Add a new task with details."""
        print("\n" + "="*70)
        print("➕ ADD NEW TASK")
        print("="*70)
        
        title = input("📌 Task Title: ").strip()
        if not title:
            print("❌ Task title cannot be empty!\n")
            return
        
        description = input("📝 Description (optional): ").strip()
        
        category = input("🏷️  Category (Work/Personal/Shopping/Health/Other) [Default: Personal]: ").strip()
        if not category or category.lower() not in ["work", "personal", "shopping", "health", "other"]:
            category = "Personal"
        else:
            category = category.capitalize()
        
        print("\nPriority Levels:")
        print("1 - 🔴 High   (Urgent)")
        print("2 - 🟡 Medium (Important)")
        print("3 - 🟢 Low    (Can Wait)")
        priority = input("Priority (1/2/3) [Default: 2]: ").strip()
        if priority not in ["1", "2", "3"]:
            priority = "2"
        
        due_date = input("📅 Due Date (YYYY-MM-DD) or press Enter to skip: ").strip()
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format! Skipping due date.\n")
                due_date = None
        else:
            due_date = None
        
        task = {
            "id": int(datetime.now().timestamp() * 1000),
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_date": None,
            "tags": []
        }
        
        tags_input = input("🏷️  Add tags (comma-separated, optional): ").strip()
        if tags_input:
            task["tags"] = [tag.strip() for tag in tags_input.split(",")]
        
        self.tasks.append(task)
        self.save_tasks()
        print(f"\n✅ Task '{title}' added successfully!\n")
    
    def display_tasks(self, tasks: List[Dict] = None, show_all: bool = True):
        """Display tasks with professional formatting."""
        if tasks is None:
            tasks = self.tasks
        
        if not tasks:
            print("\n📋 No tasks to display!\n")
            return
        
        # Sort by priority, then by due date
        sorted_tasks = sorted(tasks, key=lambda x: (x["priority"], x["due_date"] or "9999-12-31"))
        
        print("\n" + "="*90)
        print("📋 TASK LIST")
        print("="*90)
        print(f"{'#':<3} {'Status':<8} {'Priority':<12} {'Title':<20} {'Category':<12} {'Due Date':<12}")
        print("-"*90)
        
        for i, task in enumerate(sorted_tasks, 1):
            status = "✅" if task["completed"] else "⭕"
            priority_display = PRIORITY_LEVELS[task["priority"]]
            due_date = task["due_date"] or "No date"
            title = task["title"][:18] + "..." if len(task["title"]) > 18 else task["title"]
            category = task["category"][:10]
            
            print(f"{i:<3} {status:<8} {priority_display:<12} {title:<20} {category:<12} {due_date:<12}")
            
            if task["description"]:
                print(f"    📝 {task['description']}")
            if task["tags"]:
                print(f"    🏷️  Tags: {', '.join(task['tags'])}")
            print()
        
        print("="*90 + "\n")
    
    def view_by_priority(self):
        """View tasks filtered by priority."""
        print("\n" + "="*70)
        print("🎯 TASKS BY PRIORITY")
        print("="*70)
        
        for priority_key, priority_label in PRIORITY_LEVELS.items():
            filtered = [t for t in self.tasks if t["priority"] == priority_key and not t["completed"]]
            
            if filtered:
                print(f"\n{priority_label}:")
                print("-" * 50)
                for task in filtered:
                    due = f" (Due: {task['due_date']})" if task["due_date"] else ""
                    print(f"  • {task['title']}{due}")
                    if task["description"]:
                        print(f"    → {task['description']}")
        
        print("\n" + "="*70 + "\n")
    
    def view_by_category(self):
        """View tasks filtered by category."""
        print("\n" + "="*70)
        print("🏷️  TASKS BY CATEGORY")
        print("="*70)
        
        categories = set(t["category"] for t in self.tasks)
        
        for category in sorted(categories):
            filtered = [t for t in self.tasks if t["category"] == category and not t["completed"]]
            
            if filtered:
                print(f"\n📂 {category}:")
                print("-" * 50)
                for task in filtered:
                    print(f"  {PRIORITY_LEVELS[task['priority']]} {task['title']}")
        
        print("\n" + "="*70 + "\n")
    
    def view_overdue_tasks(self):
        """View overdue tasks."""
        today = datetime.now().strftime("%Y-%m-%d")
        overdue = [t for t in self.tasks if t["due_date"] and t["due_date"] < today and not t["completed"]]
        
        if not overdue:
            print("\n✅ No overdue tasks! You're all caught up!\n")
            return
        
        print("\n" + "="*70)
        print("⏰ OVERDUE TASKS")
        print("="*70)
        
        for task in overdue:
            days_overdue = (datetime.now() - datetime.strptime(task["due_date"], "%Y-%m-%d")).days
            print(f"\n{PRIORITY_LEVELS[task['priority']]} {task['title']}")
            print(f"   📅 Overdue by {days_overdue} days (Due: {task['due_date']})")
            print(f"   📂 Category: {task['category']}")
            if task["description"]:
                print(f"   📝 {task['description']}")
        
        print("\n" + "="*70 + "\n")
    
    def complete_task(self):
        """Mark a task as completed."""
        if not self.tasks:
            print("\n❌ No tasks to complete!\n")
            return
        
        pending = [t for t in self.tasks if not t["completed"]]
        if not pending:
            print("\n✅ All tasks completed! Great work!\n")
            return
        
        self.display_tasks(pending)
        
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            if 0 < task_num <= len(pending):
                task = pending[task_num - 1]
                task["completed"] = True
                task["completed_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"\n✅ Task '{task['title']}' marked as completed!\n")
            else:
                print("\n❌ Invalid task number!\n")
        except ValueError:
            print("\n❌ Please enter a valid number!\n")
    
    def delete_task(self):
        """Delete a task."""
        if not self.tasks:
            print("\n❌ No tasks to delete!\n")
            return
        
        self.display_tasks()
        
        try:
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(self.tasks):
                deleted = self.tasks.pop(task_num - 1)
                self.save_tasks()
                print(f"\n✅ Task '{deleted['title']}' deleted successfully!\n")
            else:
                print("\n❌ Invalid task number!\n")
        except ValueError:
            print("\n❌ Please enter a valid number!\n")
    
    def search_tasks(self):
        """Search tasks by keyword."""
        keyword = input("\n🔍 Enter search keyword: ").strip().lower()
        
        if not keyword:
            print("❌ Search keyword cannot be empty!\n")
            return
        
        results = [t for t in self.tasks if keyword in t["title"].lower() or keyword in t["description"].lower()]
        
        if not results:
            print(f"\n❌ No tasks found matching '{keyword}'!\n")
            return
        
        print(f"\n✅ Found {len(results)} task(s):")
        self.display_tasks(results)
    
    def show_statistics(self):
        """Show task statistics."""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        pending = total - completed
        high_priority = len([t for t in self.tasks if t["priority"] == "1" and not t["completed"]])
        
        print("\n" + "="*70)
        print("📊 TASK STATISTICS")
        print("="*70)
        print(f"📈 Total Tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⭕ Pending: {pending}")
        print(f"🔴 High Priority (Urgent): {high_priority}")
        
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"📊 Completion Rate: {completion_rate:.1f}%")
            print("\n" + create_progress_bar(completion_rate))
        
        print("="*70 + "\n")
    
    def edit_task(self):
        """Edit an existing task."""
        if not self.tasks:
            print("\n❌ No tasks to edit!\n")
            return
        
        self.display_tasks()
        
        try:
            task_num = int(input("Enter task number to edit: "))
            if 0 < task_num <= len(self.tasks):
                task = self.tasks[task_num - 1]
                
                print(f"\n✏️ Editing: {task['title']}")
                print("Leave blank to keep current value\n")
                
                new_title = input(f"Title [{task['title']}]: ").strip()
                if new_title:
                    task["title"] = new_title
                
                new_desc = input(f"Description [{task['description']}]: ").strip()
                if new_desc:
                    task["description"] = new_desc
                
                new_priority = input(f"Priority [1={task['priority']}]: ").strip()
                if new_priority in ["1", "2", "3"]:
                    task["priority"] = new_priority
                
                new_due = input(f"Due Date [{task['due_date']}]: ").strip()
                if new_due:
                    try:
                        datetime.strptime(new_due, "%Y-%m-%d")
                        task["due_date"] = new_due
                    except ValueError:
                        print("Invalid date format!")
                
                self.save_tasks()
                print(f"\n✅ Task updated successfully!\n")
            else:
                print("\n❌ Invalid task number!\n")
        except ValueError:
            print("\n❌ Please enter a valid number!\n")
    
    def show_menu(self):
        """Display the main menu."""
        print("\n" + "="*70)
        print("🎯 PROFESSIONAL TO-DO LIST APPLICATION")
        print("="*70)
        print("1.  📋 View All Tasks")
        print("2.  🎯 View Tasks by Priority")
        print("3.  🏷️  View Tasks by Category")
        print("4.  ⏰ View Overdue Tasks")
        print("5.  ➕ Add New Task")
        print("6.  ✏️  Edit Task")
        print("7.  ✅ Mark Task as Completed")
        print("8.  🗑️  Delete Task")
        print("9.  🔍 Search Tasks")
        print("10. 📊 View Statistics")
        print("11. 🚪 Exit")
        print("="*70)
    
    def run(self):
        """Main application loop."""
        print("\n" + "🎉 "*10)
        print("Welcome to Professional To-Do List Application!")
        print("🎉 "*10 + "\n")
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-11): ").strip()
            
            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.view_by_priority()
            elif choice == '3':
                self.view_by_category()
            elif choice == '4':
                self.view_overdue_tasks()
            elif choice == '5':
                self.add_task()
            elif choice == '6':
                self.edit_task()
            elif choice == '7':
                self.complete_task()
            elif choice == '8':
                self.delete_task()
            elif choice == '9':
                self.search_tasks()
            elif choice == '10':
                self.show_statistics()
            elif choice == '11':
                print("\n👋 Thank you for using Professional To-Do List. Goodbye!\n")
                break
            else:
                print("\n❌ Invalid choice! Please enter a number between 1-11.\n")


def create_progress_bar(percentage: float, width: int = 40) -> str:
    """Create a visual progress bar."""
    filled = int(width * percentage / 100)
    bar = "█" * filled + "░" * (width - filled)
    return f"Progress: [{bar}] {percentage:.1f}%"


if __name__ == "__main__":
    app = TodoApp()
    app.run()
