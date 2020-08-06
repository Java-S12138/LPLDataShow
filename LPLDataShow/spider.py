# @BY     :Java_S
# @Time   :2020/8/4 9:04
# @Slogan :够坚定够努力大门自然会有人敲,别怕没人赏识就像三十岁的梵高

import time
import pymysql
from lxml import etree
from selenium import webdriver

class LPL_Data:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
        self.url = 'https://lpl.qq.com/es/data/rank.shtml?iGameId=134&sGameType=7,8'
        self.db = pymysql.connect(
                        host = 'localhost',user = 'root',
                        passwd = '123456',db = 'lpl',charset = 'utf8')
        self.cur = self.db.cursor()

    def click(self,xp):
        self.browser.find_element_by_xpath(xp).click()

    def get_html(self,rule):
        info = self.browser.find_element_by_xpath(rule)
        html = info.get_attribute("innerHTML")
        return html

    def all_html(self):
        self.browser.get(self.url)

        #战队胜率前五
        wings_top5_html = self.get_html('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/div[1]')

        #战队金钱前十二
        self.click('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/ul/li[6]')
        time.sleep(1)
        wings_money12_html = self.get_html('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/div[1]')

        #个人击杀前五
        self.click('//*[@id="data-page"]/ul/li[2]/a')
        time.sleep(1)
        member_kill_top5 = self.get_html('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/div[1]')

        #个人MVP前十二
        self.click('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/ul/li[10]/a')
        time.sleep(1)
        member_mvp_top12 = self.get_html('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/div[1]')

        #英雄pick率前六十
        self.click('//*[@id="data-page"]/ul/li[3]/a')
        time.sleep(1)
        hero_top_1_12 = self.get_html('//*[@id="data-page"]/div[4]/div[3]/div[2]/div/div[1]')
        hero_top60 = [etree.HTML(hero_top_1_12)]
        for i in range(4):
            count = i+5
            if count < 7:
                self.click(f'//*[@id="heroPageContent"]/a[{count}]')
            else:
                self.click('//*[@id="heroPageContent"]/a[7]')
            time.sleep(1)
            hero_top = self.get_html('//*[@id="data-page"]/div[4]/div[3]/div[2]/div/div[1]')
            hero_top60.append(etree.HTML(hero_top))

        #首页圆圈数据
        self.click('//*[@id="data-page"]/ul/li[1]/a')
        self.click('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/ul/li[1]/a')
        time.sleep(1)
        win_rate_name = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[2]').text
        win_rate_v_d = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[4]/b').text.split('/')
        win_rate_v = win_rate_v_d[0]
        win_rate_d = win_rate_v_d[1]

        self.click('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/ul/li[2]/a')
        time.sleep(1)
        wings_kill_name = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[2]').text
        wings_kill_kill = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[6]').text.split("(")[0]
        wings_kill_die = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[7]').text.split("(")[0]

        self.click('//*[@id="data-page"]/div[4]/div[1]/div[2]/div/ul/li[4]/a')
        time.sleep(1)
        play_eye_name = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[2]').text
        in_eye = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[8]/b').text
        out_eye = self.browser.find_element_by_xpath('//*[@id="teamRank"]/tr[1]/td[9]/b').text

        self.click('//*[@id="data-page"]/ul/li[2]/a')
        self.click('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/ul/li[4]/a')
        time.sleep(1)
        kda_name = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[2]').text
        kda_kill = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[5]/b').text.split("(")[0]
        kda_a = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[6]/b').text.split("(")[0]
        kda_d = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[7]/b').text.split("(")[0]
        kda_ka = str(int(kda_a)+int(kda_kill))

        self.click('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/ul/li[3]/a')
        time.sleep(1)
        die_name = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[2]').text
        die_kill = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[5]/b').text.split("(")[0]
        die_a = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[6]/b').text.split("(")[0]
        die_d = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[7]/b').text.split("(")[0]
        die_ka = str(int(die_kill) + int(die_a))

        self.click('//*[@id="data-page"]/div[4]/div[2]/div[2]/div/ul/li[1]/a')
        time.sleep(1)
        kill_name = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[2]').text
        kill_kill = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[5]/b').text.split("(")[0]
        kill_a = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[6]/b').text.split("(")[0]
        kill_d = self.browser.find_element_by_xpath('//*[@id="personalRank"]/tr[1]/td[7]/b').text.split("(")[0]
        kill_ad = str(int(kill_a) + int(kill_d))

        self.browser.quit()

        name = [win_rate_name,wings_kill_name,play_eye_name,kda_name,die_name,kill_name]
        data1 = [win_rate_v,wings_kill_kill,in_eye,kda_ka,die_d,kill_kill]
        data2 = [win_rate_d,wings_kill_die,out_eye,kda_d,die_ka,kill_ad]
        round_list = [('name',name),('data1',data1),('data2',data2)]
        round_dict = {key:value for key,value in round_list}

        html_list = [('战队胜率前五', wings_top5_html), ('战队金钱前十二', wings_money12_html), ('个人击杀前五', member_kill_top5),
                     ('个人MVP前十二', member_mvp_top12)]
        html_dict = {key: etree.HTML(value) for key, value in html_list}
        html_dict['英雄pick率前六十'] = hero_top60
        html_dict['首页圆圈数据'] = round_dict

        return html_dict

    def data(self):
        html_dict = self.all_html()

        # 战队排行榜前五
        wings_top_rule = ["//tbody[@id = 'teamRank']/tr/td[2]/text()","//tbody[@id = 'teamRank']/tr/td[3]/b/text()","//tbody[@id = 'teamRank']/tr/td[5]/b/text()"]
        wings_top_xpath = [html_dict['战队胜率前五'] for i in range(3)]
        wings_top5 = list(map(lambda xpath,rule :xpath.xpath(rule)[:5],wings_top_xpath,wings_top_rule))

        # 战队胜负数据表
        wings_money12_rule = ["//tbody[@id = 'teamRank']/tr/td[2]/text()","//tbody[@id = 'teamRank']/tr/td[4]/b/strong/text()","//tbody[@id = 'teamRank']/tr/td[4]/b/em/text()","//tbody[@id = 'teamRank']/tr/td[5]/b/text()"]
        wings_money12_xpath = [html_dict['战队金钱前十二'] for i in range(4)]
        wings_money12 = list(map(lambda xpath,rule :xpath.xpath(rule),wings_money12_xpath,wings_money12_rule))

        # 个人排行榜前五
        member_kill_name = html_dict['个人击杀前五'].xpath('//tbody[@id="personalRank"]/tr/td[2]/text()')[:5]
        member_kill_seat = html_dict['个人击杀前五'].xpath('//tbody[@id="personalRank"]/tr/td[3]/text()')[:5]
        member_kill_sum = [i[:3] for i in html_dict['个人击杀前五'].xpath('//tbody[@id="personalRank"]/tr/td[5]/b/text()')[:5]]
        member_kill_top5 = [member_kill_name,member_kill_seat,member_kill_sum]

        # 个人MVP前十二
        member_mvp_top12_name = html_dict['个人MVP前十二'].xpath('//tbody[@id="personalRank"]/tr/td[2]/text()')
        member_mvp_top12_out_count = html_dict['个人MVP前十二'].xpath('//tbody[@id="personalRank"]/tr/td[4]/b/text()')
        member_mvp_top12_kill_sum = [i[:3] for i in html_dict['个人MVP前十二'].xpath('//tbody[@id="personalRank"]/tr/td[5]/b/text()')]
        member_mvp_top12_assist_sum = [i[:3] for i in html_dict['个人MVP前十二'].xpath('//tbody[@id="personalRank"]/tr/td[6]/b/text()')]
        member_mvp_top12_die_sum = [i[:3] for i in html_dict['个人MVP前十二'].xpath('//tbody[@id="personalRank"]/tr/td[7]/b/text()')]
        member_mvp_top12 = [member_mvp_top12_name,member_mvp_top12_out_count,member_mvp_top12_kill_sum,member_mvp_top12_assist_sum,member_mvp_top12_die_sum]

        #英雄pick率前六十
        hero_name = [j for i in html_dict['英雄pick率前六十'] for j in i.xpath('//*[@id="heroRank"]/tr/td[2]/text()')]
        hero_out_count = [j for i in html_dict['英雄pick率前六十'] for j in i.xpath('//*[@id="heroRank"]/tr/td[3]/b/text()')]
        hero_pick = [j for i in html_dict['英雄pick率前六十'] for j in i.xpath('//*[@id="heroRank"]/tr/td[4]/b/text()')]
        hero_win_rete = [j for i in html_dict['英雄pick率前六十'] for j in i.xpath('//*[@id="heroRank"]/tr/td[6]/b/text()')]
        hero_top60 = [hero_name,hero_out_count,hero_pick,hero_win_rete]

        data_list = [('战队排行榜前五',wings_top5),('战队胜负数据表',wings_money12),('个人排行榜前五',member_kill_top5),
                     ('个人MVP前十二',member_mvp_top12),('英雄pick率前六十',hero_top60)]
        data_dict = {key:value for key,value in data_list}
        data_dict['首页圆圈数据'] = html_dict['首页圆圈数据']
        print("数据爬取成功！")
        return data_dict

    def save_mysql(self):
        data_dict = self.data()

        try:

            self.cur.execute("DROP TABLE IF EXISTS 战队排行榜前五")
            set_sql_top5 = """
                        create table 战队排行榜前五(
                        战队名称 varchar(20),
                        出场次数 varchar(10),
                        胜率 varchar(10))
                          """
            self.cur.execute(set_sql_top5)
            self.db.commit()

            save_sql_top5 = "INSERT INTO 战队排行榜前五 values(%s,%s,%s);"
            for i in range(5):
                self.cur.execute(save_sql_top5,
                                 (data_dict['战队排行榜前五'][0][i],
                                 data_dict['战队排行榜前五'][1][i],
                                 data_dict['战队排行榜前五'][2][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

        try:

            self.cur.execute("DROP TABLE IF EXISTS 战队胜负数据")
            set_sql_wings_wd = """
                            create table 战队胜负数据(
                            战队名称 varchar(20),
                            胜场次数 varchar(10),
                            败场次数 varchar(10),
                            胜率 varchar(10))
                              """
            self.cur.execute(set_sql_wings_wd)
            self.db.commit()

            save_sql_wings_vd = "INSERT INTO 战队胜负数据 values(%s,%s,%s,%s);"
            for i in range(12):
                self.cur.execute(save_sql_wings_vd,
                                 (data_dict['战队胜负数据表'][0][i],
                                  data_dict['战队胜负数据表'][1][i],
                                  data_dict['战队胜负数据表'][2][i],
                                  data_dict['战队胜负数据表'][3][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

        try:

            self.cur.execute("DROP TABLE IF EXISTS 个人排行榜前五")
            set_sql_member_top5 = """
                            create table 个人排行榜前五(
                            队员名称 varchar(20),
                            位置 varchar(10),
                            总击杀 varchar(10))
                              """
            self.cur.execute(set_sql_member_top5)
            self.db.commit()

            save_sql_member5 = "INSERT INTO 个人排行榜前五 values(%s,%s,%s);"
            for i in range(5):
                self.cur.execute(save_sql_member5,
                                 (data_dict['个人排行榜前五'][0][i],
                                  data_dict['个人排行榜前五'][1][i],
                                  data_dict['个人排行榜前五'][2][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

        try:

            self.cur.execute("DROP TABLE IF EXISTS 个人MVP前十二")
            set_sql_member_mvp = """
                                create table 个人MVP前十二(
                                队员名称 varchar(20),
                                出场次数 varchar(10),
                                总击杀 varchar(10),
                                总助攻 varchar(10),
                                总死亡 varchar(10))
                                  """
            self.cur.execute(set_sql_member_mvp)
            self.db.commit()

            save_sql_member_top12 = "INSERT INTO 个人MVP前十二 values(%s,%s,%s,%s,%s);"
            for i in range(12):
                self.cur.execute(save_sql_member_top12,
                                 (data_dict['个人MVP前十二'][0][i],
                                  data_dict['个人MVP前十二'][1][i],
                                  data_dict['个人MVP前十二'][2][i],
                                  data_dict['个人MVP前十二'][3][i],
                                  data_dict['个人MVP前十二'][4][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

        try:

            self.cur.execute("DROP TABLE IF EXISTS 英雄pick率前六十")
            set_sql_hero_top60 = """
                                create table 英雄pick率前六十(
                                英雄名称 varchar(20),
                                出场次数 varchar(10),
                                pick比率 varchar(10),
                                胜率 varchar(10))
                                  """
            self.cur.execute(set_sql_hero_top60)
            self.db.commit()

            save_sql_hero_top60 = "INSERT INTO 英雄pick率前六十 values(%s,%s,%s,%s);"
            for i in range(len(data_dict['英雄pick率前六十'][0])):
                self.cur.execute(save_sql_hero_top60,
                                 (data_dict['英雄pick率前六十'][0][i],
                                  data_dict['英雄pick率前六十'][1][i],
                                  data_dict['英雄pick率前六十'][2][i],
                                 data_dict['英雄pick率前六十'][3][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

        try:

            self.cur.execute("DROP TABLE IF EXISTS 首页圆圈数据")
            set_sql_home_data = """
                                create table 首页圆圈数据(
                                name varchar(20),
                                data1 varchar(10),
                                data2 varchar(10))
                                  """
            self.cur.execute(set_sql_home_data)
            self.db.commit()

            save_sql_home_data = "INSERT INTO 首页圆圈数据 values(%s,%s,%s);"

            self.db.commit()
            for i in range(len(data_dict['首页圆圈数据']['name'])):
                self.cur.execute(save_sql_home_data,
                                 (data_dict['首页圆圈数据']['name'][i],
                                  data_dict['首页圆圈数据']['data1'][i],
                                  data_dict['首页圆圈数据']['data2'][i]))
                self.db.commit()
            print("写入数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)

# lpl = LPL_Data()
# lpl.save_mysql()