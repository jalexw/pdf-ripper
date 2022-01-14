# This file contains some utility functions for the program
from time import sleep

def countdown_timer(seconds: int):
  for i in range(seconds, 0, -1):
    print("    " + str(i))
    sleep(1.0)
  return

def five_second_timer():
  countdown_timer(5)
  return

def short_pause():
  sleep(1.0)
  return
