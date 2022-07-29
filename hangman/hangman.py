import random

class User:
    def __init__(self):
        self.name = input("What is your name? \n--> ")
        print('\nHi, {} ! Time to play hangman game!'.format(self.name), '\n\n\n')
class HangMan:
    input_list = ["secret", "answer", "merong"]

    def __init__(self, user):
        self.user = user.name
        self.count = 10
        self.r = []

    def countRound(self, a): #사용자가 어떤 문제를 풀었는지 저장하기 위함
        str = ''.join(a)
        if str not in self.r and str in HangMan.input_list:
            print(self.r)
            print(HangMan.input_list)
            self.r.append(str)

    def getAnswer(self): #문제 가져오기
        while True:
            a = list(random.choice(HangMan.input_list))
            if ''.join(a) in self.r:
                continue
            break
        self.countRound(a)        
        return a

    def startGame(self):
        #제시된 모든 문제를 풀었을 경우 종료
        for i in range(len(HangMan.input_list)):
            if HangMan.input_list[i] not in self.r:
                break
        else:
            print("You are done all rounds ! ")
            return 0, 0
        a = self.getAnswer()
        q = []
        print("Let's start next round !")
        for i in a:
            q.append('_')
        print(' '.join(q), "\n")
        return a, q

    def doGame(self, a, q):
        if self.count < 0:
            return 0
        while self.count >= 0:
            c = input("Guess a character.  ")
            for i in range(len(a)): #중복된 문자를 찾기 위함
                if a[i] == c:
                    q[i] = c

            #정답을 맞췄을 경우    
            if a == q:
                print(' '.join(q), "\n")
                print("Congratulaions ! The guesss are correct.")
                break
    
            #문자를 찾지 못한 경우
            if c not in a:
                print("Oops! Wrong")
                self.count -= 1
                if self.count == 0:
                    return 0
                print("you have {} more guesses!".format(self.count))
            print(' '.join(q), "\n")
                

    def execute(self): #게임 실행
        while True:
            a, q = self.startGame() #게임 시작
            if a == 0 and q == 0: #제시된 정답 모두 맞췄을 경우 게임 종료
                print("\nGame Clear!")
                break
            if self.doGame(a, q) == 0: #카운트가 0이 되었을 경우 게임 종료
                print("\nGame Over. . .")
                break

    def gameOver(self):
        print("User :", self.user, " |  Score :", self.count)

"""
1. rand 함수가 중복될 경우
- not in r ?
- r, answer = [“answer”, “merong”]

	break len(answer == 0) : break
[완료]

2. return 의 예외처리에 대해서는?? 
만약 do grame 에 대해서 count 가 -1 일 경우????
[완료]

"""