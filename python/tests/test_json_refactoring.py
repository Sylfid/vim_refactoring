from pytest import fixture

from json_refactoring import JsonRefactoring


@fixture
def json_refactoring() -> JsonRefactoring:
    return JsonRefactoring()


def test_should_refactor_simple_json(json_refactoring):
    current_buffer = ['{"yo": "salut"}']

    json_refactoring.refactor_current_buffer(current_buffer)

    assert current_buffer == [
        '{',
        '    "yo": "salut"',
        '}'
    ]


def test_should_remove_unused_line(json_refactoring):
    current_buffer = ['{"yo": "salut"}', '', '', '']

    json_refactoring.refactor_current_buffer(current_buffer)

    assert current_buffer == [
        '{',
        '    "yo": "salut"',
        '}'
    ]
