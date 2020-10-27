import module as m


class ModuleTest:
    def __init__(self):
        print('module test.')

if __name__ == "__main__":
    module_test = ModuleTest()
    m2 = m.Module2()
    m2.func_in_module2()