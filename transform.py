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























