#需要安装pillow库
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
from PIL import Image, ImageFont, ImageDraw

class Book:
    def __init__(self, ID=0, name="", authors=None, pub_date="", publisher="", isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None):
        if bookLists is None:
            bookLists = []
        if tags is None:
            tags = []
        if authors is None:
            authors = []
        self.ID = ID  # 序号，每本书的序号将作为它的关键码，不能有重复，对用户是不可见的
        self.name = name
        self.authors = authors
        self.pub_date = pub_date
        self.publisher = publisher
        self.isbn = isbn  # 以字符串形式存储
        self.language = language
        self.cover_path = cover_path  # 封面的存储位置，通过此信息加载封面
        self.rating = rating  # 评分，int型数据，1星到5星，0表示未评分
        self.file_path = file_path  # 文件位置，可以根据此信息打开文件
        self.tags = tags  # 书籍的标签，列表
        self.bookLists = bookLists  # 所属的书单，列表
        self.INFO = None
        self.isOpen = False  # 书籍是否已经打开

def vertical_write(book_info_strs, drawobj, font, color, x):
    W, H = 365, 458
    row_hight = 0 # 行高设置（文字行距）
    word_dir = 10 # 文字间距
    right = 0   # 往右位移量
    down = -20 # 往下位移量 
    i = 0
    w, h = font.getsize(book_info_strs[0]) # 获取第一个文字的宽和高 
    num_h = len(book_info_strs)
    while i < len(book_info_strs):    
        char = book_info_strs[i]
        if char == "," or char == "\n" :  
            right = right + w  + row_hight
            down = -20
            continue
        elif char == '[': # 遇到[]符号时，合并三个字符
            char = book_info_strs[i:i+3]
            i += 2
            num_h -= 2 # 字数减二(计算高度用)
        elif i == 0:
            down = -20
        else:
            down = down + h + word_dir
        i += 1
        height = num_h*h + word_dir*(num_h-1)
        y = (H - height)/2
        drawobj.text((x+right, y+down), char, font=font, fill=color) # 设置位置坐标 文字 颜色 字体

def template_first(book, color, color_index):
    W, H = 365, 458
    im = Image.new('RGB', (W, H), color[0])
    drawobj = ImageDraw.Draw(im)
    book_name = book.name
    font = ImageFont.truetype('./fonts/方正咆哮体.TTF', 38) # 选取字体为方正咆哮体, 36号
    w, h = drawobj.textsize(book_name, font=font)
    drawobj.text(((W-w)/2, 110), book_name, font=font, fill=color[1])

    authors = book.authors
    font = ImageFont.truetype('./fonts/SIMSUN.TTC', 13) # 选取字体为宋体, 13号
    w, h = drawobj.textsize(authors, font=font)
    drawobj.text(((W-w)/2, 250), authors, font=font, fill=color[2])

    publisher = book.publisher
    font = ImageFont.truetype('./fonts/华文细黑.ttf', 12) # 选取字体为华文细黑, 12号
    w, h = drawobj.textsize(publisher, font=font)
    drawobj.text(((W-w)/2, 380), publisher, font=font, fill=color[3]) 
    im.show()
    im.save('./res_picture/template_first_color_' + str(color_index+1) + '/' + book_name + '.png')

def template_second(book, color, color_index):
    W, H = 365, 458
    im = Image.new('RGB', (W, H), color[0])
    drawobj = ImageDraw.Draw(im)
    book_name = book.name
    font = ImageFont.truetype('./fonts/方正喵呜体.TTF', 38) # 选取字体为方正喵呜体, 38号
    vertical_write(book_name, drawobj, font, color[1], 120) # 竖写

    authors = book.authors
    font = ImageFont.truetype('./fonts/SIMSUN.TTC', 13) # 选取字体为宋体, 13号
    vertical_write(authors, drawobj, font, color[2], 250) # 竖写

    publisher = book.publisher
    font = ImageFont.truetype('./fonts/华文细黑.ttf', 12) # 选取字体为华文细黑, 12号
    w, h = drawobj.textsize(publisher, font=font)
    drawobj.text(((W-w)/2, 380), publisher, font=font, fill=color[3]) 
    im.show()
    im.save('./res_picture/template_second_color_' + str(color_index+1) + '/' + book_name + '.png')

def del_file(path_data):
    for i in os.listdir(path_data) : # 返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + '\\' + i # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True: # 判断是否为文件,如果是文件,就删除
            os.remove(file_data)
        else:                                   # 如果是文件夹,递归给del_file
            del_file(file_data)

def main():
    books = []
    books.append(Book(name='解忧杂货店', authors='[日]东野圭吾', pub_date='2014-5', publisher='南海出版公司', isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None)) # 将书籍信息逐一导入书籍列表
    books.append(Book(name='活着', authors='余华', pub_date='2012-8-1', publisher='作家出版社', isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None)) 
    books.append(Book(name='追风筝的人', authors='[美]卡勒德·胡赛尼', pub_date='2006-5', publisher='上海人民出版社', isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None)) 
    books.append(Book(name='白夜行', authors='[日]东野圭吾', pub_date='2008-9', publisher='南海出版公司', isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None)) 
    books.append(Book(name='三体', authors='刘慈欣', pub_date='2008-1', publisher='重庆出版社', isbn="", language="", cover_path="",
                 rating=0, file_path="", tags=None, bookLists=None)) 

    # 清空文件夹下文件
    del_file('./res_picture/template_first_color_1/')
    del_file('./res_picture/template_first_color_2/')
    del_file('./res_picture/template_first_color_3/')
    del_file('./res_picture/template_second_color_1/')
    del_file('./res_picture/template_second_color_2/')
    del_file('./res_picture/template_second_color_3/')
    
    color_list = [['#87CEFA', '#FF4500', '#8B4513', '#663366'], 
                  ['#FF6633', '#33FF66', '#33CCFF', '#333366'], 
                  ['#ffff66', '#666600', '#3333FF', '#663366']] # 三种配色
    
    for i in range(len(books)):
        mode = random.randint(1, 2)
        color_index = random.randint(0, 2)
        if mode == 1:
            template_first(books[i], color_list[color_index], color_index)
        elif mode == 2:
            template_second(books[i], color_list[color_index], color_index)
        else:
            pass

if __name__ == '__main__':
    main()

