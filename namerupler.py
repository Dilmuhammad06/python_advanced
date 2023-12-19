from collections import namedtuple

User = namedtuple('User', ['name', 'age', 'location'])


def get_user():
    return [
        User('Boburjon', 25, 'Fergana'),
        User('Murodjon', 26, 'Namangan'),
        User('Javohir', 25, 'Fergana')
    ]


for i in get_user():
    print(f'{i.name} is {i.age} years old and live in {i.location}')
