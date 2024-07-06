import os
from rich.console import Console
from rich.table import Table

console = Console()

class Task:
    def __init__(self, text: str):
        self.text: str = text
        self.completed: bool = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self) -> str:
        return self.text

class TodoApp:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task_text: str) -> None:
        task = Task(task_text)
        self.tasks.append(task)
        console.print(f"Задача добавлена: {task_text}")

    def list_tasks(self) -> None:
        table = Table(title="Список дел")
        table.add_column("Номер", style="cyan")
        table.add_column("Задача", style="cyan")
        table.add_column("Выполнено", style="green")
        n = 1
        for task in self.tasks:
            status = "Нет" if not task.completed else "Да"
            table.add_row(str(n), str(task), status)
            n += 1
        console.print(table)

    def list_unfinished_tasks(self) -> None:
        table = Table(title="Список дел")
        table.add_column("Номер", style="cyan")
        table.add_column("Задача", style="cyan")
        table.add_column("Выполнено", style="green")
        n = 1
        for task in self.tasks:
            if task.completed:
                continue
            status = "Нет" if not task.completed else "Да"
            table.add_row(str(n), str(task), status)
            n += 1
        console.print(table)

    def mark_task_completed(self, task_index: int) -> None:
        if task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
            console.print(f"Задача {task_index + 1} помечена как завершенная")
        else:
            console.print("Неправильный номер задачи", style="red")

    def delete_task(self, task_index: int) -> None:
        if task_index < len(self.tasks):
            self.tasks.pop(task_index)
            console.print(f"Задача {task_index + 1} удалена")
        else:
            console.print("Неправильный номер задачи", style="red")

    def run(self) -> None:
        while True:
            console.print("Приложение список дел", style="bold magenta")
            console.print("1. Добавить задачу")
            console.print("2. Список задач")
            console.print("3. Отметить дело как выполненное")
            console.print("4. Показать список незавершенных задач")
            console.print("5. Удалить задачу")
            console.print("6. Выход")
            choice = input("Выберете действие: ")
            if choice == "1":
                task = input("Введите описание задачи: ")
                self.add_task(task)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                task_index = int(input("Введите номер задачи: ")) - 1
                self.mark_task_completed(task_index)
            elif choice == "4":
                self.list_unfinished_tasks()
            elif choice == "5":
                task_index = int(input("Введите номер задачи: ")) - 1
                self.delete_task(task_index)
            elif choice == "6":
                break
            else:
                console.print("Неправильный ввод", style="red")

            console.print("")

if __name__ == "__main__":
    app = TodoApp()
    app.run()