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
    p.init()                                                    # Initialize Pygame
    screen = p.display.set_mode((WIDTH, HEIGHT))                
    clock = p.time.Clock()                                      #  for controlling frame rates
    screen.fill(p.Color("white"))                               
    gs = chessEngine.GameState()                                # Create an instance of the GameState class from chessEngine
    loadImages()                                              
    running = True  
    sqSleected=(     )                                          #tuple to keep track of last click of user
    playerClicks   =[]                                          #keep tracks of player clicks(two tuples:[(6,4),(4,4)])     
    while running:
        for e in p.event.get():  
            if e.type == p.QUIT:                                 # If the QUIT event (window close) is detected
                running = False  
            
            #Mouse Handlers
            elif e.type== p.MOUSEBUTTONDOWN:                     #logic to move pieces
                loaction=p.mouse.get_pos()
                col=loaction[0]//SQ_SIZE
                row=loaction[1]//SQ_SIZE
            

                print("Selected Square:", (row, col))
                if sqSleected==(row,col):                            #if user clicked the same square twice
                    sqSleected=()                                   #deselected
                    playerClicks=[]                                  #clear player clicks
                else:
                    sqSleected=(row,col)
                    playerClicks.append(sqSleected)      

                print("Player Clicks:", playerClicks)              #append for both 1st and 2nd clicks
                    
                    
                if len(playerClicks)==2: #check for 2nd click
                    move= chessEngine.Move(playerClicks[0],playerClicks[1],gs.board)     
                    print("Chess Notation",move.getChessNotation())
                    gs.makeMove(move)
                    sqSleected=()
                    playerClicks=[]

                #key Handelers
            elif e.type==p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()

                    

        drawGameState(screen, gs)  
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