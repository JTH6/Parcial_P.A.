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

    def delete_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

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
                print(f"tarea '{title}' marcada como completada.")
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


if __name__ == "__main__":
    gestor = Task_management()

    tarea1 = Task("Hacer la compra", "Comprar leche y pan", datetime.datetime(2024, 4, 5))
    tarea2 = Task("Enviar informe", "Enviar informe mensual al jefe")
    tarea3 = Task("Llamar al médico", "Pedir cita para revisión", datetime.datetime(2024, 4, 10))

    gestor.add_task(tarea1)
    gestor.add_task(tarea2)
    gestor.add_task(tarea3)

    gestor.pending_tasks()

    gestor.complete_tasks("Hacer la compra")

    gestor.pending_tasks()
    gestor.view_complete_tasks()    
    gestor.notify_tasks()