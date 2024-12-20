# app/utils/decorators.py
# Contains helpers decorators

from typing import Type


def singleton(cls: Type):
    if not isinstance(cls, type):
        raise TypeError("Not a class")

    setattr(cls, "_instance", None)

    original_new = cls.__new__

    def singleton_new(cls_, *args, **kwargs):
        if cls_._instance is None:
            cls_._instance = original_new(cls_, *args, **kwargs)
        return cls_._instance

    cls.__new__ = singleton_new
    return cls
