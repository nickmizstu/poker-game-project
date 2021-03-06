import csv
import itertools
import numpy as  np
import pandas as pd




carddeck = []

pict = ['h', 's', 'd', 'c']

for i in range(2, 15):
    for j in pict:
        carddeck.append(str(i)+j)


# print(carddeck)

# separate the card into number and pitcure
class card(object):
    def num(self, name):
        self.name = name
        num = name[:-1]
        return (int(num))

    def pic(self, name):
        self.name = name
        pic = name[-1]
        return (pic)


'''		
x = card()
print(x.num('13s'))
print(x.pic('11j'))
'''


class handclass(card):
    def hand(self, h1, h2, h3, h4, h5):
        x = card()
        # sort the numbers
        tnl = [x.num(h1), x.num(h2), x.num(h3), x.num(h4), x.num(h5)]
        nl = sorted(tnl)
        # get the picture
        p = [x.pic(h1), x.pic(h2), x.pic(h3), x.pic(h4), x.pic(h5)]
        # rank the hand
        if nl[0]+4 == nl[1]+3 == nl[2]+2 == nl[3]+1 == nl[4] and p[0] == p[1] == p[2] == p[3] == p[4]:
            return (9)
            #print('Straight flush!!')

        elif nl[0]+12 == nl[1]+11 == nl[2]+10 == nl[3]+9 == nl[4] == 14 and p[0] == p[1] == p[2] == p[3] == p[4]:
            return (9)
            #print('Straight flush!!')
        
        elif nl[0] == nl[1] == nl[2] == nl[3] or nl[1] == nl[2] == nl[3] == nl[4]:
            return (8)
            #print('Four cards!!')

        elif nl[0] == nl[1] == nl[2] and nl[3] == nl[4] or nl[0] == nl[1] and nl[2] == nl[3] == nl[4]:
            return (7)
        #	print('Full house!!')

        elif p[0] == p[1] == p[2] == p[3] == p[4]:
            return (6)
        #	print('Flush!!')

        elif nl[0]+4 == nl[1]+3 == nl[2]+2 == nl[3]+1 == nl[4] or nl[0]+12 == nl[1]+11 == nl[2]+10 == nl[3]+9 == nl[4] == 14:
            return (5)
            # print('Straight!!')

        elif nl[0] == nl[1] == nl[2] or nl[1] == nl[2] == nl[3] or nl[2] == nl[3] == nl[4]:
            return (4)
            #print('Three cards!!')

        elif nl[0] == nl[1] and nl[2] == nl[3] or nl[0] == nl[1] and nl[3] == nl[4] or nl[1] == nl[2] and nl[3] == nl[4]:
            return (3)
            #print('Two pair!!')

        elif nl[0] == nl[1] or nl[1] == nl[2] or nl[2] == nl[3] or nl[3] == nl[4]:
            return (2)
            #print('One pair!!')

        else:
            return (1)
        #	print('High card!!')


class handpoint(handclass):
    def points(self, myhand):
        #handlist = ('high card!!','one pair!!','two pair!!','three cards!!','straight!!','flush!!','fullhouse!!','four cards!!','stright flush!!')

        if len(myhand) != len(set(myhand)):
            return 0
        
        else:
            ah = []
            # checking all 5 card conbination
            for v in itertools.combinations(myhand, 5):
                # returning the point and sort
                ah += str(handclass.hand(self, v[0], v[1], v[2], v[3], v[4]))
                ag = sorted(ah)
                # printing the highest point
                return ag[-1]
    



with open('pro.csv','a') as f:
    writer = csv.writer(f)
    columnlist = ['',]
    for c in itertools.combinations(carddeck,2):
        columnlist.append(c)

    writer.writerow(columnlist)

    for t in itertools.combinations(carddeck,5):
        body_list = [t]
        for c in itertools.combinations(carddeck,2):        
            myhand = list(c) + list(t)
            point = handpoint()
            p = point.points(myhand)
            body_list.append(p)
            
        writer.writerow(body_list)
        

