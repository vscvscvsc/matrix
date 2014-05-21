# -*- coding: utf-8 -*- 
from numpy import *
import random
import time  
import os  

time_begin = time.clock()  


def init_set():
	ret = []
	for i in range(1, 11):
		for j in range(1, 11):
			for k in range(1, 11):
				for l in range(1, 11):
					for m in range(1, 11):
						ret.append((i, j, k, l,m))
	return ret

allposition = init_set() #循环出5个关键词的所有位置的组合
number = 0
allkeymatrix  = []
alljisuan = []

for position in allposition:

	#计算关键词矩阵
	key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #未填充数值的矩阵
	keymatrix = []
	for row in range(0,5):
		keymatrix.append(key)
	#print keymatrix

	#print "___________________________"

	#计算花费矩阵
	key = [0,0,0,0,0] #未填充数值的矩阵
	costmatrix = []
	for row in range(0,10):
		costmatrix.append(key)
	#print costmatrix


	def  posicost(position):  #根据排名随机花费
		cost = []
		for row in position:
			cost.append(random.randint(50,150)/row)
		return cost
	givemeacost = posicost(position)
	# print "根据排名随机花费"
	# print givemeacost


	def  posiconversion(position):  #根据排名随机转化
		conversion = []
		for row in position:
			conversion.append(random.randint(1,20)/row)
		return conversion
	givemeaconversion = posiconversion(position)
	# print "根据排名随机转化"
	# print givemeaconversion

	def keywork(position):#计算关键词矩阵
		keymatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(0,5)]
		num = 0
		for row in range(0,5):
			keymatrix[num][position[row]-1] = 1
			num+=1
		#print "关键词矩阵是"
		return keymatrix


	def costwork(position,givemeacost):#计算花费矩阵
		costmatrix = [[0, 0, 0, 0, 0] for i in range(0,10)]
		add = 160
		for hang in range(0,10):
			add -=15
			for lie in range(0,5):
				ran = random.randint(0,lie) +8
				costmatrix[hang][lie] = random.randint(add-ran,add)
		# num = 0
		# for costs in givemeacost:
		# 	#print costs
		# 	costmatrix[position[num]-1][num] = costs
		# 	num +=1
		# num = 0
		#print "花费矩阵是"
		return costmatrix

	def conversionwork(position,givemeacost): #计算转化矩阵
		conversionmatrix = [[0, 0, 0, 0, 0] for i in range(0,10)]
		add = 32
		for hang in range(0,10):
			add -=3
			for lie in range(0,5):
				ran = random.randint(0,lie) +1
				conversionmatrix[hang][lie] = random.randint(add-ran,add)
		# num = 0
		# for conversions in givemeacost:
		# 	#print costs
		# 	conversionmatrix[position[num]-1][num] = conversions
		# 	num +=1
		# num = 0
		#print "转化矩阵是"
		return conversionmatrix

	keymatrix = keywork(position) #计算出关键词的矩阵
	allkeymatrix.insert(number, keymatrix) #保存该关键词矩阵
	#print keymatrix
	costmatrix = costwork(position,givemeacost) #计算出花费的矩阵
	#print costmatrix
	conversionmatrix = conversionwork(position,givemeaconversion) #计算出转化的矩阵
	#print conversionmatrix
	# print "-----------------------------------------"
	# print "-----------------------------------------"
	# print "矩阵乘法计算!"
	# print "-----------------------------------------"
	# print "-----------------------------------------"
	# print "下面是关键词*花费"
	map(list,dot(keymatrix,costmatrix))
	# print "-----------------------------------------"
	#print "下面是关键词*转化"
	map(list,dot(keymatrix,conversionmatrix))
	# print "-----------------------------------------"

	# print "-----------------------------------------"
	# print "-----------------------------------------"
	# print "矩阵对角线计算!"
	# print "-----------------------------------------"
	# print "-----------------------------------------"
	num = 1
	jisuan1 = 0
	x = map(list,dot(keymatrix,costmatrix))
	for y in x:
		jisuan1 += y[num-1]
		#print y[num]
		num +=1
	#print "下面是关键词*花费的对角线值"
	#print jisuan

	num = 1
	jisuan2 = 0
	x = map(list,dot(keymatrix,conversionmatrix))
	for y in x:
		jisuan2 += y[num-1]
		#print y[num]
		num +=1
	#print "下面是关键词*转化的对角线值"
	#print jisuan


	alljisuan.insert(number, [jisuan1,jisuan2])


	number +=1

num = 0
for x in alljisuan:
	num +=1
print "total number is %d "%num
print "Use time: %s" % (time.clock() - time_begin)



target = open('duijiao.txt', 'w')
for row in alljisuan:
	#print row
	givemestring = "%s,%s \n" % (row[0],row[1])
	target.write(givemestring)


target = open('keywordmatrix.txt', 'w')
for position in allposition:
	givemestring = "%s,%s,%s,%s,%s \n" % (position[0],position[1],position[2],position[3],position[4])
	target.write(givemestring)
