# Python学习
# 学习时间：2022/8/20 9:56

class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, Cpu, Disk):
        self.Cpu = Cpu
        self.Disk = Disk

# 变量的赋值

cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))
# 赋值操作会使两个变量指向同一个对象的id


# 类的浅拷贝

print('----------------------------')
disk = Disk()
computer = Computer(cpu1, disk)
import copy
computer2 = copy.copy(computer)
print(computer, computer.Cpu, computer.Disk)
print(computer2, computer2.Cpu, computer2.Disk)
# 浅拷贝只是新建一个对象，但是新对象里面的属性还是源对象的属性

# 深拷贝
computer3 = copy.deepcopy(computer)
print('----------------------------')
print(computer, computer.Cpu, computer.Disk)
print(computer3, computer3.Cpu, computer3.Disk)

# 深拷贝就是新建一个对象，并且将源对象里面的所有属性都新建一份
