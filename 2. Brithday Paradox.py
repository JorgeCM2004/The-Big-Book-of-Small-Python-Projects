#Birthday Paradox proves the surprisingly high probability that two people will have the same birthday even in a small group of people.
import random, datetime

def genterate_dates(num):
    birthdays = []
    for i in range(num):
        datetime.datetime(random.randint(0, 2023), random.randint(1, 12), )