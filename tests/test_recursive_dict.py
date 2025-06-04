from doms_json import recursive_dict

class Child:
    def __init__(self, name: str) -> None:
        self.name = name

class Parent:
    def __init__(self, child: Child, values: list[int]) -> None:
        self.child = child
        self.values = values


def test_recursive_dict():
    parent = Parent(Child("A"), [1, 2, 3])
    result = recursive_dict(parent)
    assert result == {
        "child": {"name": "A"},
        "values": [1, 2, 3]
    }

