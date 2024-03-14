import json
from tasks.task_manager import Task, TaskManager

def save_to_json(tasks):
    try:
        with open("data/tasks.json", "w") as f:
            data = [{"name": task.name, "status": task.status} for task in tasks]
            json.dump(data, f, indent=4)
    except json.JSONDecodeError:
        print("Gagal menyimpan data ke file tasks.json")

def main():
    task_manager = TaskManager.get_instance()
    
    try:
        with open("data/tasks.json", "r") as f:
            tasks = json.load(f)
            task_manager._tasks = [Task(task["name"], task["status"]) for task in tasks]
    except FileNotFoundError:
        print("File tasks.json tidak ditemukan")
        task_manager._tasks = []
    except json.encoder.JSONEncoder:
        print("Error: Format file tasks.json tidak valid")
        task_manager._tasks = []
        
    while True:
        print("**Sistem Manajemen Tugas Sederhana**")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Selesaikan Tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            break

        elif choice == "2":
            break

        elif choice == "3":
            break

        elif choice == "4":
            break

        else:
            print("Pilihan tidak ada!")


if __name__ == "__main__":
    main()
        
            