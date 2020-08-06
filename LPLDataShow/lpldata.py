# @BY     :Java_S
# @Time   :2020/8/4 15:41
# @Slogan :够坚定够努力大门自然会有人敲,别怕没人赏识就像三十岁的梵高

import pymysql
import json

class Lpl_Data:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='lpl')
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def query(self,sql,*args):
        self.cur.execute(sql,args)
        res =self.cur.fetchall()
        #self.close()
        return res

    def get_wings_vd(self):
        sql = 'SELECT 战队名称,胜场次数,败场次数,胜率 FROM 战队胜负数据'
        infos = self.query(sql)
        name = [info[0] for info in infos]
        victory = [info[1] for info in infos]
        defeat = [info[2] for info in infos]
        win_rate = [info[3][:2] for info in infos]

        infos_list = [('name',name),('victory',victory),('defeat',defeat),('winRate',win_rate)]
        infos_dict = {key:value for key,value in infos_list}
        return json.dumps(infos_dict)

    def get_member_top12(self):
        sql = 'SELECT 队员名称,出场次数,总击杀,总助攻,总死亡 FROM 个人mvp前十二'
        infos = self.query(sql)
        name = [info[0] for info in infos]
        out_count = [info[1] for info in infos]
        kill_sum = [info[2] for info in infos]
        assist_sum= [info[3] for info in infos]
        die_sum= [info[4] for info in infos]

        infos_list = [('name', name), ('outcount', out_count), ('killsum', kill_sum), ('assistsum', assist_sum),('diesum',die_sum)]
        infos_dict = {key: value for key, value in infos_list}
        return json.dumps(infos_dict)

    def get_wings_top5(self):
        sql_wings = 'SELECT 战队名称,出场次数,胜率 FROM 战队排行榜前五'
        sql_member = 'SELECT 队员名称,位置,总击杀 FROM 个人排行榜前五'
        infos_wings = self.query(sql_wings)
        infos_member = self.query(sql_member)
        name = [info[0] for info in infos_wings]
        out_count = [info[1] for info in infos_wings]
        win_rate = [info[2] for info in infos_wings]
        member_name = [info[0] for info in infos_member]
        member_post = [info[1] for info in infos_member]
        member_kill_sum = [info[2] for info in infos_member]
        infos_list = [('name', name), ('outcount', out_count), ('winRate', win_rate),
                      ('membername', member_name),('memberpost', member_post),('memberkillsum', member_kill_sum)]
        infos_dict = {key: value for key, value in infos_list}
        return json.dumps(infos_dict)

    def get_hero_top60(self):
        sql = 'SELECT 英雄名称,出场次数,pick比率,胜率 FROM 英雄pick率前六十'
        infos = self.query(sql)
        name = [info[0] for info in infos]
        out_count = [info[1] for info in infos]
        pick = [info[2] for info in infos]
        winrate = [info[3] for info in infos]
        infos_list = [('name', name), ('outcount', out_count), ('picknum', pick),('winrate',winrate)]
        infos_dict = {key: value for key, value in infos_list}
        return json.dumps(infos_dict)
    def get_home_data(self):
        sql = 'SELECT name,data1,data2 FROM 首页圆圈数据'
        infos = self.query(sql)
        name = [info[0] for info in infos]
        data1 = [info[1] for info in infos]
        data2 = [info[2] for info in infos]
        infos_list = [('name', name), ('data1', data1), ('data2', data2)]
        infos_dict = {key: value for key, value in infos_list}
        return json.dumps(infos_dict)


# lpl = Lpl_Data()
# lpl.home_data()
