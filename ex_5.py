class JsonResult:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):

        result = ""
        for key, value in self.__dict__.items():
            result += key
            result += " : "
            result += str(value)
            result += '\n'
        return result


initParam = {'albumId': '1',
             'id': 1,
             'title': 'accusamus beatae ad facilis cum similique qui sunt',
             'url': 'https://via.placeholder.com/600/92c952',
             'thumbnailUrl': 'https://via.placeholder.com/150/92c952'}

a = JsonResult(initParam)

print(a.title)
print('******************************************************************')
print(a)
