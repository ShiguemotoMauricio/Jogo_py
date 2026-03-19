import pygame
import fase1  # Importação interna para desacoplar a Main
# Se houver mais fases, importe aqui: import fase2, fase3...

# Definições de cores e constantes conforme as fontes [3]
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 150, 255)

class Bloco:
    def __init__(self, x, y, largura, altura, resistencia, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.resistencia = resistencia
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, 1)

class Raquete:
    def __init__(self, largura_tela, altura_tela):
        self.largura = 120
        self.altura = 20
        self.x = (largura_tela // 2) - (self.largura // 2)
        self.y = altura_tela - 50
        self.velocidade = 8
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.largura_tela = largura_tela

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < self.largura_tela:
            self.rect.x += self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, AZUL, self.rect)

class Bola:
    def __init__(self, largura_tela, altura_tela):
        self.raio = 10
        self.rect = pygame.Rect(largura_tela // 2, altura_tela - 100, self.raio * 2, self.raio * 2)
        self.dx = 5
        self.dy = -5
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

    def mover(self, raquete_rect, blocos):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left <= 0 or self.rect.right >= self.largura_tela: self.dx *= -1
        if self.rect.top <= 0: self.dy *= -1
        if self.rect.colliderect(raquete_rect):
            self.dy *= -1
            self.rect.bottom = raquete_rect.top

        for bloco in blocos[:]:
            if self.rect.colliderect(bloco.rect):
                self.dy *= -1
                bloco.resistencia -= 1
                if bloco.resistencia <= 0:
                    blocos.remove(bloco)
                break

    def desenhar(self, tela):
        pygame.draw.circle(tela, BRANCO, self.rect.center, self.raio)

class Jogo:
    """Classe que encapsula a partida e gerencia as fases internamente """
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.raquete = Raquete(largura_tela, altura_tela)
        self.bola = Bola(largura_tela, altura_tela)
        self.game_over = False
        self.vitoria = False
        
        # Controle de fase interno
        self.nivel_atual = 1
        self.blocos = self.carregar_fase()

    def carregar_fase(self):
        """Decide qual fase carregar sem envolver a main.py"""
        if self.nivel_atual == 1:
            # Chama a função de geração de blocos do arquivo fase1.py
            return fase1.gerar_fase(Bloco) 
        # Exemplo para próximas fases:
        # elif self.nivel_atual == 2: return fase2.gerar_fase(Bloco)
        return []

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        self.raquete.mover(teclas)
        self.bola.mover(self.raquete.rect, self.blocos)
        
        if self.bola.rect.bottom > self.altura_tela:
            self.game_over = True
        
        if len(self.blocos) == 0:
            # Lógica para avançar de nível ou vencer
            self.vitoria = True

    def desenhar(self, tela):
        tela.fill(PRETO)
        self.raquete.desenhar(tela)
        self.bola.desenhar(tela)
        for bloco in self.blocos:
            bloco.desenhar(tela)