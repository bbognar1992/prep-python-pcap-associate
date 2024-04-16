import os
import uuid

FILE_PATH = "tasks.txt"


class Page(object):
    @classmethod
    def show(cls) -> None:
        pass

    @classmethod
    def choice(cls) -> int:
        return 0


class MainMenu(Page):
    @classmethod
    def show(cls) -> None:
        print("== TODO LIST ==")
        print("[1] Show tasks")
        print("[2] Add task")
        print("[3] Complete task")
        print("[4] Exit")

    @classmethod
    def choice(cls) -> int:
        try:
            choice = int(input("Your choice:"))
            if choice not in range(1, 5):
                raise ValueError("Not in range")
        except ValueError as e:
            print(e)
            return 0
        else:
            return choice


class ShowTasks(Page):

    @classmethod
    def show(cls) -> None:
        print("")
        print("[YOUR TASKS]")
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                for task in f.readlines():
                    if task != "":
                        print(task)
        else:
            print("Empty list")
        print("")


class AddTask(Page):

    @classmethod
    def show(cls) -> None:
        print("")
        print("[ADD TASK]")

    @classmethod
    def choice(cls) -> int:
        try:
            t_id = str(uuid.uuid4())
            t_name = input("What is the task?")
            t_deadline = input("What is deadline?")
            accepted_dl = ["today", "tomorrow"]
            if t_deadline not in accepted_dl:
                raise ValueError(f"{t_deadline} not in {accepted_dl}")

            tasks = []
            if os.path.exists(FILE_PATH):
                tasks: list
                with open(FILE_PATH, "r") as f:
                    tasks = f.readlines()

            tasks.append(f"{t_id} | {t_name} | {t_deadline}")

            with open(FILE_PATH, "w") as f:
                f.write("\n".join(tasks) + "\n")

        except Exception as e:
            print(e)
            return 0
        else:
            return 1


class CompleteTask(ShowTasks):
    @classmethod
    def choice(cls) -> int:
        try:
            t_id = input("Enter id to complete")
            tasks = []
            if os.path.exists(FILE_PATH):
                tasks: list
                with open(FILE_PATH, "r") as f:
                    for line in f.readlines():
                        task = tuple(line.split(" | "))
                        if t_id != tasks[0]:
                            tasks.append(task)
                        else:
                            raise ValueError(f"Unknown ID: {t_id}")
            if tasks:
                with open(FILE_PATH, "w") as f:
                    f.write("\n".join(tasks) + "\n")

        except Exception as e:
            print(e)
            return 0
        else:
            return 1


class Exit(Page):
    @classmethod
    def show(cls) -> None:
        exit(0)


if __name__ == "__main__":
    pages = {
        0: MainMenu,
        1: ShowTasks,
        2: AddTask,
        3: CompleteTask,
        4: Exit
    }
    selected_page = 0
    while True:
        pages[selected_page].show()
        selected_page = pages[selected_page].choice()
