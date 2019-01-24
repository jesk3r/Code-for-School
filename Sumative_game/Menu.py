def menu_screen():
    pg.mouse.set_visible(True)
    startA = pg.Rect((22, 246), (130, 40))
    quitA = pg.Rect((22, 300), (90, 40))

    frame = pg.image.load("/Users/dheeraj/Documents/git_projects/School_work/Coding_class/Sumative_game/Main Menu/Main Menu-23 (dragged).png").convert()

    while True:
        pos = pg.mouse.get_pos()
        mclicks = pg.mouse.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                QUIT()

        if startA.collidepoint(pos) and mclicks[0] == 1:
            gameloop()

        elif quitA.collidepoint(pos) and mclicks[0] == 1:
            sys.exit()

        DisplayScreen.blit(frame, ((0, 0)))

        clock.tick(24)
        pg.display.update()

def menu_animation():

    pg.mouse.set_visible(False)
    n = 1
    while n != 24:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                QUIT()

        frame = pg.image.load("/Users/dheeraj/Documents/git_projects/School_work/Coding_class/Sumative_game/Main Menu/Main Menu-{0} (dragged).png".format(n))

        DisplayScreen.blit(frame, ((0, 0)))

        clock.tick(24)
        pg.display.update()
        n += 1