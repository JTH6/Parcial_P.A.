import datetime

class ITask:
    def notify_tasks(self):
        pass

    def pending_tasks (self):
        pass

    def view_complete_tasks (self):
        pass

    def complete_tasks(self, title):
        pass

class Task():
    def __init__(self, title, description, due_date = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.complete_task = False

    def complete(self):
        self.complete_task = True

class Task_management(Task, ITask):
    
    def __init__(self) -> None:
        self.tasks = []    

    def add_task(self, task: Task):
        if task not in self.tasks:
            self.tasks.append(task)

    def delete_task(self):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Tarea Eliminada Correctamente")

    def pending_tasks (self):
        for task in self.tasks:
            if not task.complete_task:
                print(f"Título: {task.title}")
                print(f"Descripción: {task.description}")
                if task.due_date:
                    print(f"Fecha de vencimiento: {task.due_date}")
                print('\n')

    def view_complete_tasks (self):
        for task in self.tasks:
            if task.complete_task:
                print(f"Título: {task.title}")
                print(f"Descripción: {task.description}")
                print('\n')

    def complete_tasks(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                print(f"\ntarea '{title}' marcada como completada.")
                return
        print(f"No se encontró ninguna tarea con el título '{title}'.")

    def notify_tasks(self):
        for task in self.tasks:
            if task.due_date:
                restant_time = task.due_date - datetime.datetime.now()
                if 0 <= restant_time.days < 3:
                    print(f"¡Notificación!: La tarea '{task.title}' está próxima a su fecha de vencimiento.")
                    print(f"Fecha de vencimiento: {task.due_date}")
                    print('\n')

def main():
    print('Bienvendio a Task Gestion Special \n')
    print("1. Agregar nueva tarea")
    print("2. Eliminar una tarea")
    print("3. Marcar tarea como completada")
    print("4. Ver tareas pendientes")
    print("5. Ver tareas completadas")
    print("6. Salir")
    option = input("\nSeleccione una opción: ")
    return option

gestor = Task_management()

while True:
    option = main()

    if option == "1":
        title = input("\nIngrese el título de la tarea: ")
        print(f'Titulo: {title} \n')
        description = input("Ingrese la descripción de la tarea: ")
        print(f'Descripción: {description} \n')
        due_date_str = input("Ingrese la fecha de vencimiento (opcional - formato: AAAA-MM-DD): ")
        if due_date_str:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
            print(f'Fecha de vencimiento: {due_date} \n')
            task = Task(title, description, due_date)
        else:
            task = Task(title, description)
        gestor.add_task(task)
        print("\nTarea agregada con éxito.\n")

    elif option == "2":
        title = input("\nIngrese el título de la tarea: ")
        gestor.delete_task()
        print(f'Tarea Eliminada: {title} \n')

    elif option == "3":
        title = input("\nIngrese el título de la tarea que desea marcar como completada: ")
        gestor.complete_tasks(title)
        print('\n')

    elif option == "4":
        print("\nTareas pendientes: \n")
        gestor.pending_tasks()
        gestor.notify_tasks()
        print("\n")

    elif option == "5":
        print("\nTareas completadas: \n")
        gestor.view_complete_tasks()
        print("\n")

    elif option == "6":
        print("\nSaliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.\n")