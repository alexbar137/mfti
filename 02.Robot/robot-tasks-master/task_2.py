#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
  for x in range(2):
    move_down()
  for x in range(4):
    move_right()
    if x == 1:
      fill_cell()
  move_down()


if __name__ == '__main__':
    run_tasks()
