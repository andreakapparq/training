from app.kata_manhattan import manhattan_distance,Point


def test_manhattan_distance_empty():
    p1 = Point()
    p2 = Point()
    actual = manhattan_distance(p1,p2)
    expected = 0
    assert actual == expected


def test_manhattan_distance_first():
    p1 = Point(0,0)
    p2 = Point(0,0)
    actual = manhattan_distance(p1,p2)
    expected = 0
    assert actual == expected

def test_manhattan_distance_sec():
    p1 = Point(0,0)
    p2 = Point(0,1)
    actual = manhattan_distance(p1,p2)
    expected = 1
    assert actual == expected


def test_manhattan_distance_gen():
    p1 = Point(1,1)
    p2 = Point(2,5)
    actual = manhattan_distance(p1,p2)
    expected = 5
    assert actual == expected
