import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, size, text='', text_color=(0, 0, 0), font_size=24, isSpace=False):
        super().__init__()
        self.size = size
        self.default_color = (255, 180, 200)
        self.pressed_color = (255, 100, 100)
        self.color = self.default_color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font_path = "assets/Thasadith-Regular.ttf"
        self.border_color = (255, 255, 255)
        self.border_width = 2
        self.isSpace = isSpace

        # Create the surface for the key
        self.image = pygame.Surface((10 * self.size if self.isSpace else self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Draw the rounded rectangle
        self.draw_key()
        
    def draw_key(self):
        """Draw the key with a border and rounded edges."""
        # Draw the border
        pygame.draw.rect(
            self.image,
            self.border_color,
            (0, 0, 10 * self.size if self.isSpace else self.size, self.size),
            border_radius=self.size // 6,
            width=self.border_width
        )
        
        # Draw the inner rectangle (key body)
        pygame.draw.rect(
            self.image,
            self.color,
            (self.border_width, self.border_width, (10 * self.size if self.isSpace else self.size) - 2 * self.border_width, self.size - 2 * self.border_width),
            border_radius=(self.size // 6) - self.border_width
        )
        
        # Render the text on the key
        if self.text:
            font = pygame.font.Font(self.font_path, self.font_size)
            text_surface = font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=((10 * self.size if self.isSpace else self.size) // 2, self.size // 2))
            self.image.blit(text_surface, text_rect)

    def handle_event(self, event):
        """Handle events to change the key color when pressed."""
        if event.type == pygame.KEYDOWN and ((self.isSpace and event.key == pygame.K_SPACE) or (not self.isSpace and event.unicode == self.text.lower())):
            self.color = self.pressed_color
            self.draw_key()
        elif event.type == pygame.KEYUP and ((self.isSpace and event.key == pygame.K_SPACE) or (not self.isSpace and event.unicode == self.text.lower())):
            self.color = self.default_color
            self.draw_key()
    
    def update(self):
        """Optional: Add custom update logic if needed."""