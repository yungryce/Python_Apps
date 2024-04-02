# class ade:
#     x = [2, 4, 9, 10]
#     y = {'boys':3, 'girls':8}
# pdjs = ade()
# # print(pdjs.x)
# # print(pdjs.y)
# print(type(ade))
# # print(dir(ade))


# fill = list()
# print(type(fill))

# # print(dir(dict()))
# print(f'how far na {ade.x}')


# # class dict:
# a = 'string'
# print(type(a.upper()))


# class partyanimal:
#     x = 0

#     def __init__(self):
#         print('i just constructed a party function in a class template partyanimal which has become the object')

#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)

#     def __del__(self):
#         print('i am getting destroyed :(')

# agege = partyanimal()
# agege.party()
# agege = 1
# print(agege)


a = ['Sally', 'Jimmy']
class john:
    x = 0
    y = ''
    def __init__(self, z):
        self.y = z
        print(f'{self.y} constructed')
    def party(self):
        self.x += 1
        print(f'{self.y} count {self.x}')
agege = john('Sally')
agege.party()
gage = john('Jimmy')
gage.party()
gage.party()