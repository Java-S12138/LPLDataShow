# @BY     :Java_S
# @Time   :2020/8/14 14:53
# @Slogan :够坚定够努力大门自然会有人敲,别怕没人赏识就像三十岁的梵高
import numpy as np
import pymysql
import requests
import json


hero_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HERORANK_LIST_134_7_8.js'

def mysql():
    db = pymysql.connect(
        host='localhost', user='root',
        passwd='123456', db='lpl', charset='utf8')
    cur = db.cursor()
    return db,cur

def get_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
    response = requests.get(url=url,headers=headers)
    return response.text

def teamrank():
    teamrank_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_TEAMRANK_LIST_134_7_8.js'
    info = get_info(teamrank_api)
    info = json.loads(info)
    info_msg = info['msg']

    teamName = [data['sTeamName'] for data in info_msg]
    out_count = [data['iAppearancesFrequency'] for data in info_msg]
    win = [data['iWin'] for data in info_msg]
    loss = [data['iLoss'] for data in info_msg]
    win_rate = [int(str((int(data['iWin'])/(int(data['iWin'])+int(data['iLoss'])))*100)[:2]) for data in info_msg]
    kill_sum = [data['iKill'] for data in info_msg]
    death_sum = [data['iDeath'] for data in info_msg]
    placed_eye = [int(float(data['sAveragingWardPlaced']))for data in info_msg]
    killed_eye = [int(float(data['sAveragingWardKilled']))for data in info_msg]
    infos_list = [('队名',teamName),('出场次数',out_count),('胜场',win),
                  ('败场',loss),('胜率',win_rate),('总击杀',kill_sum),
                  ('总死亡',death_sum),('插眼',placed_eye),('排眼',killed_eye)]
    info_dict = {key:value for key,value in infos_list}
    return info_dict

def team_top5():
    info_dict = teamrank()
    win_rate_array = np.array(info_dict['胜率'])  # 转换为数组对象
    win_rate_past_count = np.argsort(-win_rate_array)  # argsort（-x）函数返回的是数组值从大到小的索引值
    team_top5_name = [info_dict['队名'][win_rate_past_count[i]] for i in range(5)]
    team_top5_out_count = [info_dict['出场次数'][win_rate_past_count[i]] for i in range(5)]
    team_top5_win_rate = [info_dict['胜率'][win_rate_past_count[i]] for i in range(5)]
    info_list = [(team_top5_name[i],team_top5_out_count[i],str(team_top5_win_rate[i])+'%') for i in range(5)]

    db, cur = mysql()
    try:

        # 是否存在这个表，若存在就删除
        cur.execute("DROP TABLE IF EXISTS 战队排行榜前五")
        # 创建表sql语句
        set_sql_top5 = """                             
                    create table 战队排行榜前五(
                    战队名称 varchar(20),
                    出场次数 varchar(10),
                    胜率 varchar(10))
                      """
        # 执行sql语句
        cur.execute(set_sql_top5)
        db.commit() # 保存

        # 准备写入数据的sql语句
        save_sql_top5 = "INSERT INTO 战队排行榜前五 values(%s,%s,%s);"
        # 写入数据库，参数一:写入的sql语句  参数二:数据，类型为列表，里面的元素类型是元组
        cur.executemany(save_sql_top5,info_list)
        db.commit()

        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)

def team_rate_top12():
    info_dict = teamrank()
    win_rate_array = np.array(info_dict['胜率'])  # 转换为数组对象
    win_rate_past_count = np.argsort(-win_rate_array)  # argsort（-x）函数返回的是数组值从大到小的索引值
    team_rate_top12_name = [info_dict['队名'][win_rate_past_count[i]] for i in range(12)]
    team_rate_top12_win = [info_dict['胜场'][win_rate_past_count[i]] for i in range(12)]
    team_rate_top12_loss = [info_dict['败场'][win_rate_past_count[i]] for i in range(12)]
    team_rate_top12_win_rete = [info_dict['胜率'][win_rate_past_count[i]] for i in range(12)]
    info_list = [(team_rate_top12_name[i], team_rate_top12_win[i],
                  team_rate_top12_loss[i],team_rate_top12_win_rete[i]) for i in range(12)][::-1]

    try:

        db,cur = mysql()

        cur.execute("DROP TABLE IF EXISTS 战队胜负数据")
        set_sql_wings_wd = """
                        create table 战队胜负数据(
                        战队名称 varchar(20),
                        胜场次数 varchar(10),
                        败场次数 varchar(10),
                        胜率 varchar(10))
                          """
        cur.execute(set_sql_wings_wd)
        db.commit()

        save_sql_wings_vd = "INSERT INTO 战队胜负数据 values(%s,%s,%s,%s);"
        cur.executemany(save_sql_wings_vd,info_list)

        db.commit()
        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)

def member():
    member_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_PERSONALRANK_LIST_134_7_8.js'
    info = get_info(member_api)
    info = json.loads(info)
    info_msg = info['msg']
    # member_name = [data['sMemberName'] for data in info_msg]
    # member_position = [data['iPosition'] for data in info_msg]
    # member_kill_sum = [data['iKill'] for data in info_msg]
    # member_assists = [data['iAssists'] for data in info_msg]
    # member_death = [data['iDeath'] for data in info_msg]
    # member_mvp_count = [data['iMVPFrequency'] for data in info_msg]

    key_list = ['sMemberName','iPosition','iKill','iAssists','iDeath','iMVPFrequency','iAppearancesFrequency','iKDA']
    info_list = list(map(lambda key:[data[f'{key}'] for data in info_msg],key_list))
    data_list = [('队员名称',info_list[0]),('位置',info_list[1]),('总击杀',info_list[2]),
                 ('总辅助',info_list[3]),('总死亡',info_list[4]),('mvp次数',info_list[5]),
                 ('出场次数',info_list[6]),('kda',info_list[7])]
    info_dict = {key:value for key,value in data_list}
    return info_dict

def member_top5():
    info_dict = member()
    kill_sum_int = [int(kill) for kill in info_dict['总击杀']]
    member_kill_sum = np.array(kill_sum_int)  # 转换为数组对象
    member_kill_sum_count = (np.argsort(-member_kill_sum))[:5]  # argsort（-x）函数返回的是数组值从大到小的索引值

    member_top5_name = [info_dict['队员名称'][member_kill_sum_count[i]] for i in range(5)]
    member_top5_position = [info_dict['位置'][member_kill_sum_count[i]] for i in range(5)]
    member_top5_kill_sum = [info_dict['总击杀'][member_kill_sum_count[i]] for i in range(5)]

    info_list = [(member_top5_name[i], member_top5_position[i],member_top5_kill_sum[i]) for i in range(5)]

    db,cur = mysql()
    try:

        cur.execute("DROP TABLE IF EXISTS 个人排行榜前五")
        set_sql_member_top5 = """
                        create table 个人排行榜前五(
                        队员名称 varchar(20),
                        位置 varchar(10),
                        总击杀 varchar(10))
                          """
        cur.execute(set_sql_member_top5)
        db.commit()

        save_sql_member5 = "INSERT INTO 个人排行榜前五 values(%s,%s,%s);"
        cur.executemany(save_sql_member5,info_list)
        db.commit()
        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)

def member_mvp_top12():
    info_dict = member()
    mvp_int = [int(kill) for kill in info_dict['mvp次数']]
    member_mvp = np.array(mvp_int)  # 转换为数组对象
    member_mvp_count = (np.argsort(-member_mvp))[:12]  # argsort（-x）函数返回的是数组值从大到小的索引值

    member_mvp_top12_name = [info_dict['队员名称'][member_mvp_count[i]] for i in range(12)]
    member_mvp_top12_out_count = [info_dict['出场次数'][member_mvp_count[i]] for i in range(12)]
    member_mvp_top12_kill_sum = [info_dict['总击杀'][member_mvp_count[i]] for i in range(12)]
    member_mvp_top12_as_sum = [info_dict['总辅助'][member_mvp_count[i]] for i in range(12)]
    member_mvp_top12_die_sum = [info_dict['总死亡'][member_mvp_count[i]] for i in range(12)]

    info_list = [(member_mvp_top12_name[i], member_mvp_top12_out_count[i], member_mvp_top12_kill_sum[i],
                  member_mvp_top12_as_sum[i],member_mvp_top12_die_sum[i],) for i in range(12)]

    db,cur = mysql()
    try:

        cur.execute("DROP TABLE IF EXISTS 个人MVP前十二")
        set_sql_member_mvp = """
                            create table 个人MVP前十二(
                            队员名称 varchar(20),
                            出场次数 varchar(10),
                            总击杀 varchar(10),
                            总助攻 varchar(10),
                            总死亡 varchar(10))
                              """
        cur.execute(set_sql_member_mvp)
        db.commit()

        save_sql_member_top12 = "INSERT INTO 个人MVP前十二 values(%s,%s,%s,%s,%s);"
        cur.executemany(save_sql_member_top12,info_list)
        db.commit()
        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)

def home_round():
    tema_info_dict = teamrank()
    member_info_dict = member()

    # 首页圆圈一
    win_rate_array = np.array(tema_info_dict['胜率'])  # 转换为数组对象
    win_rate_past_count = np.argsort(-win_rate_array)  # argsort（-x）函数返回的是数组值从大到小的索引值
    team_rate_top1_name = tema_info_dict['队名'][win_rate_past_count[0]]
    team_rate_top1_win = tema_info_dict['胜场'][win_rate_past_count[0]]
    team_rate_top1_loss = tema_info_dict['败场'][win_rate_past_count[0]]

    # 首页圆圈二
    kill_top1_array = [int(i) for i in tema_info_dict['总击杀']]
    kill_top1_array = np.array(kill_top1_array)
    kill_top1_array_count = np.argsort(-kill_top1_array)
    kill_top1_name = tema_info_dict['队名'][kill_top1_array_count[0]]
    kill_top1_kill = tema_info_dict['总击杀'][kill_top1_array_count[0]]
    kill_top1_die = tema_info_dict['总死亡'][kill_top1_array_count[0]]

    #首页圆圈三
    eye_top1_array = np.array(tema_info_dict['插眼'])
    eye_top1_array_count = np.argsort(-eye_top1_array)
    eye_top_name = tema_info_dict['队名'][eye_top1_array_count[0]]
    eye_top_pl = tema_info_dict['插眼'][eye_top1_array_count[0]]
    eye_top_ki = tema_info_dict['排眼'][eye_top1_array_count[0]]

    #首页圆圈四
    kda_top1_index = member_info_dict['队员名称'].index('V5y4')
    kda_top1_kill = member_info_dict['总击杀'][kda_top1_index]
    kda_top1_as = member_info_dict['总辅助'][kda_top1_index]
    kda_top1_die = member_info_dict['总死亡'][kda_top1_index]
    kda_ka = int(kda_top1_kill)+int(kda_top1_as)

    #首页圆圈五
    die_top1 = [int(i) for i in member_info_dict['总死亡']]
    die_top1_array = np.array(die_top1)
    die_top1_array_index = np.argsort(-die_top1_array)
    die_top1_name = member_info_dict['队员名称'][die_top1_array_index[0]]
    die_top1_as = member_info_dict['总辅助'][die_top1_array_index[0]]
    die_top1_kill= member_info_dict['总击杀'][die_top1_array_index[0]]
    die_top1_die= member_info_dict['总死亡'][die_top1_array_index[0]]
    die_ka = int(die_top1_as)+int(die_top1_kill)

    #首页圆圈六
    member_kill_top1 = [int(i) for i in member_info_dict['总击杀']]
    member_kill_top1_array = np.array(member_kill_top1)
    member_kill_top1_array_index = np.argsort(-member_kill_top1_array)
    member_kill_top1_name = member_info_dict['队员名称'][member_kill_top1_array_index[0]]
    member_kill_top1_kill = member_info_dict['总击杀'][member_kill_top1_array_index[0]]
    member_kill_top1_as = member_info_dict['总辅助'][member_kill_top1_array_index[0]]
    member_kill_top1_die = member_info_dict['总死亡'][member_kill_top1_array_index[0]]
    member_kill_top1_da = int(member_kill_top1_die)+int(member_kill_top1_as)

    info_list = [(team_rate_top1_name,team_rate_top1_win,team_rate_top1_loss),
                 (kill_top1_name,kill_top1_kill,kill_top1_die),
                 (eye_top_name,eye_top_pl,eye_top_ki),
                 ('V5y4',kda_ka,kda_top1_die),
                 (die_top1_name,die_top1_die,die_ka),
                 (member_kill_top1_name,member_kill_top1_kill,member_kill_top1_da)]

    db,cur = mysql()
    try:

        cur.execute("DROP TABLE IF EXISTS 首页圆圈数据")
        set_sql_home_data = """
                            create table 首页圆圈数据(
                            name varchar(20),
                            data1 varchar(10),
                            data2 varchar(10))
                              """
        cur.execute(set_sql_home_data)
        db.commit()

        save_sql_home_data = "INSERT INTO 首页圆圈数据 values(%s,%s,%s);"

        db.commit()
        cur.executemany(save_sql_home_data,info_list)
        db.commit()
        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)

def hero():
    hero_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HERORANK_LIST_134_7_8.js'
    hero_name_api = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    info = get_info(hero_api)
    get_info_name = get_info(hero_name_api)
    info = json.loads(info)
    info_msg = info['msg']#英雄详细数据
    hero_key_id = [data['iChampionId'] for data in info_msg]#英雄对应的ID
    hero_out_count = [data['iAppearancesFrequency'] for data in info_msg]#英雄出场次数
    hero_pick = [int(float(data['sAveragingPick'])*100) for data in info_msg]#英雄pick率
    hero_win_rate = [int(float(data['sAveragingWin'])*100) for data in info_msg]#英雄胜率

    hero_pick_array = np.array(hero_pick)
    hero_pick_array_index = np.argsort(-hero_pick_array)[:60]#pick率top60对应的索引值
    hero_key_id_top60 = [hero_key_id[i] for i in hero_pick_array_index]#英雄id前60
    hero_out_count_top60 = [hero_out_count[i] for i in hero_pick_array_index]#英雄出场次数前60
    hero_pick_top60 = [hero_pick[i] for i in hero_pick_array_index]#英雄pick率前60
    hero_win_rate_top60 = [hero_win_rate[i] for i in hero_pick_array_index]#英雄胜率前60

    get_hero_name_dict = json.loads(get_info_name)
    hero_name_id_list = [i['heroId'] for i in get_hero_name_dict['hero']]#所有英雄对应的id
    hero_name_list = [i['name'] for i in get_hero_name_dict['hero']]#所有英雄名字
    name = []
    for i in hero_key_id_top60:
        for j in hero_name_id_list:
            if i == j :
                #由于从lpl数据页面无法获取到英雄名称，只能获取到对应的id
                #一层循环是pick率前60的英雄id，二层是所有英雄的的id
                #通过if判断，将pick率前60的英雄写入到指定列表中
                name.append(hero_name_list[hero_name_id_list.index(j)])

    info_list = [(name[i],hero_out_count_top60[i],str(hero_pick_top60[i])+'%',str(hero_win_rate_top60[i])+'%')
                 for i in range(60)]

    db,cur = mysql()
    try:

        cur.execute("DROP TABLE IF EXISTS 英雄pick率前六十")
        set_sql_hero_top60 = """
                            create table 英雄pick率前六十(
                            英雄名称 varchar(20),
                            出场次数 varchar(10),
                            pick比率 varchar(10),
                            胜率 varchar(10))
                              """
        cur.execute(set_sql_hero_top60)
        db.commit()

        save_sql_hero_top60 = "INSERT INTO 英雄pick率前六十 values(%s,%s,%s,%s);"
        cur.executemany(save_sql_hero_top60,info_list)
        db.commit()
        print("写入数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)


if __name__ == '__main__':
    team_top5()
    team_rate_top12()
    member_top5()
    member_mvp_top12()
    home_round()
    hero()
