from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np

def translate(elem, Tx, Ty):
	TM = np.matrix([[1,0,0],[0,1,0],[Tx,Ty,1]])
	point_arr = []
	for p in elem.object.point_arr:
		a = np.array([p.x(), p.y(), 1])
		x,y,_ = np.array(a*TM)[0]
		point_arr.append(QPoint(x,y))
	elem.updatePoints(point_arr)

def rotate(elem, cx, cy, angle):
	TM1 = np.matrix([[1,0,0],[0,1,0],[-cx,-cy,1]])
	TM2 = np.matrix([[1,0,0],[0,1,0],[cx,cy,1]])
	RM = np.matrix([[np.cos(angle*np.pi/180), np.sin(angle*np.pi/180), 0],
					[-np.sin(angle*np.pi/180), np.cos(angle*np.pi/180), 0],
					[0, 0, 1]])
	point_arr = []
	for p in elem.object.point_arr:
		a = np.array([p.x(), p.y(), 1])
		x,y,_ = np.array(a*TM1*RM*TM2)[0]
		point_arr.append(QPoint(x,y))
	elem.updatePoints(point_arr)

def scale(elem, cx, cy, portion):
	TM1 = np.matrix([[1,0,0],[0,1,0],[-cx,-cy,1]])
	TM2 = np.matrix([[1,0,0],[0,1,0],[cx,cy,1]])
	SM = np.matrix([[portion, 0, 0], 
					[0, portion, 0],
					[0, 0, 1]])
	point_arr = []
	for p in elem.object.point_arr:
		a = np.array([p.x(), p.y(), 1])
		x,y,_ = np.array(a*TM1*SM*TM2)[0]
		point_arr.append(QPoint(x,y))
	elem.updatePoints(point_arr)


def lineClip(lineElem, pLL, pUR, algorithm='Cohen-Sutherland'):	# lower_left, upper_right
	# To be implemented
	if algorithm == 'Cohen-Sutherland':
		CohenSutherland(lineElem, pLL, pUR)
	elif algorithm == 'Liang-Barsky':
		LiangBarsky(lineElem, pLL, pUR)
	else:
		print("Can't clip line! Unknown algorithm.")


def CohenSutherland(lineElem, pLL, pUR):
	# print("CohenSutherland")
	xLL, yLL = pLL.x(), pLL.y()
	xUR, yUR = pUR.x(), pUR.y()
	x0, y0 = lineElem.object.p1.x(), lineElem.object.p1.y()
	x2, y2 = lineElem.object.p2.x(), lineElem.object.p2.y()
	x, y = 0, 0
	c, c1, c2 = 0, encode(xLL, yLL, xUR, yUR, x0, y0), \
				encode(xLL, yLL, xUR, yUR, x2, y2)
	# print(c1, c2)
	if c1==0 and c2==0:
		return ;
	else:
		while c1!=0 or c2!=0:
			if c1 & c2:
				lineElem.object.setP1(QPoint(0, 0))
				lineElem.object.setP2(QPoint(0, 0))
				# print("No line left")
				lineElem.updatePoints([])
				return ;
			c = c2 if c1==0 else c1
			if c & 1 == 1:
				x, y = xLL, y0+(y2-y0)*(xLL-x0)/(x2-x0)
			elif c & 2:
				x, y = xUR, y0+(y2-y0)*(xUR-x0)/(x2-x0)
			elif c & 4:
				x, y = x0+(x2-x0)*(yLL-y0)/(y2-y0), yLL
			elif c & 8:
				x, y = x0+(x2-x0)*(yUR-y0)/(y2-y0), yUR
			if c == c1:
				x0, y0 = x, y
				c1 = encode(xLL, yLL, xUR, yUR, x, y)
			else:
				x2, y2 = x, y
				c2 = encode(xLL, yLL, xUR, yUR, x, y)
		lineElem.object.setP1(QPoint(x0, y0))
		lineElem.object.setP2(QPoint(x2, y2))
		# print("from {} to {}".format((x0, y0), (x2, y2)))
		lineElem.updatePoints([]) 


def encode(xLL, yLL, xUR, yUR, x, y):
	if x < xLL:
		if y < yLL:
			return 5
		elif yLL <= y <= yUR:
			return 1
		else:
			return 9
	elif xLL <= x <= xUR:
		if y < yLL:
			return 4
		elif yLL <= y <= yUR:
			return 0
		else:
			return 8
	else:
		if y < yLL:
			return 6
		elif yLL <= y <= yUR:
			return 2
		else:
			return 10


def LiangBarsky(lineElem, pLL, pUR):
	xLL, yLL = pLL.x(), pLL.y()
	xUR, yUR = pUR.x(), pUR.y()
	x0, y0 = lineElem.object.p1.x(), lineElem.object.p1.y()
	x2, y2 = lineElem.object.p2.x(), lineElem.object.p2.y()
	t0 = t1 = deltax = deltay = 0
	t0, t1 = 0.0, 1.0
	deltax, deltay = x2 - x0, y2 - y0
	Res = True
	t_dict = {"t0":t0, "t1":t1}
	# print(t_dict)
	if not canSeeLine(-deltax, x0-xLL, t_dict): 
		Res = False
	if Res and not canSeeLine(deltax, xUR-x0, t_dict):
		Res = False
	if Res and not canSeeLine(-deltay, y0-yLL, t_dict):
		Res = False
	if Res and not canSeeLine(deltay, yUR-y0, t_dict):
		Res = False
	if not Res:
		lineElem.object.setP1(QPoint(0, 0))
		lineElem.object.setP2(QPoint(0, 0))
		lineElem.updatePoints([])
	else:
		t0, t1 = t_dict["t0"], t_dict["t1"]
		x2, y2 = x0+t1*deltax, y0+t1*deltay
		x0, y0 = x0+t0*deltax, y0+t0*deltay
		# print("from {} to {}".format((x0, y0), (x2, y2)))
		lineElem.object.setP1(QPoint(x0, y0))
		lineElem.object.setP2(QPoint(x2, y2))
		lineElem.updatePoints([]) 


def canSeeLine(q, d, t_dict):
	r = 0
	if q < 0:
		r = d/q
		if r > t_dict["t1"]:
			return False
		elif r > t_dict["t0"]:
			t_dict["t0"] = r
	elif q > 0:
		r = d/q
		if r < t_dict["t0"]:
			return False
		elif r < t_dict["t1"]:
			t_dict["t1"] = r
	elif d < 0:
		return False
	# print(t_dict)
	return True





