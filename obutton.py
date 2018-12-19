#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:45:23 2018

@author: kasaran
Buttons
"""
from graphics import *

class Button:
    '''Button class'''
    
    def __init__ (self, p1, p2, text, color = 'snow'):
        '''p1 & p2 are points that are opposite corners of this Button
        
        code builds a Rectangle and ensures that p1 has smaller x,y values
        than p2
        
        text becomes label of the Button
        '''
        if p1.getX() < p2.getX():
            x1 = p1.getX()
            x2 = p2.getX()
        else:
            x2 = p1.getX()
            x1 = p2.getX()
            
        if p1.getY() < p2.getY():
            y1 = p1.getY()
            y2 = p2.getY()
        else:
            y2 = p1.getY()
            y1 = p2.getY()
        
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        
        x1 = self.rect.getP1().getX()
        x2 = self.rect.getP2().getX()
        y1 = self.rect.getP1().getY()
        y2 = self.rect.getP1().getY()
        
        x = x1 + (x2 - x1) / 2
        y = y2 - (y2 - y1) / 2 + 10
        
        self.center = Point(x, y)
        
        self.label = Text(self.center, text) 
        
        self.color = self.rect.setFill(color)
        
    def draw(self, window):
        '''draws Button in a Graphwin object
        '''
        self.rect.draw(window)
        self.label.draw(window)
    
    def is_clicked(self, point):
        '''return True if point is inside Button
        '''
        if point.getX() >= self.rect.getP1().getX() and point.getX() <= \
        self.rect.getP2().getX() and point.getY() <= self.rect.getP2().getY() \
        and point.getY() >= self.rect.getP1().getY():
            return True
        return False
        
    def textSize(self, size):
        self.label.setSize(size)

    def undraw(self):
       self.rect.undraw()
       self.label.undraw()
    