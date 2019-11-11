%%writefile first.py
def first(l):
    return l[0]
Overwriting first.py


# This is appended to the file.
def test_first():
    assert first([1, 2, 3]) == 1
Appending to first.py
%cat first.py
def first(l):
    return l[0]

# This is appended to the file.
def test_first():
    assert first([1, 2, 3]) == 1