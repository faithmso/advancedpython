import time


def measure_runtime(func):
  start = time.time()
  func()
  end = time.time()
  print(end-start)


  
def powers(limit):
  return [x**2 for x in range (limit)]



measure_runtime(lambda: powers(50000))

import timeit

print(timeit.timeit("[x**2 for x in range (10)]"))

import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)


price = 'price: $189.50'
expressions = 'price: \$([0-9]*\.[0-9]*)'

matches1 = re.search(expressions, price)
print(matches1.group(0))
print(matches1.group(1))


import logging
logging.basicConfig(
  format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
  level = logging.DEBUG)
logger = logging.getLogger('test_logger')

logger.info = ('This will not show up.')
logger.warning = ('This will.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

def greet():
  print("Hello")


def before_and_after(func):
  print("Before....")
  func()
  print("After....")

before_and_after(greet)


movies = [
  {"name": "The Matrix", "director": "Wachowski"},
  {"name": "Klaus", "director" : "Pablos"},
  {"name" : "1917", "director" : "Mendes"}
]


def find_movie(expected, finder):
  for movie in movies:
    if finder(movie) == expected:
      return movie
  

find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])

print(movie or 'no movies found')



  