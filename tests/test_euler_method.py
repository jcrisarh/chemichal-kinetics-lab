from src.euler_method import generate_temp_positions_and_remaining_interval

def test_generate_temp_positions_and_remaining_interval_module_zero():
    tf = 1
    dt = 0.2
    assert (generate_temp_positions_and_remaining_interval(tf, dt)) == (6, 0.0)

def test_generate_temp_positions_and_remaining_interval_non_zero_module():
    tf = 1
    dt = 0.3
    assert (generate_temp_positions_and_remaining_interval(tf, dt)) == (5, 0.1)
