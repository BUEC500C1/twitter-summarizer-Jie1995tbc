import pytest
from twitter_vision_main import test_exam1
from twitter_vision_main import test_exam2
from twitter_vision_main import test_exam3

def test1():
    try:
        test_exam1()
    except:
        assert False
    else:
        assert True

def test2():
    try:
        test_exam2()
    except:
        assert False
    else:
        assert True

def test3():
    try:
        test_exam3()
    except:
        assert False
    else:
        assert True