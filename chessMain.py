import pygame as p
import chessEngine

WIDTH=HEIGHT=512 
DEMENSION=8 #8X8
SQ_SIZE=HEIGHT//DEMENSION
MAX_FPS=15
IMAGES={}


def loadImages():
    pieces=['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece]=p.image.load("images/"+piece+ ".png")
    print(IMAGES)



def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)  # Draw the game state
        p.display.flip()
        clock.tick(MAX_FPS)




def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)


def drawBoard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    for r in range(DEMENSION):
        for c in range(DEMENSION):
            color=colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DEMENSION):
        for c in range(DEMENSION):
            piece = board[r][c]
            if piece != "--":  # Check if the square is not empty
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


    

if __name__=="__main__":    
    main()