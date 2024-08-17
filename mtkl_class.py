# 模拟凯利公式
import random
import os


class Mtkl:
    """
    beg:本金，默认是1
    p:胜率，0-1 之间，浮点数
    p_gain:盈利比例
    q_lost:亏损比例
    number:模拟下注次数
    egg:存放期末本金的列表
    """
    def __init__(self, beg, cangwei, p, p_gain, q_lost, number):
        self.beg = beg
        self.cangwei = cangwei
        self.p = p
        self.p_gain = p_gain
        self.q_lost = q_lost
        self.number = number
        self.egg = []

    def run(self):
        """
        模拟循环下注。
        """
        f = open('kaili.csv', 'w', encoding='utf8')
        f.write(f'次序,期初本金,盈亏比例,盈亏\n')
        for i in range(self.number):
            gainrate = random.choices([self.p_gain, self.q_lost], [self.p, 1-self.p])[0]
            gain = self.beg * self.cangwei * gainrate
            print('*******')
            print(f'第{i}次模拟')
            print(f'期初本金:{round(self.beg,2)}\n仓位:{self.cangwei}\n盈亏率：{gainrate}')
            print(f'盈亏金额:{round(gain,2)}')
            self.beg += gain
            print(f'期末本金:{round(self.beg,2)}')
            self.egg.append(self.beg)
            f.write(f'{i},{round(self.beg, 2)},{round(gainrate, 2)},{round(gain, 2)}\n')
            f.flush()
            print('########\n\n')
            if self.beg <= 0.05 :
                print("收手吧，阿祖！")
                break
        f.close()

        

if __name__ == "__main__":
    print(os.getcwd())
    print("初始资金默认是1，请设置模拟的各项参数：")
    print("仓位:   小数，0-1之间，大于1则是杠杆")
    print('胜率：  小数，0-1之间')
    print('盈利率：小数，0-1之间')
    print('亏损率：负小数， -1-0之间')
    print("******************")
    cangwei = float(input('请设置仓位：'))
    p = float(input('请设置胜率：'))
    p_gain = float(input('请设置盈利率：'))
    q_lost = float(input('请设置亏损率(负数)：'))
    num = int(input('请设置模拟次数：'))
    mt = Mtkl(1, cangwei,p, p_gain, q_lost, num)
    mt.run()

    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.suptitle('凯利公式模拟')
    ax.plot(range(len(mt.egg)), mt.egg)
    print('资金最高点是:',max(mt.egg))
    plt.show()
    input("模拟结果已写入当前目录下kaili.csv文件。输入任意值后按回车退出。")
