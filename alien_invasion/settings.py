#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings():

	def __init__(self):
		self.screen_width = 1300
		self.screen_height = 800
		self.bg_color = (224,160,192)
		
		self.ship_speed_factor = 1
		self.ship_limit = 1

		self.bullet_speed_factor = 3
		self.bullet_width = 30
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 5

		self.alien_speed_factor = 1
		self.fleet_drop_speed = 6
		
		self.fleet_direction = 1

		self.speedup_scale = 1.05
		
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		
		self.ship_speed_factor = 1.1
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		self.fleet_direction = 1

		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		# print(self.alien_points)
