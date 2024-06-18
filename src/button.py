import pygame
from settings import WHITE, YELLOW, mouse_click_sound

class Button:
    def __init__(self, x, y, text, font):
        self.text = text
        self.font = font
        self.image = self.font.render(self.text, True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # Add hover effect
            hover_image = self.font.render(self.text, True, YELLOW)
            window.blit(hover_image, self.rect.topleft)
        else:
            window.blit(self.image, self.rect.topleft)

        # Draw underline
        underline_start = (self.rect.left, self.rect.bottom + 2)
        underline_end = (self.rect.right, self.rect.bottom + 2)
        pygame.draw.line(window, WHITE, underline_start, underline_end, 3)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            mouse_click_sound.play()  # Play click sound when clicked
            return True
        return False
