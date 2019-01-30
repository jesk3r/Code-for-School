import pygame
pygame.init()

class UserInterface:
    def __init__(self):
        self.id = None


    def Event_Handler(self):
        '''
        This method returns the value of the button pressed

        :return: The type of button pressed and the value of it
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.Quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 1,pygame.mouse.get_pos()
                pass

            if event.type == pygame.KEYDOWN:
                return [2,event.key]

            if event.type == pygame.KEYUP:
                return [3,event.key]


        return [0]
