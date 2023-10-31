import pygame
from sys import exit

# inicializa o pygame
pygame.init()

# Cria
tamanho = (700,300)
tela = pygame.display.set_mode(tamanho)

# Define o titulo da tela
pygame.display.set_caption("Capivara Runner")

# Cria um relógio para controlar frames
relogio = pygame.time.Clock()

# Importa imagem de fundo cenario
chao_super = pygame.image.load('assets/fundos/ground.png')
ceu_super = pygame.image.load('assets/fundos/Sky.png')

# Importa a imagem da capivara 
capivara_sup = pygame.image.load('assets/capivara/andando/tile000.png')
capivara_rect = capivara_sup.get_rect(center = (30,150))

# Importa a imagem do gamba
gamba_super = pygame.image.load('assets/gamba/tile000.png')
gamba_rect = gamba_super.get_rect(center = (730,150))

# Propriedades da capivara
gravidade_capivara = 0

# LOOP PRINCIPAL
while True:
    # Verifica a ocorrencia de eventos
    for evento in pygame.event.get():
        # Verifica se o usuario quer sair
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Coloca uma cor de fundo na tela
    tela.fill("#7FFF00")

    # Coloca fundo na tela
    tela.blit(ceu_super, (0, 0))
    tela.blit(chao_super, (0, 160))

    # Coloca gamba na tela
    tela.blit(gamba_super, gamba_rect)
    gamba_rect.x -= 5

    # Coloca a capivara na tela
    tela.blit(capivara_sup, capivara_rect)

    # Aumenta a gravidade de 1 em 1
    gravidade_capivara += 1
    capivara_rect.centery += gravidade_capivara
    if capivara_rect.centery > 150: capivara_rect.centery = 150

    # Atualiza a tela
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)