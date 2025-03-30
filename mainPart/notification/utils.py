import math
class Pagination:
    def __init__(self,data,currentPage,sizePage,totalPage,totalItem,sortField):
        self.data = data
        self.currentPage = currentPage
        self.sizePage = sizePage
        self.totalPage = totalPage
        self.totalItem = totalItem
        self.sortField = sortField

    def ReturnData(self):
        self.data = list(self.data)#Самі дані
        self.totalPage = (self.totalItem+self.sizePage-1)/self.sizePage#Кількість всього сторінок
            #Яка зараз сторінка
        return {
            'data':list(self.data),
            'totalPage':self.totalPage,
            'totalItem':self.totalItem,
            'currentPage':self.currentPage,
            'sizePage':self.sizePage,
            'hasNext': True,
            'hasPrev': True
        }
