from service import Service
from entity import Entity


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def naver_cartoon(self):
        this = self.entity
        service = self.service
        soup = service.url_open('https://comic.naver.com/webtoon/weekday.nhn')
        myfolder = 'C:\\Users\\hong\\Desktop\\sbaproject\\crawler\\images\\'
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일',
                        'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        service.create_weekday_folder(weekday_dict, myfolder)
        mylist = service.create_webtoon_list(soup, myfolder, weekday_dict)
        service.save_csv_file(mylist, 'cartoon.csv')


if __name__ == '__main__':

    api = Controller()
    api.naver_cartoon()
