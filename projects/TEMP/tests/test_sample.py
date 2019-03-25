
class Test_Sample():


    def test_answer1(self):
        assert 2+3 == 5

    def test_answer2(self):
        assert 2 + 4 == 5


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4