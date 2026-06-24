# 📋 Professional To-Do List Application

A powerful, feature-rich Python-based To-Do List application with advanced task management capabilities and persistent storage.

## ✨ Professional Features

✅ **Task Priorities** - High 🔴 / Medium 🟡 / Low 🟢
✅ **Categories** - Work, Personal, Shopping, Health, Custom
✅ **Due Dates** - Set deadlines for your tasks
✅ **Tags** - Organize tasks with custom tags
✅ **Task Editing** - Modify existing tasks anytime
✅ **Advanced Filtering** - View by priority, category, or overdue status
✅ **Search Functionality** - Find tasks by keyword
✅ **Statistics Dashboard** - Track progress with completion rates
✅ **Persistent Storage** - All data saved in JSON format automatically

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

## Installation & Usage

### 1. Run the Application

```bash
python main.py
```

### 2. Menu Options (11 Features)

1. **📋 View All Tasks** - Display all tasks sorted by priority and due date
2. **🎯 View Tasks by Priority** - High, Medium, Low priority filters
3. **🏷️  View Tasks by Category** - Organized by Work, Personal, Shopping, Health
4. **⏰ View Overdue Tasks** - See tasks past their due date
5. **➕ Add New Task** - Create task with priority, due date, category, tags
6. **✏️  Edit Task** - Modify existing task details
7. **✅ Mark Task as Completed** - Check off completed tasks
8. **🗑️  Delete Task** - Remove tasks permanently
9. **🔍 Search Tasks** - Find tasks by keyword
10. **📊 View Statistics** - Progress tracking with completion rates
11. **🚪 Exit** - Close the application

### 3. Example Usage

```
🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 
Welcome to Professional To-Do List Application!
🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 

======================================================================
🎯 PROFESSIONAL TO-DO LIST APPLICATION
======================================================================
1.  📋 View All Tasks
2.  🎯 View Tasks by Priority
3.  🏷️  View Tasks by Category
4.  ⏰ View Overdue Tasks
5.  ➕ Add New Task
6.  ✏️  Edit Task
7.  ✅ Mark Task as Completed
8.  🗑️  Delete Task
9.  🔍 Search Tasks
10. 📊 View Statistics
11. 🚪 Exit
======================================================================

Enter your choice (1-11): 5
======================================================================
➕ ADD NEW TASK
======================================================================
📌 Task Title: Design Homepage
📝 Description (optional): Create responsive layout for mobile and desktop
🏷️  Category (Work/Personal/Shopping/Health/Other) [Default: Personal]: Work

Priority Levels:
1 - 🔴 High   (Urgent)
2 - 🟡 Medium (Important)
3 - 🟢 Low    (Can Wait)
Priority (1/2/3) [Default: 2]: 1
📅 Due Date (YYYY-MM-DD) or press Enter to skip: 2026-07-15
🏷️  Add tags (comma-separated, optional): urgent, frontend, design

✅ Task 'Design Homepage' added successfully!
```

## Data Storage

- Tasks are automatically saved to `tasks.json` in the same directory
- Each task includes comprehensive information:
  - **Title** - Task name
  - **Description** - Detailed notes
  - **Category** - Work, Personal, Shopping, Health, Other
  - **Priority** - High (1), Medium (2), Low (3)
  - **Due Date** - Task deadline (YYYY-MM-DD)
  - **Tags** - Custom labels for organization
  - **Status** - Completed or Pending
  - **Timestamps** - Creation and completion times
  - **Unique ID** - Auto-generated identifier

## File Structure

```
To Do LIST/
├── main.py           # Main application file
├── tasks.json        # Automatically created - stores your tasks
└── README.md         # This file
```

## Advanced Features Explained

### Task Properties
- **Title**: Required - Name of the task
- **Description**: Optional - Detailed information
- **Priority**: 🔴 High (Urgent) | 🟡 Medium (Important) | 🟢 Low (Can Wait)
- **Category**: Work, Personal, Shopping, Health, or Custom
- **Due Date**: Optional deadline (YYYY-MM-DD format)
- **Tags**: Multiple keywords for better organization
- **Status**: ⭕ Pending or ✅ Completed
- **Timestamps**: Auto-tracked creation and completion

### Smart Filtering
- **By Priority** - Focus on urgent tasks first
- **By Category** - Organize work and personal tasks separately
- **Overdue Tasks** - See what needs immediate attention
- **Search** - Find tasks by title or description

### Statistics & Progress
- Total tasks count
- Completed vs. Pending
- High-priority task count
- Completion rate percentage
- Visual progress bar

## Professional Tips

- **Prioritization**: Mark urgent items as High priority to focus first
- **Categorization**: Use consistent categories (Work/Personal/Shopping) for better organization
- **Due Dates**: Set realistic deadlines to track project timelines
- **Tags**: Use tags for cross-category organization (e.g., "urgent", "client-xyz", "backend")
- **Search**: Use keywords to quickly find related tasks
- **Statistics**: Check progress regularly to stay motivated
- **Editing**: Update tasks as requirements change
- **Regular Review**: Check overdue tasks daily for accountability

## Troubleshooting

**Q: I get "Code language not supported" error when running?**
- A: Install Python extension from VS Code Extensions, or use terminal: `python main.py`

**Q: My tasks disappeared!**
- A: Make sure `tasks.json` wasn't deleted. File is created in same directory as `main.py`

**Q: Invalid date error when entering due date?**
- A: Use YYYY-MM-DD format (e.g., 2026-07-15). Leave blank to skip due date.

**Q: Search not finding tasks?**
- A: Search looks in title and description. Use exact or partial keywords.

**Q: Can't edit tasks properly?**
- A: Leave blank to keep current value, or enter new value to update.

## Professional Use Cases

- **Project Management** - Track tasks by category and priority
- **Team Collaboration** - Assign tasks with clear deadlines
- **Personal Productivity** - Organize work and life balance
- **Client Projects** - Use tags for client-specific tracking
- **Development Sprints** - Plan and track features with priorities

## Future Enhancement Ideas

Potential improvements for advanced features:
- Database support (SQLite, PostgreSQL)
- Web interface (Flask/Django)
- Mobile app
- Task dependencies & subtasks
- Recurring tasks & automation
- Multi-user support with authentication
- Task notifications & reminders
- Data export (CSV, PDF)
- Task templates
- Integration with calendars (Google Calendar, Outlook)
- Dark mode UI
- Collaborative team features

---

**Made with ❤️ for better productivity! 🚀**
