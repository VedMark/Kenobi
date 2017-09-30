#!/usr/bin/python3.6


def singleton(class_):
    class ClassW(class_):
        _instance = None

        def __new__(class_, *args, **kwargs):
            if ClassW._instance is None:
                ClassW._instance = super(ClassW, class_).__new__(class_, *args, **kwargs)
                ClassW._instance._sealed = False
            return ClassW._instance

        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(ClassW, self).__init__(*args, **kwargs)
            self._sealed = True

    ClassW.__name__ = class_.__name__
    return ClassW
