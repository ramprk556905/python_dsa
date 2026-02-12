# class Cookie:
#     def __init__(self,color):
#         self.color = color
#     def get_color(self):
#         return self.color
#     def set_color(self,color):
#         self.color = color

# my_cookie = Cookie("brown")
# my_cookie_1 = Cookie("black")
# print('First Cookie color:', my_cookie.get_color())
# print('Second Cookie color:', my_cookie_1.get_color())

# my_cookie.set_color("dark brown")
# print('First Cookie new color:', my_cookie.get_color())



def list_methods():
    lst1 = [1,2,3,4,6,5,6]

    lst1.remove(6)
    for i in range(len(lst1)):
        print(lst1[i])

def list_comprehension():
    lst=[]
    even_lst = []
    for i in range(20):
        if i > 0:
            lst.append(i)
    even_lst = [x for x in lst if x%2==0]
    return even_lst


print(list_comprehension())