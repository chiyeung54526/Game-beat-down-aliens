#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
import game_functions as ff
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Beat Down Aliens")
	play_button = Button(ai_settings, screen, "Play")

	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	ship = Ship(ai_settings, screen)
	bullets = Group()

	bg_color = (ai_settings.bg_color)

	alien = Alien(ai_settings, screen)
	aliens = Group()

	ff.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		ff.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			ff.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			ff.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
				
		ff.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)		
		# print(len(bullets))
		
pygame.mixer.init()
pygame.mixer.music.load('sounds/8bits.wav')
pygame.mixer.music.play(-1,0)


run_game()

