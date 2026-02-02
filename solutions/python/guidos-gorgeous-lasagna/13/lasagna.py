"""Module for calculating preparation and baking times for Guido's lasagna.

This module provides helper functions to calculate remaining bake time,
preparation time, and total elapsed cooking time.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - time already spent baking.
    :return: int - remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time spent preparing and baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time