from entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import os
import shutil


class Service:
    def __init__(self):
        self.entity = Entity()

    # url을 가져오는 함수
    def url_open(self, url) -> object:
        myparser = 'html.parser'
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        return soup

    # 요일별로 폴더를 생성해주는 함수
    def create_weekday_folder(self, weekday_dict, myfolder):
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return weekday_dict

    # 이미지 저장 경로와 실제로 파일 쓰기를 수행하는 함수
    @staticmethod
    def save_image_file(mysrc, myfolder, weekday_dict, myweekday, mytitle):
        image_file = urlopen(mysrc)
        filename = myfolder + \
            weekday_dict[myweekday] + '\\' + mytitle + '.jpg'

        myfile = open(filename, mode='wb')
        myfile.write(image_file.read())
        myfile.close()

    # 웹툰 리스트를 만들고 이미지 파일을 저장
    def create_webtoon_list(self, soup, myfolder, weekday_dict):
        mytarget = soup.find_all('div', attrs={'class': 'thumb'})
        print(len(mytarget))

        mylist = []

        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')

            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            mysrc = imgtag.attrs['src']

            Service.save_image_file(
                mysrc, myfolder, weekday_dict, myweekday, mytitle)

            sublist = [mytitleid, myweekday, mytitle, mysrc]
            mylist.append(sublist)

        return mylist

    # csv 파일로 저장하는 함수
    def save_csv_file(self, mylist, filename):
        mycolumns = ['타이틀 번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns=mycolumns)
        myframe.to_csv(filename, encoding='utf-8', index=False)
        print('csv 저장 완료')
