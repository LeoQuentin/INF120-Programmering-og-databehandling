# -*- coding: utf-8 -*-
"""Created on Sun Sep 18 13:07:22 2022
__author__ = "Leo Quentin Bækholt"
__email__ = "leo.quentin.thorbjornsen.bakholt@nmbu.no"
"""

innsamling_hist = [
    [2015, 86343, 123],
    [2016, 93512, 125],
    [2017, 83935, 119],
    [2018, 91274, 128],
    [2019, 88935, 127],
    [2020, 95182, 132],
    ]

money_per_person = lambda data: (data[1] / data[2])
DictofMoney = { i[0] : money_per_person(i) for i in innsamling_hist }
print(DictofMoney)
#del 1
for key, value in DictofMoney.items(): print(f"{key} : {'{:.2f}'.format(value)}kr/bøssebærer")

# del 2
print(f"Året med flest penger samlet per bøssebærer var {max(DictofMoney, key=DictofMoney.get)} med {'{:.2f}'.format(max(DictofMoney.values()))}kr per bøssebærer")
# året med mest innsamlet penger per bøssebærer var 2016.
