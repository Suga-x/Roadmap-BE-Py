
"""
Task Tracker CLI
A simple command-line application to track tasks with JSON storage
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional


class TaskTracker:
    """Main class to handle task tracking operations"""
    
    def __init__(self, data_file: str = "tasks.json"):
        """Initialize the task tracker with data file"""
        self.data_file = data_file
        self.tasks = self._load_tasks()
        self.next_id = self._get_next_id()
    
    def _load_tasks(self) -> List[Dict[str, Any]]:
        """Load tasks from JSON file, create file if it doesn't exist"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            else:
                # Create empty JSON file
                with open(self.data_file, 'w') as f:
                    json.dump([], f)
                return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            return []
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def _get_next_id(self) -> int:
        """Get the next available task ID"""
        if not self.tasks:
            return 1
        return max(task.get('id', 0) for task in self.tasks) + 1
    
    def _find_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        """Find a task by its ID"""
        for task in self.tasks:
            if task.get('id') == task_id:
                return task
        return None
    
    def _print_task(self, task: Dict[str, Any]) -> None:
        """Print a single task in a formatted way"""
        status_icons = {
            'todo': '○',
            'in-progress': '▶',
            'done': '✓'
        }
        
        status = task.get('status', 'todo')
        icon = status_icons.get(status, '○')
        
        print(f"{icon} ID: {task['id']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {status.replace('-', ' ').title()}")
        print(f"  Created: {task.get('created_at', 'N/A')}")
        if task.get('updated_at'):
            print(f"  Updated: {task['updated_at']}")
        print("-" * 40)
    
    def add(self, description: str) -> None:
        """Add a new task"""
        if not description:
            print("Error: Task description cannot be empty")
            return
        
        task = {
            'id': self.next_id,
            'description': description,
            'status': 'todo',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': None
        }
        
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added successfully (ID: {self.next_id})")
        self.next_id += 1
    
    def update(self, task_id: int, new_description: str) -> None:
        """Update an existing task"""
        if not new_description:
            print("Error: Task description cannot be empty")
            return
        
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return
        
        task['description'] = new_description
        task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_tasks()
        print(f"Task {task_id} updated successfully")
    
    def delete(self, task_id: int) -> None:
        """Delete a task"""
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return
        
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self._save_tasks()
        print(f"Task {task_id} deleted successfully")
    
    def mark_in_progress(self, task_id: int) -> None:
        """Mark a task as in progress"""
        self._update_status(task_id, 'in-progress', "marked as in progress")
    
    def mark_done(self, task_id: int) -> None:
        """Mark a task as done"""
        self._update_status(task_id, 'done', "marked as done")
    
    def _update_status(self, task_id: int, status: str, action: str) -> None:
        """Update task status helper method"""
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return
        
        if task['status'] == status:
            print(f"Task {task_id} is already {status.replace('-', ' ')}")
            return
        
        task['status'] = status
        task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_tasks()
        print(f"Task {task_id} {action} successfully")
    
    def list_tasks(self, status_filter: Optional[str] = None) -> None:
        """List all tasks, optionally filtered by status"""
        if not self.tasks:
            print("No tasks found")
            return
        
        if status_filter:
            valid_statuses = ['todo', 'in-progress', 'done']
            if status_filter not in valid_statuses:
                print(f"Error: Invalid status filter. Use: {', '.join(valid_statuses)}")
                return
            
            filtered_tasks = [task for task in self.tasks if task['status'] == status_filter]
            
            if not filtered_tasks:
                print(f"No tasks with status '{status_filter}' found")
                return
            
            print(f"\nTasks with status '{status_filter}':")
            for task in filtered_tasks:
                self._print_task(task)
            print(f"Total: {len(filtered_tasks)} task(s)")
        else:
            print("\nAll Tasks:")
            for task in self.tasks:
                self._print_task(task)
            print(f"Total: {len(self.tasks)} task(s)")
    
    def summary(self) -> None:
        """Show a summary of tasks by status"""
        if not self.tasks:
            print("No tasks found")
            return
        
        counts = {
            'todo': 0,
            'in-progress': 0,
            'done': 0
        }
        
        for task in self.tasks:
            status = task.get('status', 'todo')
            counts[status] = counts.get(status, 0) + 1
        
        print("\nTask Summary:")
        print(f"  Todo: {counts['todo']}")
        print(f"  In Progress: {counts['in-progress']}")
        print(f"  Done: {counts['done']}")
        print(f"  Total: {len(self.tasks)}")


def print_usage() -> None:
    """Print usage instructions"""
    print("""
Task Tracker CLI - Manage your tasks

Usage:
  python3 task_tracker.py add "Task description"      Add a new task
  python3 task_tracker.py update <id> "New description" Update a task
  python3 task_tracker.py delete <id>                 Delete a task
  python3 task_tracker.py mark-in-progress <id>       Mark task as in progress
  python3 task_tracker.py mark-done <id>              Mark task as done
  python3 task_tracker.py list                        List all tasks
  python3 task_tracker.py list todo                   List todo tasks
  python3 task_tracker.py list in-progress            List in-progress tasks
  python3 task_tracker.py list done                   List done tasks
  python3 task_tracker.py summary                     Show task summary
  python3 task_tracker.py help                        Show this help message

Examples:
  python3 task_tracker.py add "Buy groceries"
  python3 task_tracker.py update 1 "Buy groceries and cook dinner"
  python3 task_tracker.py mark-done 1
  python3 task_tracker.py list done
    """)


def main() -> None:
    """Main function to handle command line arguments"""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    tracker = TaskTracker()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Missing task description")
                print("Usage: task-cli add \"Task description\"")
                sys.exit(1)
            tracker.add(sys.argv[2])
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Missing task ID or description")
                print("Usage: task-cli update <id> \"New description\"")
                sys.exit(1)
            tracker.update(int(sys.argv[2]), sys.argv[3])
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                print("Usage: task-cli delete <id>")
                sys.exit(1)
            tracker.delete(int(sys.argv[2]))
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                print("Usage: task-cli mark-in-progress <id>")
                sys.exit(1)
            tracker.mark_in_progress(int(sys.argv[2]))
        
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                print("Usage: task-cli mark-done <id>")
                sys.exit(1)
            tracker.mark_done(int(sys.argv[2]))
        
        elif command == "list":
            if len(sys.argv) == 2:
                tracker.list_tasks()
            else:
                tracker.list_tasks(sys.argv[2])
        
        elif command == "summary":
            tracker.summary()
        
        elif command in ["help", "--help", "-h"]:
            print_usage()
        
        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
            sys.exit(1)
    
    except ValueError as e:
        print(f"Error: Invalid argument - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()