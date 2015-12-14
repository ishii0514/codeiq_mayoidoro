#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ishii0514'
import fileinput
import unittest


def test():
    unittest.main()

class TestMayoi(unittest.TestCase):

    def setUp(self):
        self.mayoi = Mayoi()

    def test_mayoi(self):
        test_set = [
            {'in': 0, 'exp': 0},
            {'in': 1, 'exp': 2},
            {'in': 2, 'exp': 2},
            {'in': 3, 'exp': 7},
            {'in': 4, 'exp': 7},
            {'in': 5, 'exp': 20},
            {'in': 6, 'exp': 20},
            {'in': 7, 'exp': 54},
            {'in': 10, 'exp': 143},
            {'in': 15, 'exp': 2583},
            {'in': 23, 'exp': 121392},

            {'in': 31, 'exp': 5702886},
            {'in': 50, 'exp': 32951280098},
            {'in': 100, 'exp': 927372692193078999175L},
            {'in': 1000, 'exp': 113796925398360272257523782552224175572745930353730513145086634176691092536145985470146129334641866902783673042322088625863396052888690096969577173696370562180400527049497109023054114771394568040040412172632375L},
            {'in': 2015, 'exp': 24410294683171395267259945469996127000411199333760853190535535281681195871429510314079442068798555059453792431772087225245168879580469159794544170936403149540819320510882801573596907938222922817134288725100817648047405608500267748766714030468003650259685406411646787207097050545802045736020993909154298598218721111963426993884619351338577630868510716463423585020972878819198991971234596733617320373133963970742975210614208L},
        ]
        for test in test_set:
            self.mayoi.setN(test['in'])
            self.mayoi.root_count()
            self.assertEqual(self.mayoi.root_num, test['exp'])


def main():
    mayoi = Mayoi()
    for line in fileinput.input():
        n = int(line.strip())
        mayoi.setN(n)
        mayoi.root_count()

        print str(mayoi.root_num),


class Mayoi:
    def __init__(self):
        self.n = 0
        self.maxlayer = 0
        self.root_num = 0L

    def setN(self, n):
        """
        :param n:反転数
        :return:
        """
        #偶数なら一つ小さい奇数にする
        if n > 0 and n % 2 == 0:
            n -= 1
        self.n = n
        self.maxlayer = self.n * 2
        #ルートの数
        self.root_num = 0L

    def root_count(self):
        if self.n == 0:
            return
        self.calc_by_list()

    def calc_by_list(self):
        last_nums = [1, 0]
        for i in range(1, self.n+1):
            #n*2の範囲が必要
            list_len = i*2+1
            #次の階層の計算用に＋1する。
            current_nums = [0L]*(list_len+1)
            for j in range(i,list_len):
                current_nums[j] = last_nums[j-1]
                if j % 2 == 0:
                    current_nums[j] += current_nums[j-1]
            if i % 2 == 1:
                self.root_num += sum(current_nums)
            last_nums = current_nums

    def root_count_by_tree(self):
        if self.n == 0:
            return
        self.root_num += 1
        self.calc_by_tree(1, [1])

    def calc_by_tree(self, last_layer=1, last_numlist=[1]):
        """
        :param last_layer:一つ前の階層
        :param last_numlist:一つ前の反転数リスト
        :return:現階層の班点数リスト
        """
        layer = last_layer + 1
        if layer > self.maxlayer:
            return
        new_numlist = []
        if layer % 2 == 0:
            for i in last_numlist:
                if i < self.n:
                    new_numlist += [i, i+1]
                elif i == self.n:
                    new_numlist += [i]
        else:
            new_numlist = [i+1 for i in last_numlist if i < self.n]
        self.count_root_num(new_numlist)

        self.calc(layer, new_numlist)

    def count_root_num(self, numlist):
        self.root_num += len([i for i in numlist if i <= self.n and i % 2 == 1])


if __name__ == '__main__':
    #main()
    test()
