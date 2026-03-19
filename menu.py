import pygame

# Cores baseadas nas fontes fornecidas [1]
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 150, 255)
VERDE = (100, 255, 100)

class Menu:
    def __init__(self, tela):
        self.tela = tela
        # Inicialização das fontes conforme as fontes do sistema do código original [1]
        self.fonte_titulo = pygame.font.SysFont("Arial", 50)
        self.fonte_botao = pygame.font.SysFont("Arial", 30)
        
        # Opções do menu solicitadas
        self.opcoes = ["Novo Jogo", "Continuar", "Sobre"]
        self.indice_selecionado = 0
        self.selecionado = False

    def desenhar(self):
        """Renderiza o menu na tela."""
        self.tela.fill(PRETO)  # Fundo padrão [1]
        
        # Desenha o título
        texto_titulo = self.fonte_titulo.render("MENU PRINCIPAL", True, BRANCO)
        rect_titulo = texto_titulo.get_rect(center=(self.tela.get_width() // 2, 100))
        self.tela.blit(texto_titulo, rect_titulo)

        # Desenha as opções
        for i, opcao in enumerate(self.opcoes):
            # Se a opção estiver selecionada, muda a cor para verde [1]
            cor = VERDE if i == self.indice_selecionado else BRANCO
            
            texto_surf = self.fonte_botao.render(opcao, True, cor)
            # Centraliza as opções verticalmente com espaçamento
            rect_opcao = texto_surf.get_rect(center=(self.tela.get_width() // 2, 250 + i * 60))
            
            # Pequeno destaque visual para a opção selecionada
            if i == self.indice_selecionado:
                pygame.draw.rect(self.tela, AZUL, rect_opcao.inflate(20, 10), 2) # Borda azul ao redor [1]
                
            self.tela.blit(texto_surf, rect_opcao)

    def atualizar(self, eventos):
        """
        Trata as entradas de teclado para navegar no menu.
        Retorna a opção selecionada quando o usuário pressionar ENTER.
        """
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.indice_selecionado = (self.indice_selecionado - 1) % len(self.opcoes)
                elif evento.key == pygame.K_DOWN:
                    self.indice_selecionado = (self.indice_selecionado + 1) % len(self.opcoes)
                elif evento.key == pygame.K_RETURN:
                    return self.opcoes[self.indice_selecionado]
        return None