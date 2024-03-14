import unittest
from tasks.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = {"id": 1, "title": "Test Task", "completed": False}
        self.task_manager.add_task(task)
        self.assertIn(task, self.task_manager.get_tasks())def test_complete_task(self):
        task = {"id": 1, "title": "Test Task", "completed": False}
        self.task_manager.add_task(task)
        self.task_manager.complete_task(1)
        self.assertTrue(self.task_manager.get_tasks()[0]["completed"])

if _name_ == "_main_":
    unittest.main()
