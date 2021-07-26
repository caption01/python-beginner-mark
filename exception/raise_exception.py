def add_name(name):
    """Add a new name to database."""
    if len(name) < 2:
        raise ValueError(name)
    print(f'Name added: {name}')


try:
    add_name('a')
except ValueError as ve:
    print(f'Unable to add name: "{str(ve)}" is too short.')