import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator


def test_emergency_holds_doors():
    assert door_action(100, False, True) == "hold_open"


def test_idle_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"


def test_next_direction_up_branches():
    assert next_direction(3, "up", [5]) == "up"
    assert next_direction(3, "up", [1]) == "down"
    assert next_direction(3, "up", []) == "idle"


def test_next_direction_down_branches():
    assert next_direction(3, "down", [1]) == "down"
    assert next_direction(3, "down", [5]) == "up"
    assert next_direction(3, "down", []) == "idle"


def test_next_direction_idle_branches():
    assert next_direction(3, "idle", [5]) == "up"
    assert next_direction(3, "idle", [1]) == "down"


def test_door_action_outcomes():
    assert door_action(700, False, False) == "overload"
    assert door_action(500, True, False) == "reopen"
    assert door_action(500, False, False) == "close"


def test_pick_elevator_logic():
    assert pick_elevator([], 5) is None
    elevators = [
        ("CarA", 10, True),
        ("CarB", 0, False),
        ("CarC", 4, True)
    ]

    assert pick_elevator(elevators, 5) == "CarC"