#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:05:17 2018

@author: namratakasaraneni

used in othello.py
note: if second player uses CPU_color as their color, then game can become two
human player
"""

import graphics
import obutton as b

class OthelloGraphicInterface:
    '''graphic interface for Othello gameplay between
    user and CPU
    '''
    
    def __init__(self):
        
        #initialize window
        self.win = graphics.GraphWin("Othello", 800, 800)
        
        #player color choice buttons
        self.black = b.Button(graphics.Point(300, 400), graphics.Point(500, 350), 
                              'BLACK', 'black')
        self.black.label.setTextColor('snow')
        self.black.label.move(0, 18)
        self.black.label.setFace('courier')
        self.white = b.Button(graphics.Point(300, 500), graphics.Point(500, 450), 'WHITE')
        self.white.label.setTextColor('black')
        self.white.label.move(0, 20)
        self.white.label.setFace('courier')
        
        #player color
        self.player_color = None
        self.CPU_color = None

        
        #dictionary of board squares & its contents
        self.key = {}
        for c in range(1, 9):
            for r in range(1, 9):
                self.key[(c, r)] = 0
                
        #starting set up
        self.key[(4, 4)] = 1
        self.key[(4, 5)] = -1
        self.key[(5, 4)] = -1
        self.key[(5, 5)] = 1
        
        #difficulty level
        self.level = None
        
    def title(self):
        '''draws title screen
        '''
        background = graphics.Rectangle(graphics.Point(0,0), graphics.Point(799, 799))
        background.setFill('CadetBlue2')
        background.draw(self.win)
        title = graphics.Text(graphics.Point(400, 300), 'Othello')
        title.setFace('courier')
        title.setSize(36)
        title.setStyle('bold')
        title.setTextColor('OrangeRed2')
        title.draw(self.win)
        instruction = graphics.Text(graphics.Point(400, 350), 'click anywhere')
        instruction.setFace('courier')
        instruction.setSize(10)
        instruction.draw(self.win)
        #waits for user click before continuing
        point = self.win.getMouse()
        title.undraw()
        instruction.undraw()
        
    def difficulty(self):
        '''three Buttons giving player options for
        difficulty level of game
        '''
        instruction = graphics.Text(graphics.Point(400, 250), 'What is your quest?')
        instruction.setFace('courier')
        instruction.setSize(36)
        instruction.setTextColor('OrangeRed2')
        instruction.draw(self.win)
        
        easy = b.Button(graphics.Point(300, 400), graphics.Point(500, 350), 
                              'coward', 'CadetBlue2')
        easy.label.setTextColor('OrangeRed2')
        easy.label.setSize(30)
        easy.label.move(0, 23)
        easy.label.setFace('courier')
        easy.rect.setOutline('CadetBlue2')
        medium = b.Button(graphics.Point(300, 450), graphics.Point(500, 400), 
                          'medium', 'CadetBlue2')
        medium.label.setTextColor('OrangeRed2')
        medium.label.setSize(30)
        medium.label.move(0, 23)
        medium.label.setFace('courier')
        medium.rect.setOutline('CadetBlue2')
        hard = b.Button(graphics.Point(300, 500), graphics.Point(500, 450), 
                              'Black Knight', 'CadetBlue2')
        hard.label.setTextColor('OrangeRed2')
        hard.label.setSize(30)
        hard.label.move(0, 23)
        hard.label.setFace('courier')
        hard.rect.setOutline('CadetBlue2')
        
        easy.draw(self.win)
        medium.draw(self.win)
        hard.draw(self.win)
        
        point = self.win.getMouse()
        
        while easy.is_clicked(point) == False and medium.is_clicked(point) \
        == False and hard.is_clicked(point) == False:
             point = self.win.getMouse()
        if easy.is_clicked(point) == True:
            self.level = 1
        elif medium.is_clicked(point) == True:
            self.level == 2
        else:
            self.level == 3
        
        instruction.undraw()
        easy.undraw()
        medium.undraw()
        hard.undraw()
        
    def color_choice(self):
        '''intro screen with Buttons giving player option 
        to play black or white
        returns 1 for black and -1 for white
        '''
        self.black.draw(self.win) 
        self.white.draw(self.win)
        
        instruction = graphics.Text(graphics.Point(400, 200), 'What is your')
        instruction2 = graphics.Text(graphics.Point(400, 250), 'favorite color?')
        instruction.setFace('courier')
        instruction2.setFace('courier')
        instruction.setSize(36)
        instruction2.setSize(36)
        instruction.setTextColor('OrangeRed2')
        instruction2.setTextColor('OrangeRed2')
        instruction.draw(self.win)
        instruction2.draw(self.win)
        
        point = self.win.getMouse()
        
        while self.black.is_clicked(point) == False and \
        self.white.is_clicked(point) == False:
            point = self.win.getMouse()
        if self.black.is_clicked(point) == True:
            self.player_color = 1
            self.CPU_color = -1
        else:
            self.player_color = -1
            self.CPU_color = 1
        
        self.black.undraw()
        self.white.undraw()
        instruction.undraw()
        
    def setup(self):
        '''draws checkerboards on board
        draws starting four pieces
        '''
        #checkerboard drawing
        for c in range(1, 9):
            for r in range(1, 9):
                if c == 1:
                    x1 = 0
                elif c != 1:
                    x1 = 100 * c - 101
                if r == 1:
                    y2 = 0
                elif r != 1:
                    y2 = 100 * r - 101
                x2 = 100 * c - 1
                y1 = 100 * r - 1 
               
                square = graphics.Rectangle(graphics.Point(x1, y1), graphics.Point(x2, y2))
                square.setFill('SpringGreen4')
                square.draw(self.win)
        
        #starting setup of othello
        circle1 = graphics.Circle(graphics.Point(349, 349), 45)
        circle1.setFill('black')
        circle2 = graphics.Circle(graphics.Point(449, 349), 45)
        circle2.setFill('snow')
        circle3 = graphics.Circle(graphics.Point(349, 449), 45)
        circle3.setFill('snow')
        circle4 = graphics.Circle(graphics.Point(449, 449), 45)
        circle4.setFill('black')
        
        circle1.draw(self.win)
        circle2.draw(self.win)
        circle3.draw(self.win)
        circle4.draw(self.win)
    
    def getCoords(self, point):
        ''' for a point on the board, finds which square the point is in 
        
        returns tuple containing column and row the square
        is located in
        '''
        if point.getX() < 100:
            column = 1
        else:
            x = str(point.getX())
            column = int(x[0]) + 1
        if point.getY() < 100:
            row = 1
        else:
            y = str(point.getY())
            row = int(y[0]) + 1
        return column, row
        
    def surroundings(self, c, r, color):
        '''tests squares surrounding inputted square to see
        if any of them have a tile of the opposite color
        
        if they do, appends the locations of those tiles to a list and
        returns list. if they don't, returns False
        '''
        surrounding = []
        if c > 1 and r > 1 and c < 8 and r < 8:
            surrounding = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                           (c - 1, r),                  (c + 1, r),
                           (c - 1, r + 1), (c, r + 1), (c + 1, r + 1)]
        elif c == 1 and r > 1 and r < 8:
            surrounding = [(c, r - 1), (c + 1, r - 1),
                                            (c + 1, r),
                           (c, r + 1), (c + 1, r + 1)]
        elif c == 8 and r > 1 and r < 8:
             surrounding = [(c - 1, r - 1), (c, r - 1),
                           (c - 1, r),
                           (c - 1, r + 1), (c, r + 1)]
        elif r == 1 and c > 1 and c < 8:
            surrounding = [(c - 1, r),                  (c + 1, r),
                           (c - 1, r + 1), (c, r + 1), (c + 1, r + 1)]
        elif r == 8 and c > 1 and c < 8:
            surrounding = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                           (c - 1, r),                  (c + 1, r)]
        elif c == 1 and r == 1:
            surrounding = [             (c + 1, r),
                           (c, r + 1), (c + 1, r + 1)]
        elif c == 1 and r == 8:
            surrounding = [ (c, r - 1), (c + 1, r - 1),
                                             (c + 1, r)]
        elif c == 8 and r == 1:
            surrounding = [(c - 1, r),                  
                           (c - 1, r + 1), (c, r + 1)]
        elif c == 8 and r == 8:
            surrounding = [(c - 1, r - 1), (c, r - 1), 
                           (c - 1, r)               ]
        ocolor = -1 * color
        options = []
        for item in surrounding:
            if self.key[item] == ocolor:
                options.append(item)
        if len(options) != 0:
            return options
        else:        
            return False

    def pathways(self, c, r, dc, dr, color):
        '''follows a row, column, or diagonal to see if it ends in 
        a same-color tile. if it does, returns a list of all tiles that
        would be flipped in that pathway
        
        dc and dr are the difference between the initial column and row value
        of the starting square and that of the square in its surroundings with an 
        opposite color tile
        '''
        turn = []
        while c > 0 and c < 9 and r > 0 and r < 9:
            c = c + dc
            r = r + dr
            if (c, r) not in self.key:
                return False
            elif self.key[(c, r)] == -1 * color:
                turn.append((c, r))
            elif self.key[(c, r)] == color:
                return turn
            else:
                return False
            
    
    def legal_move(self, c, r, color):
        '''tests to see if move is legal by making sure it is
        in the dictionary, has opposite tiles in its surroundings, 
        and has at least one successful pathway
        '''
        if self.key[(c, r)] != 0:
            return False
        elif self.surroundings(c, r, color) != False:
            for item in self.surroundings(c, r, color):
                dc = item[0] - c
                dr = item[1] - r
                if self.pathways(c, r, dc, dr, color) != False:
                    return True
        return False
    
    def legal_white(self):
        '''tests to see if there is a legal move on the board for the 
        player
        '''
        for item in self.key:
            if self.legal_move(item[0], item[1], self.player_color) != False:
                return True
        return False

    def filled(self):
        '''tests to see if the board has any legal
        moves left on it
        '''
        
        for item in self.key:
            if self.legal_move(item[0], item[1], self.CPU_color) != False or \
            self.legal_move(item[0], item[1], self.player_color) != False:
                return False
        return True
    
    def draw_tile(self, c, r, color):
        '''for inputted column, row, draws circle of inputted color
        '''

        if r == 1:
            y2 = 0
        elif r != 1:
            y2 = 100 * r - 101
        x2 = 100 * c - 1
        xr = x2 - 50
        yr = y2 + 50
        flip = graphics.Circle(graphics.Point(xr, yr), 45)
        if color == 1:
            flip.setFill('black')
        else:
            flip.setFill('snow')
        flip.draw(self.win)
    
    
    def player_move(self):
        '''
        checks to see if legal move exists for player. if so,
        user clicks a point on the board. if point is in a 
        square that it is legal to move in, self.key is editted
        so that all the squares that have tiles that are turned 
        change values, and circles are drawn over the old tiles
        with the player's color
        '''
        if self.legal_white() != False:
            point = self.win.getMouse()
            c, r = self.getCoords(point)
            while self.legal_move(c, r, self.player_color) == False:
                point = self.win.getMouse()
                c, r = self.getCoords(point)
            #updates dictionary to include new move
            self.key[(c, r)] = self.player_color
            self.draw_tile(c, r, self.player_color)
            for item in self.surroundings(c, r, self.player_color):
                dc = item[0] - c
                dr = item[1] - r
                if self.pathways(c, r, dc, dr, self.player_color) != False:
                    for square in self.pathways(c, r, dc, dr, self.player_color):
                        self.key[square] = -1 * self.key[square]
                        self.draw_tile(square[0], square[1], self.player_color)
    
    def CPU_move(self, c, r):
        '''function assumes CPU intelligently inputs some
        square that it wants to move to and that the square is a legal
        move
        '''
        self.draw_tile(c, r, self.CPU_color)
        self.key[(c, r)] = self.CPU_color
        if self.surroundings(c, r, self.CPU_color) != False:
            for item in self.surroundings(c, r, self.CPU_color):
                dc = item[0] - c
                dr = item[1] - r
                if self.pathways(c, r, dc, dr, self.CPU_color) != False:
                    for square in self.pathways(c, r, dc, dr, self.CPU_color):
                        self.key[square] = -1 * self.key[square]
                        self.draw_tile(square[0], square[1], self.CPU_color)
    
    def end_score(self):
        '''finds the number of black tiles on the board at the end
        '''
        black = 0
        for item in self.key:
            if self.key[item] == 1:
                black = black + 1
        return black
    
    def winner(self):
        '''determines the winner based on the score
        '''
        if self.end_score() > 32:
            return 1
        elif self.end_score() == 32:
            return 0
        else:
            return -1
    
    def endscreen(self):
        '''endscreen that shows a Monty Python and the Holy Grail themed
        end message and the end score
        '''
        background = graphics.Rectangle(graphics.Point(0,0), graphics.Point(799, 799))
        background.setFill('CadetBlue2')
        background.draw(self.win)
        #score text
        black = 'BLACK: ' + str(self.end_score())
        white = 'WHITE: ' + str(64 - self.end_score())
        black_text = graphics.Text(graphics.Point(400, 400), black)
        black_text.setFace('courier')
        black_text.setSize(36)
        black_text.setStyle('bold')
        black_text.setTextColor('OrangeRed2')
        white_text = graphics.Text(graphics.Point(400, 450), white)
        white_text.setFace('courier')
        white_text.setSize(36)
        white_text.setStyle('bold')
        white_text.setTextColor('OrangeRed2')
        #win/lose/tie message
        lose1 = graphics.Text(graphics.Point(400, 280), "Now go away or I will")
        lose2 = graphics.Text(graphics.Point(400, 320), " taunt you a second time.")
        lose1.setFace('courier')
        lose1.setSize(36)
        lose1.setStyle('bold')
        lose1.setTextColor('OrangeRed2')
        lose2.setFace('courier')
        lose2.setSize(36)
        lose2.setStyle('bold')
        lose2.setTextColor('OrangeRed2')
        win = graphics.Text(graphics.Point(400, 250), "All right, we'll")
        win2 = graphics.Text(graphics.Point(400, 300), "call it a draw.")
        win.setFace('courier')
        win2.setFace('courier')
        win.setSize(36)
        win2.setSize(36)
        win.setStyle('bold')
        win2.setStyle('bold')
        win.setTextColor('OrangeRed2')
        win2.setTextColor('OrangeRed2')
        tie1 = graphics.Text(graphics.Point(400, 280), "You fight with the strength")
        tie2 = graphics.Text(graphics.Point(400, 320), "of many men, Sir Knight.")
        tie1.setFace('courier')
        tie1.setSize(36)
        tie1.setStyle('bold')
        tie1.setTextColor('OrangeRed2')
        tie2.setFace('courier')
        tie2.setSize(36)
        tie2.setStyle('bold')
        tie2.setTextColor('OrangeRed2')
        
        if self.winner() == self.player_color:
            win.draw(self.win)
            win2.draw(self.win)
        elif self.winner() == self.CPU_color:
            lose1.draw(self.win)
            lose2.draw(self.win)
        else:
            tie1.draw(self.win)
            tie2.draw(self.win)
        
        black_text.draw(self.win)
        white_text.draw(self.win)
        
        point = self.win.getMouse()
            