import pygame
from poker_main import Player, StandardDeck, StandardBoard
pygame.init()

deck = StandardDeck()
board = StandardBoard()
player_1 = Player("One")
player_2 = Player("Two")

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Texas Hold'em")
clock = pygame.time.Clock()
suit_dic = {"\u2660": "s", "\u2665": "h", "\u2666": "d", "\u2663": "c"}

running = True

# Game variables
players_in_game = [player_1, player_2]
bb_list = [20, 50, 100, 200, 400, 800]
bb = bb_list[0]

# Draw variables
gap = 10
gap_x = -228*3
hand_card_1 = pygame.transform.scale(pygame.image.load('deck_images/14s.jpg'), (128//3, 178//3))
hand_card_2 = pygame.transform.scale(pygame.image.load('deck_images/14h.jpg'), (128//3, 178//3))
windows_spawned = 0
while running:
	# ---------- Game logic block ----------
	# Shuffle deck
	if not deck.shuffled:
		deck.shuffle()

	# Deal cards to players
	if len(player_1.hand) < 2:
		for x in players_in_game:
			x.hand.append(deck.pop(0))
			x.hand.append(deck.pop(0))
		for x in players_in_game:
			for card in x.hand:
				card.showing = True
	# Bet blinds
	
	# ---------- GUI block ----------
	while windows_spawned <= 2:
		for player in players_in_game:
			windows_spawned += 1
			gap_x += player.surface.get_width()
			player.draw_card()

			window.blit(player.surface, (10+gap_x, gap))
			pygame.draw.rect(player.surface, (255, 255, 255), player.surface.get_rect(), 3)
			player.surface.blit(player.card_1, (gap, gap))
			player.surface.blit(player.card_2, (gap * 2 + 128 // 3, gap))

			f1 = pygame.font.Font(None, 23)
			line_1 = f1.render(str(player), 0, (255, 255, 255))
			line_2 = f1.render("Chips amount: {0}".format(player.chip_amount), 0, (255, 255, 255))
			line_3 = f1.render("Bet N chips to continue!", 0, (255, 255, 255))

			player.surface.blit(line_1, (gap, gap * 2 + 178 // 3))
			player.surface.blit(line_2, (gap, gap * 4 + 178 // 3))
			player.surface.blit(line_3, (gap, gap * 6 + 178 // 3))	
		
		pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	clock.tick(30)

pygame.quit()
