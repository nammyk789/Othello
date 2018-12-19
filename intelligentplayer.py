#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:20:11 2018

@author: namratakasaraneni

used in othello.py
"""

class IntelligentPlayer:
    '''plays against a human at othello with some
    level of intelligence
    '''
    
    def __init__(self, game):
        self.game = game
        self.color = self.game.CPU_color
    
    def total_flips(self, c, r):
        '''calculates the total tiles that would be flipped
        by a legal move
        '''
        flips = 0
        if self.game.legal_move(c, r, self.color) != False:
            for item in self.game.surroundings(c, r, self.color):
                dc = item[0] - c
                dr = item[1] - r
                if self.game.pathways(c, r, dc, dr, self.color) != False:
                    flips = flips + len(self.game.pathways(c, r, dc, 
                                      dr, self.color))
        return flips
    
    def contain(self):
        '''keeps moves in the square surrounding the starting positions
        '''
        options = []
        for item in self.game.key:
             if item[0] > 2 and item[0] < 7 and item[1] > 2 and item[1] < 7:
                 if self.game.legal_move(item[0], item[1], self.color) != False:
                     if self.game.surroundings(item[0], item[1], self.color) != False:
                         for i in self.game.surroundings(item[0], item[1], self.color):
                             dc = i[0] - item[0]
                             dr = i[1] - item[1]
                             if self.game.pathways(item[0], item[1], 
                                                   dc, dr, self.color) != False:
                                 options.append(item)
        if len(options) > 0:
            return options
        return False
    
    def corners(self):
        '''tests if the corners of the board are available to move in
        
        returns list of corners that are available
        returns false if all corners unavailable
        '''
        corners = [(1, 1), (1, 8), (8, 1), (8, 8)]
        options = []
        for item in corners:
            if self.game.legal_move(item[0], item[1], self.color) != False:
                if self.game.key[item] == 0:
                    if self.game.surroundings(item[0], item[1], self.color) != False:
                         for i in self.game.surroundings(item[0], item[1], self.color):
                             dc = i[0] - item[0]
                             dr = i[1] - item[1]
                             if self.game.pathways(item[0], item[1], 
                                                   dc, dr, self.color) != False:
                                 options.append(item)
                
        if len(options) > 0:
            return options
        return False
    
    def edges(self):
        options = []
        for item in self.game.key:
            if item[0] == 1 or item[0] ==8 or item[1] == 1 or item[1] == 8:
                if self.game.legal_move(item[0], item[1], self.color) != False:
                         if self.game.surroundings(item[0], item[1], self.color) != False:
                             for i in self.game.surroundings(item[0], item[1], self.color):
                                 dc = i[0] - item[0]
                                 dr = i[1] - item[1]
                                 if self.game.pathways(item[0], item[1], 
                                                       dc, dr, self.color) != False:
                                     options.append(item)
        if len(options) > 0:
            return options
        return False
        
    def max_list(self, options):
        '''finds the move in list options that
        would flip the most tiles
        '''
        maxi = 0
        c = -1
        r = -1
        for item in options:
            if self.total_flips(item[0], item[1]) > maxi:
                    maxi = self.total_flips(item[0], item[1])
                    c = item[0]
                    r = item[1]
        return c, r
        
    def max_flips(self):
        '''finds the move on the board that would flip
        the most tiles
        '''
        maxi = 0
        c = -1
        r = -1
        for item in self.game.key:
            if self.game.key[item] == 0:
                if self.total_flips(item[0], item[1]) > maxi:
                    maxi = self.total_flips(item[0], item[1])
                    c = item[0]
                    r = item[1]
        return c, r 
    
    def move(self):
        '''moves to a strategic location on the board based on availability
        and based on the number of tiles that would be flipped by that move
        '''
        c = -1
        r = -1
        if self.game.level == 1:
            c, r = self.max_flips()
            self.game.CPU_move(c, r)
        elif self.game.level == 2:
            if self.contain() != False:
                c, r = self.max_list(self.contain())
            else:
                c, r = self.max_flips()
            self.game.CPU_move(c, r)
        else:    
            if self.corners() != False:
                c, r = self.max_list(self.corners())
            elif self.edges() != False:
                c, r = self.max_list(self.edges())
            elif self.contain() != False:
                c, r = self.max_list(self.contain())
            else:
                c, r = self.max_flips()
            self.game.CPU_move(c, r)