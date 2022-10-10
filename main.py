import random
import numpy as np
import csv
import os


def random_information():  # 随机生成信息
    # 百家姓姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫"
    firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    # 女孩名字
    girl = '含烟含玉涵菡晗蕾涵韵晗玥寒凝香寒雁和悌和美和怡和雅和璧和玉和暖红螺虹雨英虹颖虹影怀玉慧颖慧雅慧美慧捷慧丽慧月慧云慧俊慧秀慧巧慧英慧艳浩岚红豆红雪红英云红旭红香红艳家美家欣家馨佳悦嘉怡嘉宝嘉歆嘉美嘉云嘉玉嘉丽嘉淑嘉懿洁玉晶滢静曼静涵静逸静姝静婉慧静云秀娟秀娟妍娟丽娟巧兰若兰蕙兰梦兰泽兰芝兰英兰娜岚霏岚彩乐心乐悦乐容乐英丽泽丽华丽雅丽芳丽佳丽姿珠丽容丽文灵秀灵韵灵慧灵卉灵萱玲玲玲珑凌波凌春凌霜凌雪莉莉曼蔓曼冬曼青曼容曼文曼妮曼云曼衍曼丽曼语曼辞曼珠曼音曼吟美丽美华米琪梦凡梦菲梦菡梦露梦琪梦秋梦竹妙晴玛丽茉莉麦冬'
    # 男孩名字
    boy = '炫迁铭晋胜池信磊峻越谦元海钟任元冰朋韶然祺旷宁靖奥若钟涛苛勤含棕宏羽肃义望卫健轩皓南文谦苛敬圣渊聪闻彰豫原鸿乐洋昆文基飘妙茂方勉昭善恒昆擎利意楷商虎卫圆肖钟波向群乐惜石尘生信星博卡伟悟茂松鸣利神实际永余民渊旷盛誓睿名壮际翼宁冠浦刊圣文韶境笃音高伯境逸民阳磊昙彤桦翰景幽原翔福镇鸽雷浚理悠廉清年韵欧景文幽青怀浅胜宜胜庭岳宜逸载奇裕国善凯兼展震笃意羽泰浅如泰忆阳凌昙游浩雄世宇宜瑾川越神神瑞傲朴宜惜庭本岸煜厚清观乾彤轩健扬鼎棕山星蒙淘挚悠丰浚卡祥辉峰毅贤峰善高翱弘本烨思净耀坤伦勋蒙德秀宁'
    # 名
    name = '真中凯歌易仁器义礼智信友'
    #是否班委
    choose ='是否'

    if random.choice(range(100)) > 3:
        firstName_name = firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        if i // 2 == 0:
            i += 1
        firstName_name = firstName2[i:i + 2]

    sex = random.choice(range(2))#性别

    banwei = random.choice(choose) #是否班委

    grade = random.choice(np.random.normal(3, 1, 1)) #绩点

    while grade>4 or grade<1.5:
        grade = random.choice(np.random.normal(3, 1, 1))
    name_1 = ""
    flagg=0
    if random.choice(range(2)) > 0:
        name_1 = name[random.choice(range(len(name)))]


    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        data = firstName_name + name_1 + girl_name + "," + '女' + ',' + banwei + ',' + str(round(grade,3))
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        data = firstName_name + name_1 + boy_name + ',' + '男' + ',' + banwei + ',' + str(round(grade,3))
    return data


def main():
    with open('E:\\软件工程.csv', 'w') as m:
        msg1 =  '姓名' + ',' + '性别' + ',' + '是否班委' + ',' + '绩点' + ',' + '出勤概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('E:\\概率论.csv', 'w') as m:
        msg1 =  '姓名' + ',' + '性别' + ',' + '是否班委' + ',' + '绩点' + ',' + '出勤概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('E:\\数据库.csv', 'w') as m:
        msg1 = '姓名' + ',' + '性别' + ',' + '是否班委' + ',' + '绩点' + ',' + '出勤概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('E:\\操作系统.csv', 'w') as m:
        msg1 = '姓名' + ',' + '性别' + ',' + '是否班委' + ',' + '绩点' + ',' + '出勤概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('E:\\接口技术.csv', 'w') as m:
        msg1 = '姓名' + ',' + '性别' + ',' + '是否班委' + ',' + '绩点' + ',' + '出勤概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))


N = 90
main()