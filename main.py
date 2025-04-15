from normalization.components import *

if __name__ == "__main__":
    fd1 = FunctionalDependency("{A} -> {B, C}") #No es un subconjunto de A
    fd2 = FunctionalDependency("{A, B} -> {B}")


    print(fd1.is_trivial()) #false
    print(fd2.is_trivial()) #True

if 