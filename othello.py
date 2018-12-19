#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:24:39 2018

@author: namratakasaraneni

run this file to actually play game
"""

import othelloint as o
import intelligentplayer as CPU
import time

class Othello():
    
    def __init__(self):
        self.game = o.OthelloGraphicInterface()
        self.game.title()
        self.game.difficulty()
        self.game.color_choice()
        self.game.setup()
        self.computer = CPU.IntelligentPlayer(self.game)
        
    def play(self):
        if self.game.player_color == 1:
            while self.game.filled() == False:
                self.game.player_move()
                time.sleep(1)
                self.computer.move()
        else:
            while self.game.filled() == False:
                time.sleep(1)
                self.computer.move()
                self.game.player_move()
    def end(self):
        time.sleep(1)
        self.game.endscreen()

def main():
    game = Othello()
    game.play()
    game.end()


if __name__ == '__main__':
    main()