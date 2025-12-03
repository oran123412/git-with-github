#אחראית על תקשורת רשת במקרה זה UDP
import socket
#אחראית על פתיחה ושמירה של קבצים במחשב
import os

#הIP של השרת ,פה הוא מקומי
SERVER_IP = "127.0.0.1"
#הפורט שהשרת מאזין עליו
SERVER_PORT = 1234
#גודל הפקטה שהשרת שולח
PACKET_SIZE = 8192

def run_client():
    #יצרנו משתנה בשם sock ושמנו בתוכו ערך של מתודה ספציפית שנמצאת בספרית socket ,הגדרנו בסוגריים שאנו מעוניינים בחיבור שלל IPv4 בתחילת הסוגריים ובסוף הסוגרים שאנו מעוניינים בחיבור UDP ולא .TCP
    #socket פירושו שקע ותפקידו חיבור ברשת
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = input("Enter the filename you want to request: ").strip()
    #המשתנה sock הוא השקע ברשת שעושה חיבור .אנו שולחים דרכו חבילה של שם הקובץ מומר לבייטים לכתובת של השרת בIP ובפורט
    sock.sendto(filename.encode(), (SERVER_IP, SERVER_PORT))

    # === קבלת תגובה ראשונית מהשרת ===
    try:
        #recvfrom היא פונקציה שמקבלת כתובת IP ומידע מהשרת . הכתובת לא רלוונטית לכן שומרים אותה תחת _ ואילו המידע  נשמר תחת הresponse .גודל מקסימלי של קבלה בבת אחת הוא 65536
        response, _ = sock.recvfrom(65536)
    #במקרה ועבר הזמן לא מקריסים תוכנית פשוט מדפיסים .יוצאים מrun client וצריך להתחיל מההתחלה  
    except socket.timeout:
        print("No response from server (timeout on initial response).")
        return
    #אם השרת שלח לא נמצא מדפיס.ויוצא מהפונקציה וצריך להתחיל מחדש
    if response == b"NOT FOUND 404":
        print("File not found (404)")
        return
    else:
        print("Server accepted file request")
    #יוצרים משתנה של מילון לשמירת key,value
    received = {}

    while True:
        #כמו מקודם , הפונקציה מקבלת עד 65536 בייטים זו פונקציה שממתינה לקבל מידע וIP אנחנו שומרים את המידע הפעם בpacket ואת הכתובת של השרת בserver 
        packet, server = sock.recvfrom(65536)
        #השרת שלוח DONE כשסיים לשלוח את כל הפקטות .אם קיבלנו הודעה זו נצא מהלולאה
        if packet == b"DONE":
            break

        # בדיקה שהפקטה תקינה בכלל
        #הפורמט אצלנו בשרת בפקטות הוא seq|data . אם לא רואים את | זה אומר שהפקטה פגומה ואז חוזרים לתחילת הלולאה
        if b"|" not in packet:
            continue
        #יוצרים 2 משתנים מפצילים את הפקטה פעם אחת בלבד בגלל המספר 1 באזור | מה שלפני |שמים בheader ומה שאחרי שמים ב data. פקטה רגילה בנויה כך : b"5|  ABCDEFGH"
        header, data = packet.split(b"|", 1)

        try:
            #כמו בהסבר מקודם , הפקטה בנויה ממספר פקטה | ואז המידע . לוקחים את המספר ממירים אותו מבייטים וערכו שמים במשתנה
            seq = int(header.decode())
        #במידה ויש תקלה בפיענוח מספר הפקטה מתעלמים ממנה וחוזרים לתחילת הלולאה
        except:
            continue

        #שליחת הACK שולחים באמצעות הsock ממירים את המספר לטקסט ואז לבייטים ושולחים לכתובת של השרת שהוא server כמו שהוגדר למעלה 
        sock.sendto(str(seq).encode(), server)

        #אם הפקטה לא נמצאת במילון היא חדשה ומוסיפים אותה למילון ומדפיסים אם היא קיימת מדפיסים אחרת
        if seq not in received:
            print(f"Got new packet seq={seq}")
            received[seq] = data
        else:
            print(f"Duplicate packet seq={seq} (ACK re-sent)")

    #יוצרים משתנה חדש ושמים בתוכו ערך של פקטה ריקה עושים לולאה אם i מספרו נמצא במילון אז אתת המידע מצרפים לקובץ אחד בoutput
    output = b""
    i = 0
    while i in received:
        output += received[i]
        i += 1
    #יוצרים משתנה חדש ולתוכו שמים את שם הוקבץ בתוספת המילה received
    out_name = "received_" + filename
    #פןתח את הקובץ של המחשב על ידי open הוא פתח את הערך שעכשיו יישמנו ומשתמש בwb כדי לקרוא בינארית את הקובץ מגדירים אותו כ f ומשתמשים בwith כדי לסגור את הקובץ ברגע שסיימנו למנוע בעיות
    with open(out_name, "wb") as f:
        #בעזרת write תכתוב בf את כל מה ששמרת ב output
        #בקיצור שורה למעלה יצרנו קובץ חדש עם השם שלו כולל recieved ולתוכו יצקנו את הנתונים של output
        f.write(output)

    print(f"\nFile saved as: {out_name}")

    # === פתיחה אוטומטית ===
    try:
        #מריצים את הקובץ החדש
        os.startfile(out_name)
    except:
        print("Couldn't open file automatically.")
#אם הקובץ הופעל מקומית תפעיל את הפונקציה אם יובא ממקום אחר אל תפעיל 
if __name__ == "__main__":
    run_client()

#python client.py

