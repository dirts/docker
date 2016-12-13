#!/usr/bin/env python
#encoding=utf-8
"""
类
模块
包
定义，引用，以及使用
"""

import mymodule             # module
from mymodule import say    # module fn
from mymodule import Person # module class

import AppPackage           # package
from AppPackage import co   # package module
from AppPackage.co import p1   # package.module fn
from AppPackage.co import Cat  # package.module class
from AppPackage.co import *    # package.module all


if __name__ == "__main__":

    say()
    p = Person()
    p.hello()

    p1();
    c = Cat('hua', 20)
    c.miao('miaomiao')
    c.getWeight();

    h = HeiCat('hei', 18)
    h.run()
    h.miao('miao~ao~~')




