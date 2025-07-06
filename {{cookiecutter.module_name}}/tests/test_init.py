from {{cookiecutter.module_name}} import main as mut  # module under test


def test_init():
    assert mut.time_to_write_some_code()
