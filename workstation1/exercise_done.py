from typing import List, Tuple
SURNAME_INDEX = 0
FIRSTNAME_INDEX = 1
ADULT_AGE = 18


def create_person(surname: str, firstname: str, age: int) -> Tuple[str, str, int]:
    return surname, firstname, age


def get_names_of_adult_persons(persons: List[Tuple[str, str, int]]) -> List[str]:
    return [f'{person[SURNAME_INDEX]} {person[FIRSTNAME_INDEX]}'
            for person in persons if person[2] >= ADULT_AGE]


if __name__ == '__main__':
    persons_list = []

    mike = create_person('Davis', 'Mike', 25)
    john = create_person('Roberts', 'John', 16)
    lee = create_person('Willams', 'Lee', 46)

    persons_list.append(mike)
    persons_list.append(john)
    persons_list.append(lee)

    print(get_names_of_adult_persons(persons_list))

# List[Tuple[str, str, int]]) -> List[str]: