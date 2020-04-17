import TGCHandler
import time
from sound import Sound
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

##CONNECTING THINKGEAR
handler = TGCHandler.TGCHandler(host = '127.0.0.1')
handler.connect()
handler.configure()
handler.startMeasuring()

##FIREBASE
cred = credentials.Certificate("pythontest.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://pythontest-f3b4b.firebaseio.com/'})

i=0
stat = 'none'
while True:
    plevel = handler.get('poorSignalLevel')
    raw = handler.get('rawEeg')
    att = handler.get('attention')
    med = handler.get('meditation')
    delt = handler.get('delta')
    the = handler.get('theta')
    la = handler.get('lowAlpha')
    ha = handler.get('highAlpha')
    lb = handler.get('lowBeta')
    hb = handler.get('highBeta')
    lg = handler.get('lowGamma')
    hg = handler.get('highGamma')
    bl = handler.get('blinkStrength')
    if att != None and plevel != None and bl != None:
        print("Serial No:" + str(i) + " Raw-EEG:" + str(raw) + " Att:" + str(att) + " Sig:" + str(plevel) + " Med:" + str(med) + " Bli:" + str(bl))
        ref = db.reference('/')
        ref.set({'EEG':{
                        'Serial-No':i,
                        'Signal-Level': plevel,
                        'Raw EEG' : raw,
                        'Attention': att,
                        'Meditation': med,
                        'Delta': delt,
                        'Theta': the,
                        'Low-Alpha':la,
                        'High-Alpha':ha,
                        'Low-Beta':lb,
                        'High-Beta':hb,
                        'Low-Gamma':lg,
                        'High-Gamma':hg,
                        'Blink-Strength':bl,
                        'Executed Action':stat,
                 }})
        i+=1
        if att > 70:
            Sound.volume_up()
            print('volume up')
            stat = 'Volume Up'
        if med > 60 and att < 70:
            Sound.volume_down()
            print('volume down')
            stat = 'Volume Down'
        if bl > 140:
            Sound.mute()
            print('volume mute')
            stat = 'Volume Mute'
        time.sleep(1)
