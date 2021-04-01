"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

# Решение протестировано и работает
class Tasks:
    def __init__(self):
        self.base_tasks = []
        self.decided_tasks = []
        self.correction_tasks = []

    def add_task(self, taskname):
        self.base_tasks.insert(0, taskname)

    def send_to_solve(self):
        self.decided_tasks.insert(0, self.base_tasks[-1])
        self.base_tasks.pop()

    def send_to_correct(self):
        self.correction_tasks.insert(0, self.base_tasks[-1])
        self.base_tasks.pop()

    def sent_to_base(self):
        self.base_tasks.insert(0, self.correction_tasks[-1])
        self.correction_tasks.pop()

    def print_tasks(self):
        print('Base       ',*self.base_tasks) if len(self.base_tasks) > 0 else print('Base is empty')
        print('Decided    ',*self.decided_tasks) if len(self.decided_tasks) > 0 else print('Decided is empty')
        print('Correction ',*self.correction_tasks) if len(self.correction_tasks) > 0 else print('Correction is empty')

if __name__ == '__main__':
    a = Tasks()

    a.add_task('Task1')
    a.add_task('Task2')
    a.add_task('Task3')
    a.add_task('Task4')
    a.add_task('Task5')
    a.add_task('Task6')
    a.add_task('Task7')
    a.add_task('Task8')

    a.send_to_solve()
    a.send_to_solve()

    a.send_to_correct()
    a.send_to_correct()

    a.sent_to_base()
    a.send_to_solve()
    a.sent_to_base()
    a.send_to_correct()

    a.print_tasks()