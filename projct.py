import cv2
import cvzone
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
import random
import time
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands   

st.set_page_config(
    page_title="ROck",
    layout='wide'
)

def main_func():
    st.title("Rock🪨 Paper🧻 Scissor✂️ Game")
    # st.subheader('Try Your luck by playing this game\nCan you beat ME?🖥️')
    n = st.slider('Choose the Target of your game', 5, 25, 5)
    st.write('---')
    startGame = False
    if st.button('Play'):
        startGame = True
    # if st.button('Stop'):
    #     startGame = False
    frame_win, frame2_win = st.columns(2)
    Frame_win = frame_win.empty()
    Frame2_win= frame2_win.empty()
    
    Frame_win.header('YOU')
    # Frame2_win.header('YOU')
    st.write('---')
    Frame2_win.header('COMPUTER')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    detector = HandDetector(maxHands=1)
    # timer = 0
    # stateResult = False
    scores = [0, 0]
    while True and scores[0] != n or scores[1] !=n:

        ret, img = cap.read()
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Find hands
        hands, img = detector.findHands(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        Frame_win.image(img)
        # st.image('1.png')
        
        if startGame:
                    
            if hands and img is not None:
                # hand = hands[0]
                # fingers = detector.fingersUp(hand)
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    randomNumber = random.randint(1, 3)
                    # imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    # imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        Frame2_win.image(("{}.png".format(str(randomNumber))))
                
                        scores[1] += 1
                        time.sleep(2)

                    # Computer Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        # st.image("{}.png".format(str(randomNumber)))
                        Frame2_win.image(("{}.png".format(str(randomNumber))), caption='COMPUTER')
                        scores[0] += 1
                
                        time.sleep(2)
                    
                    if scores[0] > scores[1]:
                        lead = 'COMPUTER'
                    elif scores[1] > scores[0]:
                        lead = 'YOU'
                    elif scores[0] == scores[1]:
                        lead = 'DRAW'
                    
                    Frame2_win.header("""LEAD - {}
                                      Computer Score = {}            Your Score = {}""".format(lead, scores[0], 
                                                                                               scores[1]))

                    if scores[0] == n or scores[1] == n:
                        Frame_win.header("GAME OVER")
                        startGame = False
                        break
        # time.sleep(5)
        # st.write(scores)
                # st.write(fingers)
        
        # key = cv2.waitKey(1)
        # game = st.checkbox("Ready? Click here to start")
        # startGame == True
    
    # st.header(scores)
    if scores[0] == n and scores[0] > scores[1]:
        Frame2_win.header("COMPUTER WON BY {}-{}".format(scores[0], scores[1]))
        st.header("LOSER")
    else:
        Frame2_win.header("YOU WON BY {}-{}".format(scores[1], scores[0]))
        st.header("CONGRATULATIONS")
        
if __name__ == '__main__':
    main_func()
    