#!/usr/bin/env python3

def func(x,y):
    print(x+y)
    return x+y




def test_main():
    assert func(3,5) == 8

def main():
    func(3,5)
