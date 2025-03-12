from app.kata_manhattan import manhattan_distance,Point


def test_manhattan_distance_empty():
    p1 = Point()
    p2 = Point()
    actual = manhattan_distance(p1,p2)
    expected = 0
    assert actual == expected
