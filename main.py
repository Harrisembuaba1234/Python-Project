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
            name =input("Masukkan Nama Tugas: ")
            task_manager.add_task(name)
            print("TUgas berhasil ditambah.")
            save_to_json(task_manager.get_tasks())
            

        elif choice == "2":
            tasks = task_manager.get_tasks()
            for i, task in enumerate(tasks,1):
                print(f"{i}.{task.name}({task.status})")
            

        elif choice == "3":
            task_id = int(input("Masukkan ID Tugas Yang ingin Diselesaikan: "))
            task_manager.complete_task(task_id)
            print("tugas selesai.")
            save_to_json(task_manager.get_tasks())

        elif choice == "4":
            break

        else:
            print("Pilihan tidak ada!")


if __name__ == "__main__":
    main()
        
            