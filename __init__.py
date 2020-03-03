# -*- coding:utf-8 -*-
from operator import itemgetter, matmul

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def __getitem__(self, item):
        if item == 0:
            return self.name
        elif item == 1:
            return self.grade
        else:
            return self.age


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
r = sorted(student_tuples, key=itemgetter(2))
print(r)
r = sorted(student_objects, key=itemgetter(2))
print(r)
l = [_ for _ in map(lambda x: x + 1, [_ for _ in range(10)])]
print(l)
dict_vec = {'y': 0, 'z': 1, 'x': 1}

import collections
def p(*args, **kwargs):
    print(args)
    print(kwargs)


p(*dict_vec)
