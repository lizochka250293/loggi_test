import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('hm.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
def add(a,b):
    return a + b


def subtract(a, b):

        return a - b



def multiplicator(a, b):
    return a * b


def division(a, b):

    return a / b



num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logger.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logger.debug(f"Sub: {num_1} - {num_2} = {sub_result}")

mul_result = multiplicator(num_1, num_2)
logger.debug(f"Mul: {num_1} * {num_2} = {mul_result}")

div_result = division(num_1, num_2)
logger.debug(f"Div: {num_1} / {num_2} = {div_result}")
