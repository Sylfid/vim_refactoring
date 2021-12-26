import vim

from json_refactoring import JsonRefactoring


def refactor_json():
    JsonRefactoring().refactor_current_buffer(vim.current.buffer)
