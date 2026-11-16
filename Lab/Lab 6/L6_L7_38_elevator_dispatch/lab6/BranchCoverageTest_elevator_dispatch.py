import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator

def test_direction_up():
    assert next_direction(3, "up", [1, 5]) == "up"
    assert next_direction(3, "up", [1]) == "down"
    assert next_direction(3, "up", []) == "idle"


def test_direction_down():
    assert next_direction(3, "down", [1, 5]) == "down"
    assert next_direction(3, "down", [5]) == "up"
    assert next_direction(3, "down", []) == "idle"


def test_direction_non_directional():
    assert next_direction(3, "idle", [5]) == "up"
    assert next_direction(3, "idle", [1]) == "down"
    assert next_direction(3, "idle", [3]) == "idle"


def test_door_action_branches():
    assert door_action(100, False, True) == "hold_open"
    assert door_action(631, False, False) == "overload"
    assert door_action(630, True, False) == "reopen"
    assert door_action(500, False, False) == "close"


def test_pick_elevator_empty():
    assert pick_elevator([], 5) is None


def test_pick_elevator_decision_branches():
    elevators = [
        ("CarA", 10, True),
        ("CarB", 0, False),
        ("CarC", 6, True),
        ("CarD", 4, True),
    ]

    assert pick_elevator(elevators, 5) == "CarC"