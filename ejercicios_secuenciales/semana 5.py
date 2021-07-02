import pandas as pd# 
# 
# from turtle  import *
# import turtle

# def cuadrado():
#     i = 0
#     while i < 4:

#         fillcolor("red")
#         turtle.fd(120)
#         turtle.rt(100)
#         begin_fill()
#         goto(90, 0)
#         goto(90, 50)
#         end_fill()
#         i += 1
# cuadrado()

nombres = pd.Series(['mauricio', 'Paula', 'andrea'], index=[1,2,3])
print(nombres)
print(type(nombres))