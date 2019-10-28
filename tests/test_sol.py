# Copyright (c) 2019 Alethea Flowers for Winterbloom
# Licensed under the MIT License

import pytest

import winterbloom_smolmidi as smolmidi
from winterbloom_sol import sol


class TestState:
    def test_default_state(self):
        state = sol.State()

        assert state.message is None
        assert state.note is None
        assert state.velocity == 0
        assert state.pitch_bend == 0
        assert state.pressure == 0
        for n in range(128):
            assert state.cc[n] == 0

    def test_copy_from(self):
        state_a = sol.State()
        state_b = sol.State()

        state_a.message = object()
        state_a.note = 42
        state_a.velocity = 43
        state_a.pitch_bend == 45
        state_a.pressure == 46
        for n in range(128):
            state_a.cc[n] = n

        state_b.copy_from(state_a)

        assert state_b.message is state_a.message
        assert state_b.note == state_a.note
        assert state_b.velocity == state_a.velocity
        assert state_b.pitch_bend == state_a.pitch_bend
        assert state_b.pressure == state_a.pressure
        for n in range(128):
            assert state_b.cc[n] == state_a.cc[n]
        
        # Check for deep copy
        state_a.cc[0] = 100
        assert state_b.cc[0] != state_a.cc[0]
