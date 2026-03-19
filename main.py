import pygame
import sys
from menu import Menu
from jogo import Jogo

def main():
    # Inicialização conforme fontes [1]
    pygame.init()
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Box2D com Pygame")
    
    relogio = pygame.time.Clock()
    
    # Instancia o menu
    menu = Menu(tela)
    # O objeto jogo começa vazio e é criado ao clicar em "Novo Jogo"
    partida_atual = None
    
    estado_jogo = "MENU"

    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if estado_jogo == "MENU":
            escolha = menu.atualizar(eventos)
            
            if escolha == "Novo Jogo":
                partida_atual = Jogo(largura, altura)
                estado_jogo = "JOGANDO"
            elif escolha == "Continuar" and partida_atual is not None:
                estado_jogo = "JOGANDO"
            elif escolha == "Sobre":
                print("Sobre selecionado")
                
            menu.desenhar()

        elif estado_jogo == "JOGANDO":
            partida_atual.atualizar()
            partida_atual.desenhar(tela)
            
            # Se perder, volta para o menu
            if partida_atual.game_over:
                estado_jogo = "MENU"

        pygame.display.flip()
        relogio.tick(60)

if __name__ == "__main__":
    main()