class Task:
    def __init__(self, name, status="Belum Selesai"):
        self.name = name
        self.status = status
        
class TaskManager:
    __instance = None
    
    def __init__(self):
        self._tasks = []

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
    
    def add_task(self, name):
        self._tasks.append(Task(name))
        
    def get_tasks(self):
        return self._tasks
    
    def complete_task(self, task_id):
        self._tasks[task_id - 1].status = "Selesai"