from typing import List, Tuple
from pytest import mark
from exercise_done import create_person, get_names_of_adult_persons


def test_simple_create_person() -> None:
    assert create_person("A", "B", 12) == ("A", "B", 12)
    assert create_person("Bart", "John", 34) == ("Bart", "John", 34)


def test_simple_get_names_of_adult_persons() -> None:
    assert get_names_of_adult_persons([("A", "B", 12), ("Doe", "John", 34)]) == ["Doe John"]
    assert get_names_of_adult_persons(
        [("Jones", "Wesley", 31), ("Bart", "John", 34)]
    ) == ["Jones Wesley", "Bart John"]


# An alternative approach using decorators
@mark.parametrize(
    "surname, firstname, age, expected",
    [("A", "B", 12, ("A", "B", 12)), ("Bart", "John", 34, ("Bart", "John", 34)),],
)
def test_create_person(
    surname: str, firstname: str, age: int, expected: Tuple[str, str, int]
) -> None:
    assert create_person(surname, firstname, age) == expected

@mark.parametrize(
    "persons_list, expected",
    [
        (
            [("A", "B", 18), ("C", "D", 20), ("E", "F", 35), ("G", "H", 12)],
            ["A B", "C D", "E F"],
        ),
        ([], []),
    ],
)
def test_get_names_of_adult_persons(
    persons_list: List[Tuple[str, str, int]], expected: List[str]
) -> None:
    assert get_names_of_adult_persons(persons_list) == expected
