'''
12. 鸭子类型

“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”

我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。

比如在python中，有很多file-like的东西，比如StringIO,GzipFile,socket。它们有很多相同的方法，我们把它们当作文件使用。

又比如list.extend()方法中,我们并不关心它的参数是不是list,只要它是可迭代的,所以它的参数可以是list/tuple/dict/字符串/生成器等.

鸭子类型在动态语言中经常使用，非常灵活，使得python不想java那样专门去弄一大堆的设计模式。

13. Python中重载
引自知乎:http://www.zhihu.com/question/20053359
函数重载主要是为了解决两个问题。

可变参数类型。
可变参数个数。
另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。

好吧，那么对于情况 1 ，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数。

那么对于情况 2 ，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。

好了，鉴于情况 1 跟 情况 2 都有了解决方案，python 自然就不需要函数重载了。


14. 新式类和旧式类

直到Python 2.1，旧式类才是供用户使用的唯一样式。

（旧式）类的概念与类型的概念无关：如果x是旧式类的实例，则x.__class__ 指定的类x，但type(x)始终为<type
  'instance'>。

这反映了这样一个事实，即所有旧式实例（独立于其类）均使用称为实例的单个内置类型实现。

在Python 2.2中引入了新型类，以统一类和类型的概念。新型类只是用户定义的类型，不多也不少。

如果x是新样式类的实例，则type(x)通常与x 相同x.__class__（尽管不能保证–允许新样式类实例覆盖所返回的值x.__class__）。

引入新型类的主要动机是提供具有完整元模型的统一对象模型。

它还具有许多直接的好处，例如能够对大多数内置类型进行子类化，或者引入了“描述符”，以启用计算属性。

出于兼容性原因，默认情况下，类仍为旧样式。

通过将另一个新样式类（即一种类型）指定为父类或“顶级类型”对象（如果不需要其他父类）来创建新样式类。

新样式类的行为与旧样式类的行为不同，除了返回什么类型外，还有许多重要的细节。

其中一些更改是新对象模型的基础，例如调用特殊方法的方式。其他是出于兼容性考虑而无法实现的“修补程序”，例如在多重继承的情况下的方法解析顺序。

Python 3仅具有新型类。

无论是否从中继承子类object，类都是Python 3中的新型样式。

新式类很早在2.2就出现了,所以旧式类完全是兼容的问题,Python3里的类全部都是新式类.这里有一个MRO问题可以了解下(新式类是广度优先,旧式类是深度优先),<Python核心编程>里讲的也很多.

一个旧式类的深度优先的例子

class A():
    def foo1(self):
        print "A"

class B(A):
    def foo2(self):
        pass

class C(A):
    def foo1(self):
        print "C"

class D(B, C):
    pass

d = D()

d.foo1()
# A
按照经典类的查找顺序从左到右深度优先的规则，在访问d.foo1()的时候,D这个类是没有的..那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过

15. __new__和__init__的区别

这个__new__确实很少见到,先做了解吧.

__new__是一个静态方法,而__init__是一个实例方法.
__new__方法会返回一个创建的实例,而__init__什么都不返回.
只有在__new__返回一个cls的实例时后面的__init__才能被调用.
当创建一个新实例时调用__new__,初始化一个实例时用__init__.

ps: __metaclass__是创建类时起作用.所以我们可以分别使用__metaclass__,__new__和__init__来分别在类创建,实例创建和实例初始化的时候做一些小手脚.

16. 单例模式

​ 单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例
这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.

1 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

2 共享属性

创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1

3 装饰器版本

def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
  ...

4 import方法

作为python的模块是天然的单例模式

class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use

from mysingleton import my_singleton
my_singleton.foo()

'''