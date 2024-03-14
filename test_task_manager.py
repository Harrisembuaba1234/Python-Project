import unittest
from tasks.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        task_manager = TaskManager.get_instance()
        task_manager.add_task("Belajar Python")
        self.assertEqual(len(task_manager.get_tasks()), 1)

    def test_get_tasks(self):
        task_manager = TaskManager.get_instance()
        task_manager.add_task("Belajar Python")
        task_manager.complete_task(1)
        tasks = task_manager.get_tasks()
        self.assertEqual(tasks[0].name, "Belajar Python")
        self.assertEqual(tasks[0].status, "Selesai")  

    def test_complete_task(self):
        task_manager = TaskManager.get_instance()
        task_manager.add_task("Belajar Python")
        task_manager.complete_task(1)
        tasks = task_manager.get_tasks()
        self.assertEqual(tasks[0].name, "Belajar Python")


if __name__ == "__main__":
    unittest.main()
