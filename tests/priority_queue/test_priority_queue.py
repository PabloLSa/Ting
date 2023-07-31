import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()

    task_1 = {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10}
    task_2 = {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3}
    task_3 = {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7}
    task_4 = {"nome_do_arquivo": "arquivo4.txt", "qtd_linhas": 5}

    pq.enqueue(task_1)
    pq.enqueue(task_2)
    pq.enqueue(task_3)
    pq.enqueue(task_4)

    assert len(pq) == 4

    assert pq.search(1) == task_1

    assert pq.dequeue() == task_2
    assert pq.dequeue() == task_1
    assert pq.dequeue() == task_3
    assert len(pq) == 1
    assert pq.dequeue() == task_4
    assert len(pq) == 0

