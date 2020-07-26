from module.module2 import Module2


class ModuleTest:
    def __init__(self):
        print('module test.')

if __name__ == "__main__":
    module_test = ModuleTest()
    m2 = Module2()
    m2.func_in_module2()