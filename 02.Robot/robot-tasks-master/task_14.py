#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
  while(not(wall_is_on_the_right())):
    fill()
    move_right()
  else:
    fill()

def fill():
  if (not(wall_is_above())):
    fill_above()
  if (not(wall_is_beneath())):
    fill_below()
  if (wall_is_above() and wall_is_beneath()):
    fill_cell()

def fill_above():
  move_up()
  fill_cell()
  move_down()

def fill_below():
  move_down()
  fill_cell()
  move_up()


if __name__ == '__main__':
    run_tasks()
