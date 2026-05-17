"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..diff import prep_diff
from ..stdout import strip_ansi



def test_prep_diff() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    text1 = (
        '# This is a comment\n'
        'Mary had a little lamb.\n'
        'But it was actually a wolf.')

    text2 = (
        '# Changed the comment\n'
        'Mary was a little lady.\n'
        'But it was actually a wolf.')

    diff = prep_diff(
        text1, text2,
        ignore=['^#'],
        paths=(
            '/path/to/file1',
            '/path/to/file2'),
        ordered=True)


    _diff = [
        strip_ansi(x)
        for x in diff]

    assert _diff == [
        '--- /path/to/file1',
        '+++ /path/to/file2',
        '@@ -1,2 +1,2 @@\n',
        ' But it was actually a wolf.',
        '-Mary had a little lamb.',
        '+Mary was a little lady.']
