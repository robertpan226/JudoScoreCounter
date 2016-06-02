#Coded By: Robert Pan, Steven Lou
#Python v2.7.5.1
#Import pygame modules and Buttons.py(it must be in same dir)
import pygame, time, Buttons
from pygame.locals import *

#Initialize pygame
pygame.init()

#class Judo with instantiation and judo attributes
class Judo:
    #various fonts for different labels
    myfont = pygame.font.SysFont("arial", 60)
    update_font = pygame.font.SysFont("arial", 32)
    bigfont = pygame.font.SysFont("arial", 100)
    scorefont = pygame.font.SysFont("arial", 48)

    #clock in order to use timer
    clock = pygame.time.Clock()

    #the two colour of the players
    colour=["Red","Blue"]

    #variables to be initialized
    player_score=[0,0]
    player_penalty=[0,0]
    player_w=[0,0]
    player_y=[0,0]
    player_k=[0,0]
    size=(50,50)
    events=None
    timer_stop=True
    sudden_death=False
    winner=False
    end_trigger=False
    temp=0
    winnernumber=0
    derp=False
    red_animation=None
    blue_animation=None
    ending_time=[0,0]

    event_ending=[0,0]

    #timer initializations
    minutes = 5
    seconds = 0
    milliseconds = 0
    first_reset=False

    #--MUST USE DIRECT PATH TO IMAGES OR ELSE A LOADING ERROR WILL BE DETECTED--
    #images for the various judo scores
    images=["C:\Users\Robert\Dropbox\ComputerScience\Pygame\Summative\image\\koka.png",
            "C:\Users\Robert\Dropbox\ComputerScience\Pygame\Summative\image\\yuko.png",
            "C:\Users\Robert\Dropbox\ComputerScience\Pygame\Summative\image\\wazaari.png"]

    #instantiation
    def __init__(self):
        self.main()

    #module to reset variables to default and to be used with the "Reset" button
    def reset_default(self):
        self.player_score=[0,0]
        self.player_penalty=[0,0]
        self.player_w=[0,0]
        self.player_y=[0,0]
        self.player_k=[0,0]
        self.size=(50,50)
        self.events=None
        self.timer_stop=True
        self.sudden_death=False
        self.winner=False
        self.end_trigger=False
        self.temp=0
        self.winnernumber=0
        self.derp=False
        self.red_animation=None
        self.blue_animation=None
        self.reset_timer()

    #special variable reset for sudden death
    def sudden_death_reset(self):
        self.player_score=[0,0]
        self.player_penalty=[0,0]
        self.player_w=[0,0]
        self.player_y=[0,0]
        self.player_k=[0,0]
        self.size=(50,50)
        self.events=None
        self.timer_stop=True
        self.winner=False
        self.temp=0
        self.winnernumber=0
        self.derp=False
        self.red_animation=None
        self.blue_animation=None
        self.reset_timer()

    #attribute to reset timer with the reset_default module
    def reset_timer(self):
        self.minutes = 5
        self.seconds = 0
        self.milliseconds = 0
        self.first_reset=False

    #module to allow the referee to pause/start the timer
    def pause_timer(self):
        if (self.timer_stop==True):
            self.timer_stop=False
        else:
            self.timer_stop=True

    #To send details of the winner to other modules
    def determine_winner(self,player):
        self.winner=True
        self.winnernumber=player

    #add points to each player based on the type
    def add_score(self,player,type):
        if (type==3):
            self.player_w[player]+=1
            self.player_score[player]+=100
        if (type==2):
            self.player_y[player]+=1
            self.player_score[player]+=10
        if (type==1):
            self.player_k[player]+=1
            self.player_score[player]+=1

    #player deduction for penalties
    def player_deduction(self,player):
        self.player_penalty[player]+=1
        if (player==0):
            self.add_score(1,self.player_penalty[0])
        else:
            self.add_score(0,self.player_penalty[1])

    #to determine the time of when the events and images are disappearing
    def determine_time(self, player, events):
        if events==0:
            if self.seconds<3:
                if (self.seconds!=0):
                    self.mod=3%self.seconds
                    self.ending_time[player]=60-self.mod
            else:
                self.ending_time[player]=self.seconds-3

        else:
             if self.seconds<3:
                if (self.seconds!=0):
                    self.mod=4%self.seconds
                    self.event_ending[player]=60-self.mod
             else:
                self.event_ending[player]=self.seconds-3

    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((1000,738),0,32)
        pygame.display.set_caption("Judo Score Counter")

    #Update the display and show the buttons
    def update_display(self):
        if (self.winner==False):
            #red squares
            red_colour = pygame.Surface(self.size).convert()
            red_colour.fill((255, 0, 0))
            #blue squares
            blue_colour = pygame.Surface(self.size).convert()
            blue_colour.fill((0, 0, 255))

            self.screen.fill((30,144,255))

            #updating the buttons
            #Parameters:                        surface,      color,            x,   y, length, height, width,   text,   text_color
            self.PlayerRed_W_Add.create_button(self.screen, (107,142,35),      66, 485, 30,    30,    0,        "+", (255,255,255))
            self.PlayerRed_Y_Add.create_button(self.screen, (107,142,35),     150, 485, 30,    30,    0,        "+", (255,255,255))
            self.PlayerRed_K_Add.create_button(self.screen, (107,142,35),     234, 485, 30,    30,    0,        "+", (255,255,255))
            self.PlayerRed_Penalty.create_button(self.screen, (107,142,35),   150, 600, 150 ,    90,    0,       "Penalty", (255,255,255))
            self.PlayerBlue_W_Add.create_button(self.screen, (107,142,35),    739, 485, 30,    30,    0,       "+", (255,255,255))
            self.PlayerBlue_Y_Add.create_button(self.screen, (107,142,35),    823, 485, 30,    30,    0,       "+", (255,255,255))
            self.PlayerBlue_K_Add.create_button(self.screen, (107,142,35),    907, 485, 30,    30,    0,       "+", (255,255,255))
            self.PlayerBlue_Penalty.create_button(self.screen, (107,142,35),  739, 600, 150,   90,    0,     "Penalty", (255,255,255))
            self.Pause_Start.create_button(self.screen,             (107,142,35),  405,  500, 200,   70,    0,     "Timer Pause/Go", (255,255,255))
            self.Reset.create_button(self.screen,             (107,142,35),  430, 610, 150,   70,    0,     "Reset", (255,255,255))


            #Player Headings
            player_red_label = self.myfont.render("Player", 1, (255,255,255))
            self.screen.blit(player_red_label, (94, 10))
            self.screen.blit(red_colour, (250, 20))

            player_blue_label = self.myfont.render("Player", 1, (255,255,255))
            self.screen.blit(player_blue_label, (700, 10))
            self.screen.blit(blue_colour, (856, 20))

            #mechanics
            red_title_label = self.update_font.render("W         Y         K         S", 1, (255,255,255))
            self.screen.blit(red_title_label, (69,377))
            blue_title_label = self.update_font.render("S         W         Y         K", 1, (255,255,255))
            self.screen.blit(blue_title_label, (660,377))

            #score label
            score_red_w=self.scorefont.render(str(self.player_w[0]), 1, (255,255,255))
            self.screen.blit(score_red_w, (67,417))
            score_red_y=self.scorefont.render(str(self.player_y[0]), 1, (255,255,255))
            self.screen.blit(score_red_y, (150,417))
            score_red_k=self.scorefont.render(str(self.player_k[0]), 1, (255,255,255))
            self.screen.blit(score_red_k, (231,417))
            score_red_s=self.scorefont.render(str(self.player_score[0]), 1, (255,255,255))
            self.screen.blit(score_red_s, (312,417))

            score_blue_s=self.scorefont.render(str(self.player_score[1]), 1, (255,255,255))
            self.screen.blit(score_blue_s, (653,417))
            score_blue_w=self.scorefont.render(str(self.player_w[1]), 1, (255,255,255))
            self.screen.blit(score_blue_w, (740,417))
            score_blue_y=self.scorefont.render(str(self.player_y[1]), 1, (255,255,255))
            self.screen.blit(score_blue_y, (821,417))
            score_blue_k=self.scorefont.render(str(self.player_k[1]), 1, (255,255,255))
            self.screen.blit(score_blue_k, (905,417))

            #penalty label
            red_penalty=self.scorefont.render("Penalty: "+str(self.player_penalty[0]), 1, (255,255,255))
            self.screen.blit(red_penalty, (69,530))
            blue_penalty=self.scorefont.render("Penalty: "+str(self.player_penalty[1]), 1, (255,255,255))
            self.screen.blit(blue_penalty, (750,530))

            #to show the images
            if (self.red_animation!=None):
                self.screen.blit(pygame.image.load(self.red_animation),(115,150))

            if (self.blue_animation!=None):
                self.screen.blit(pygame.image.load(self.blue_animation),(700,150))


            #events log
            if (self.events!=None):
                events_label = self.update_font.render(self.events, 1, (255,255,255))
                self.screen.blit(events_label, (340, 90))

            #in-game timer
            if (len(str(self.seconds))==2):
                timer_label = self.myfont.render("{}:{}".format(self.minutes, self.seconds), 1, (255,255,255))
                self.screen.blit(timer_label, (445, 10))

            if (len(str(self.seconds))==1):
                temp="0"+str(self.seconds)
                timer_label = self.myfont.render("{}:{}".format(str(self.minutes), temp), 1, (255,255,255))
                self.screen.blit(timer_label, (445, 10))

        #to enable the sudden death screen
        if (self.sudden_death==True):
            self.screen.fill((0,0,0))
            sudden_label = self.bigfont.render("Sudden Death", 1, (255,255,255))
            self.screen.blit(sudden_label, (200, 280))

        #to determine the winner screen
        if self.winner==True:
            self.screen.fill((0,0,0))
            self.Reset.create_button(self.screen,             (107,142,35),  430, 610, 150,   70,    0,     "Reset", (255,255,255))

            winner_label = self.bigfont.render("Player "+self.colour[self.winnernumber]+" Wins!", 1, (255,255,255))
            self.screen.blit(winner_label, (180, 280))

        #the final screen of when sudden death is a draw
        if self.end_trigger==True and self.derp==True:
            self.screen.fill((0,0,0))
            self.Reset.create_button(self.screen,             (107,142,35),  425, 610, 150,   70,    0,     "New Match", (255,255,255))

            winner_label = self.bigfont.render("Referee will decide winner.", 1, (255,255,255))
            self.screen.blit(winner_label, (0, 280))

        pygame.display.flip()

    #Run the loop
    def main(self):
        #Initialize the buttons
        self.PlayerRed_W_Add = Buttons.Button()
        self.PlayerRed_Y_Add = Buttons.Button()
        self.PlayerRed_K_Add = Buttons.Button()
        self.PlayerRed_Penalty = Buttons.Button()
        self.PlayerBlue_W_Add = Buttons.Button()
        self.PlayerBlue_Y_Add = Buttons.Button()
        self.PlayerBlue_K_Add = Buttons.Button()
        self.PlayerBlue_Penalty = Buttons.Button()
        self.Pause_Start = Buttons.Button()
        self.Reset = Buttons.Button()

        #initialize the disply
        self.display()

        #game loop
        while True:
            #the logic of the ingame timer
            if (self.timer_stop==False):
                if self.milliseconds>1000:
                    self.seconds-=1
                    self.milliseconds=0

                if self.seconds%60==0:
                    self.minutes-=1
                    if self.minutes!=0:
                        self.seconds=59

            #determining the winner and different scenarios
            if (self.player_penalty[0]==4):
                self.determine_winner(1)

            if (self.player_penalty[1]==4):
                self.determine_winner(0)

            if (self.timer_stop==False):
                self.milliseconds += self.clock.tick_busy_loop(60)

            if (self.player_w[0]==2):
                self.determine_winner(0)

            if (self.player_w[1]==2):
                self.determine_winner(1)

            if (self.end_trigger==True and (self.player_score[1]>self.player_score[0])):
                self.determine_winner(1)

            if (self.end_trigger==True and (self.player_score[0]>self.player_score[1])):
                self.determine_winner(0)

            if (self.minutes==-1 and self.seconds==59):
                if self.player_score[0]==0 and self.player_score[1]==0:
                    if (self.sudden_death==False and self.end_trigger==True):
                        self.derp=True
                    else:
                        self.sudden_death=True

                if self.player_score[0]==self.player_score[1]:
                    if (self.sudden_death==False and self.end_trigger==True):
                        self.derp=True
                    else:
                        self.sudden_death=True
                        self.reset_timer()

                if self.player_score[0]>self.player_score[1]:
                    self.determine_winner(0)

                if self.player_score[1]>self.player_score[0]:
                    self.determine_winner(1)


            if (self.seconds==self.ending_time[0]):
                self.red_animation=None

            if (self.seconds==self.ending_time[1]):
                self.blue_animation=None

            if (self.seconds==self.event_ending[0]):
                self.events=None

            #updating the display each cycle
            self.update_display()

            #checking for sudden death
            if (self.sudden_death==True):
                time.sleep(3)
                self.sudden_death_reset()
                self.end_trigger=True
                self.sudden_death=False

            #to obtain input from mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:

                    #ALL THE BUTTONS FOR THE JUDO SCORE COUNTER

                    #adding waza-ari points to red player
                    if self.PlayerRed_W_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(0,3)
                        self.events="Player Red"+" gained a Waza-ari!"

                        self.red_animation=self.images[2]
                        self.determine_time(0,0)
                        self.determine_time(0,1)

                    #adding yuko points to red player
                    if self.PlayerRed_Y_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(0,2)
                        self.events="Player Red"+" gained a Yuko!"

                        self.red_animation=self.images[1]
                        self.determine_time(0,0)
                        self.determine_time(0,1)

                    #adding koka points to red player
                    if self.PlayerRed_K_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(0,1)
                        self.events="Player Red"+" gained a Koka!"

                        self.red_animation=self.images[0]
                        self.determine_time(0,0)
                        self.determine_time(0,1)

                    #penality for red player
                    if self.PlayerRed_Penalty.pressed(pygame.mouse.get_pos()):
                        self.player_deduction(0)
                        self.events= "Penalty for Player Red!"
                        self.determine_time(0,1)

                    #adding waza-ari points to blue player
                    if self.PlayerBlue_W_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(1,3)
                        self.events="Player Blue"+" gained a Waza-ari!"

                        self.blue_animation=self.images[2]
                        self.determine_time(1,0)
                        self.determine_time(0,1)

                    #adding yuko points to blue player
                    if self.PlayerBlue_Y_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(1,2)
                        self.events="Player Blue"+" gained a Yuko!"

                        self.blue_animation=self.images[1]
                        self.determine_time(1,0)
                        self.determine_time(0,1)

                    #adding koka points to blue player
                    if self.PlayerBlue_K_Add.pressed(pygame.mouse.get_pos()):
                        self.add_score(1,1)
                        self.events="Player Blue"+" gained a Koka!"

                        self.blue_animation=self.images[0]
                        self.determine_time(1,0)
                        self.determine_time(0,1)

                    #penality for blue player
                    if self.PlayerBlue_Penalty.pressed(pygame.mouse.get_pos()):
                        self.player_deduction(1)
                        self.events= "Penalty for Player Blue!"
                        self.determine_time(0,1)

                    #button for starting and stopping the in-game timer
                    if self.Pause_Start.pressed(pygame.mouse.get_pos()):
                        self.pause_timer()

                        if self.first_reset==False:
                            self.events= "           Time Start!"
                            self.first_reset=True

                        else:
                            self.events= "         Time Paused!"
                            self.first_reset=False


                        self.determine_time(0,1)

                    #to reset all the variables and text on screen
                    if self.Reset.pressed(pygame.mouse.get_pos()):
                        self.reset_default()
                        self.events= "                Reset!"
                        self.determine_time(0,1)

#calling the class Judo
obj = Judo()
