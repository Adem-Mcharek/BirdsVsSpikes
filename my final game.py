from tkinter import *
import time
import random



# ----Global Variables----
gamewidth = 500
gameheight = 700
waittime = 0.05
BS = []



def wait(t):  # function to make movement slower
    fin = time.time() + t
    while time.time() < fin:
        continue


class Bird:
    def __init__(self):
        self.x = 250
        self.y = 350
        self.img = PhotoImage(file="bird1.png")
        self.img1 = PhotoImage(file="bird3.png")
        self.life = True
        self.move = True
        self.initY = 480
        self.jumping = False
        self.maxJump = self.initY - 100
        self.startGame = False
        self.restart = False
        self.cookie_score = 0


    def moveLeft(self, event=None):
        self.x -= 20

    def moveRight(self, event=None):
        self.x += 20

    def gravity(self, event=None):
        self.y += 10

    def jump(self, event=None):
        self.startGame = True
        if self.y == self.initY:
            self.jumping = True

    def restart(self, event=None):
        self.restart = True

    def update(self):
        if self.jumping:
            self.y -= 17
            if self.y < self.maxJump:
                self.jumping = False
        else:
            self.initY = self.y
            self.maxJump = self.initY - 100

    def eat(self, Cookie):
        eatbird1 = (self.x - 20, self.y - 20)
        eatbird2 = (self.x + 20, self.y + 20)
        eatcookie1 = (Cookie.x - 10, Cookie.y - 10)
        eatcookie2 = (Cookie.x + 10, Cookie.y + 10 )
        if eatbird2[0] < eatcookie1[0]:
            return False
        elif eatcookie2[0] < eatbird1[0]:
            return False
        else:
            if eatbird2[1] < eatcookie1[1]:
                return False
            elif eatcookie2[1] < eatbird1[1]:
                return False
            else:
                self.cookie_score +=1
                return True


    def hitr(self, right_spike):
        hitbird1 = (self.x - 20, self.y - 20)
        hitbird2 = (self.x + 20, self.y + 20)
        hitspike1 = (right_spike.x - 10, right_spike.y - 20)
        hitspike2 = (right_spike.x + 10, right_spike.y + 20)
        if hitbird2[0] < hitspike1[0]:
            return False
        elif hitspike2[0] < hitbird1[0]:
            return False
        else:
            if hitbird2[1] < hitspike1[1]:
                return False
            elif hitspike2[1] < hitbird1[1]:
                return False
            else:
                print("die", hitbird1, hitbird2, hitspike1, hitspike2)
                self.life = False
                return True


    def hitl(self, left_spike):
        hitbird1 = (self.x - 20, self.y - 20)
        hitbird2 = (self.x + 20, self.y + 20)
        hitspike1 = (left_spike.x - 10, left_spike.y - 20)
        hitspike2 = (left_spike.x + 10, left_spike.y + 20 )
        if hitbird2[0] < hitspike1[0]:
            return False
        elif hitspike2[0] < hitbird1[0]:
            return False
        else:
            if hitbird2[1] < hitspike1[1]:
                return False
            elif hitspike2[1] < hitbird1[1]:
                return False
            else:
                print("die", hitbird1, hitbird2, hitspike1, hitspike2)
                self.life = False
                return True



class left_spike:
    def __init__(self):
        self.x = 62
        self.y = 700
        self.img = PhotoImage(file="spikel.png")

    def move(self):
        self.y -= 7

class Cookie:
    def __init__(self):
        self.x = random.randint(75, 425)

        self.y =  random.randint(200, 600)
        self.img = PhotoImage(file="cookie.png")
        self.eated = False

    def move(self):
        self.y -= 7

class right_spike:
    def __init__(self):
        self.x = 438
        self.y = 700
        self.img = PhotoImage(file="spiker.png")

    def move(self):
        self.y -= 7


main = Tk()


c = Canvas(main, width=gamewidth, height=gameheight, background='#33FFF9')

backgroundimg = PhotoImage(file="topspike.png")
backgroundimg1 = PhotoImage(file="botspike.png")
finaltext = "            Press space\n\n\n\n\n\n\n            WARNING!!! \n this game is highly addictive"


while True:
    c.delete("all")
    c.create_rectangle(0, 0, 50, 700, fill='#7a6b66', width="0")
    c.create_rectangle(450, 0, 500, 700, fill='#7a6b66', width="0")
    c.create_image(50, 0, image=backgroundimg, anchor=NW)
    c.create_image(50, 625, image=backgroundimg1, anchor=NW)
    starttext = c.create_text(250, 350, text=finaltext, fill="red", font=('arial', 20, 'bold'))

    bird = Bird()
    birdingame = c.create_image(bird.x, bird.y, image=bird.img)

    # binding keys to movements
    main.bind("<space>", bird.jump)
    main.bind("<Enter>", bird.restart)

    score = 0
    cookie_score = 0
    scoreTxt = c.create_text(250, 20, text="Score :" + str(score), fill="white", font=('arial', 20, 'bold'))
    scorecandieTxt = c.create_text(30, 30, text=str(bird.cookie_score), fill="yellow", font=('arial', 40, 'bold'))
    c.create_text(250, 600, text="**Adem Mcharek**" , fill="#36FF33", font=('arial', 20, 'bold'))


    right_spikeList = []
    right_spikeInCanvasList = []

    left_spikeList = []
    left_spikeInCanvasList = []

    cookie = Cookie()
    coockieingame = c.create_image(cookie.x, cookie.y, image=cookie.img)



    c.pack()


    while bird.life:

        c.itemconfig(scorecandieTxt, text=str(bird.cookie_score))
        c.itemconfig(scoreTxt, text="Score :" + str(score))

        if bird.eat(cookie):
            c.delete(coockieingame)
            cookie = Cookie()
            cookie_score += 1
            coockieingame = c.create_image(cookie.x, cookie.y, image=cookie.img)

        if bird.startGame:
            c.delete(starttext)
            score += 1
            bird.gravity()

            if bird.move == True:
                c.delete(birdingame)
                birdingame = c.create_image(bird.x, bird.y, image=bird.img)
                bird.moveRight()
            else:
                c.delete(birdingame)
                birdingame = c.create_image(bird.x, bird.y, image=bird.img1)
                bird.moveLeft()

            # making sure player does not cross the edge
            if bird.x <= 75:
                bird.x = 75
                bird.move = True
            if bird.x > 425:
                bird.x = 425
                bird.move = False
            bird.update()

            if bird.y <=75:
                break

            if bird.y >=625:
                break

            if len(left_spikeList) == 0:
                leftspike = left_spike()
                left_spikeList.append(leftspike)
                left_spikeInCanvasList.append(c.create_image(leftspike.x, leftspike.y, image=leftspike.img))
            if random.random() < 0.5:
                leftspike = left_spike()
                test = True
                for lspike in left_spikeList:
                    if abs(leftspike.y - lspike.y) < 250:
                        test = False
                if test:
                    left_spikeList.append(leftspike)
                    left_spikeInCanvasList.append(c.create_image(leftspike.x, leftspike.y, image=leftspike.img))


            if len(right_spikeList) == 0:
                rightspike = right_spike()
                right_spikeList.append(rightspike)
                right_spikeInCanvasList.append(c.create_image(rightspike.x, rightspike.y, image=rightspike.img))
            if random.random() < 0.5:
                rightspike = right_spike()
                test = True
                for rspike in right_spikeList:
                    if abs(rightspike.y - rspike.y) < 250:
                        test = False
                if test:
                    right_spikeList.append(rightspike)
                    right_spikeInCanvasList.append(c.create_image(rightspike.x, rightspike.y, image=rightspike.img))

            tmpListr = []
            tmpspikeListr = []
            for i in range(len(right_spikeList)):
                right_spikeList[i].move()
                c.coords(right_spikeInCanvasList[i], right_spikeList[i].x, right_spikeList[i].y)
                if right_spikeList[i].y > -50:
                    tmpListr.append(right_spikeList[i])
                    tmpspikeListr.append(right_spikeInCanvasList[i])
                    bird.hitr(right_spikeList[i])

            right_spikeList = tmpListr
            right_spikeInCanvasList  = tmpspikeListr



            tmpListl = []
            tmpspikeListl = []
            for i in range(len(left_spikeList)):
                left_spikeList[i].move()
                c.coords(left_spikeInCanvasList[i], left_spikeList[i].x, left_spikeList[i].y)
                if left_spikeList[i].y > -50:
                    tmpListl.append(left_spikeList[i])
                    tmpspikeListl.append(left_spikeInCanvasList[i])
                    bird.hitl(left_spikeList[i])

            left_spikeList = tmpListr
            left_spikeInCanvasList  = tmpspikeListr


            bird.update()




            c.coords(birdingame, bird.x, bird.y)
        c.update()
        wait(waittime)
    BS.append(score)
    bs = max(BS)
    finaltext = "            Game Over\n\n\n\n\n\n\n       your score "  + str(score) + "\nyou collected " +  str(cookie_score ) + "  candy \n       best score " +  str(bs)