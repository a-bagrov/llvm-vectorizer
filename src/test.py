import os

from pycparser import parse_file, c_generator


def test_file(name, showcoord=False):
    print('\n-----' + name + '-----\n')
    src = os.path.abspath(name)
    ast = parse_file(src)  # , cpp_path='C:\\MinGW\\bin\\cpp.exe',use_cpp=True)
    generator = c_generator.CGenerator()
    print(generator.visit(ast))
    ast.show(showcoord=showcoord)


if __name__ == "__main__":
    test_file('c-src/helloworld.c')
    test_file('c-src/simple-loop.c')
    test_file('c-src/prefun.c')
