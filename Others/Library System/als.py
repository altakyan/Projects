from datetime import datetime, date, timedelta
import tkinter
from turtle import title, width
from dateutil.relativedelta import relativedelta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTk, Image
import pymysql

#connect to database
connect = pymysql.connect(
    host='localhost',
    user='root',
    passwd='alistair00',
    db='library',
    charset='utf8'
)
# connect
cursor = connect.cursor()

# root = Tk()
# root.title("A Library System (ALS)")

# fonts
font1 = ("Arial", 30)
font2 = ("Arial", 20)
font3 = ("Arial", 15)
font4 = ("Arial", 10)

def quit():
    destroyMainMenu()
    Tk().quit()
    cursor.close()
    connect.close()

## 1 MAIN MENU ##
def destroyMainMenu():
	mainMenu.destroy()

def mainMenuF():
    global mainMenu
    mainMenu = Toplevel()
    mainMenu.title("Main Menu")
    mainMenu.iconbitmap() # to fill
    mainMenu.geometry("1280x720")
    mainMenuHeader = Label(mainMenu, text = "(ALS)",
    font = font1, bg = "lightblue", fg = "black",
    pady = 20, padx = 600, borderwidth = 5)

    def navMainToMemb():
        membMenuF()
        destroyMainMenu()
    
    def navMainToBooks():
        booksMenuF()
        destroyMainMenu()
    
    def navMainToLoans():
        loansMenuF()
        destroyMainMenu()

    def navMainToRes():
        resMenuF()
        destroyMainMenu()

    def navMainToFines():
        fineMenuF()
        destroyMainMenu()

    def navMainToReps():
        reportMenuF()
        destroyMainMenu()

    memButton = Button(mainMenu, text = "Membership", command = navMainToMemb, 
    font = font2,
    fg = "black", bg = "green",
    padx = 58, pady = 50)
    booksButton = Button(mainMenu, text = "Books", command = navMainToBooks, 
    font = font2,
    fg = "black", bg = "green",
    padx = 80, pady = 50)
    loansButton = Button(mainMenu, text = "Loans", command = navMainToLoans, 
    font = font2,
    fg = "black", bg = "green",
    padx = 80, pady = 50)
    resButton = Button(mainMenu, text = "Reservations", command = navMainToRes, 
    font = font2,
    fg = "black", bg = "green",
    padx = 56, pady = 50)
    finesButton = Button(mainMenu, text = "Fines", command = navMainToFines, 
    font = font2,
    fg = "black", bg = "green",
    padx = 90, pady = 50)
    repsButton = Button(mainMenu, text = "Reports", command = navMainToReps, 
    font = font2, 
    fg = "black", bg = "green",
    padx = 70, pady = 50)
    quitButton = Button(mainMenu, text = "Quit", command = quit,
    font = font2,
    fg = "black", bg = "green",
    padx = 35, pady = 25)

    mainMenuHeader.grid(row = 0, column = 0, pady = 50, columnspan = 3)
    memButton.grid(row = 1, column = 0, padx = 20, pady = 50)
    booksButton.grid(row = 1, column = 1, padx = 20, pady = 50)
    loansButton.grid(row = 1, column = 2, padx = 20, pady = 50)
    resButton.grid(row = 2, column = 0, padx = 20, pady = 50)
    finesButton.grid(row = 2, column = 1, padx = 20, pady = 50)
    repsButton.grid(row = 2, column = 2, padx = 20, pady = 50)

    quitButton.grid(row = 3, column = 1)

#######################
## 2 Membership Menu ## done
#######################

def destroyMembMenu():
    membMenu.destroy()

def membMenuF():
    # Admin Work
    global membMenu
    membMenu = Toplevel()
    # Design iconbitmap, geometry
    membMenu.title("Membership")
    membMenuHeader = Label(membMenu, text = "Select one of the Options below:",
    font = font2, bg = "lightblue", fg = "black",
    pady = 20, padx = 200, borderwidth = 5)

    ## Membership Creation Menu ##
    def destroyMembCre():
        membCre.destroy()

    def membCreF():
        global membCre
        membCre = Toplevel()
        # Design
        membCre.title("Membership Creation Menu")
        membCreHeader = Label(membCre, text = "To Create Member, Please Enter Requested Information Below:",
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)
        
        membIDLabel = Label(membCre, text = "Membership ID", font = font3)
        membNameLabel = Label(membCre, text = "Name", font = font3)
        membFacLabel = Label(membCre, text = "Faculty", font = font3)
        membPNLabel = Label(membCre, text = "Phone Number", font = font3)
        membEmLabel = Label(membCre, text = "Email Address", font = font3)

        # Entry
        membID = Entry(membCre)
        membID.insert(0, "A unique alphanumeric id that distinguishes every member")
        membName = Entry(membCre)
        membName.insert(0, "Enter Member's Name")
        membFac = Entry(membCre)
        membFac.insert(0, "e.g., Comoputing, Engineering, Science, etc.")
        membPN = Entry(membCre)
        membPN.insert(0, "e.g., 91234567, 81093487, 92054981, etc")
        membEm = Entry(membCre)
        membEm.insert(0, "e.g., ALSuser@als.edu")

        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            membCre.destroy()

        def errorPop():
            global error
            error = Toplevel(membCre)
            error.title("Error!")
            errorMessage = Label(error, text = "Member already exist; Missing or Incomplete fields.")

            def errorToMembCre():
                destroyErrorPop()
                membCreF()
                membCre.lift()
                membCre.lift()

            returnButton = Button(error, text = "Back to Create Function", command = errorToMembCre)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            membCre.destroy()

        def succPop(id, name, fac, pn, em):
            # add the data into db
            sql = """INSERT IGNORE INTO Member(ID, name, faculty, phoneNo, email) VALUES
            (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (id, name, fac, pn, em))
            connect.commit()
            # popup admin
            global succ
            succ = Toplevel(membCre)
            succ.title("Success!")
            succMessage = Label(succ, text = "ALS Membership created.")

            def succToMembCre():
                destroySuccPop()
                membCreF()
                membCre.lift()
                membCre.lift()

            returnButton = Button(succ, text = "Back to Create Function", command = succToMembCre)

            succMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def createMemb():
            id = membID.get()
            name = membName.get()
            fac = membFac.get()
            pn = membPN.get()
            em = membEm.get()

            if (id == "" or name == "" or fac == "" or pn == "" or em == ""):
                return errorPop()

             # check inside sql database
            try:
                sql = """SELECT ID
                FROM Member
                WHERE ID = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sql, (id, ))
                data = cursor.fetchone()

                # check if id alr inside system
                if data == None: # empty means no clashing ID 
                    return succPop(id, name, fac, pn, em)
                else: # not empty means clash, return errorPop
                    return errorPop()
            except Exception as e:
                print(e)
            
        # create back to memb create button and function
        backToMembMenuB = Button(membCre, text = "Back To Main Menu", command = membCreToMembMenu)
        createMembButton = Button(membCre, text = "Create Member", command = createMemb)

        ### memb popup ###

        # Float Functions
        def tempTextID(e):
            membID.delete(0, END)
        def tempTextName(e):
            membName.delete(0, END)
        def tempTextFac(e):
            membFac.delete(0, END)
        def tempTextPN(e):
            membPN.delete(0, END)
        def tempTextEm(e):
            membEm.delete(0, END)
        

        # Placements
        membCreHeader.grid(row = 0, pady = 50, columnspan = 3)
        membIDLabel.grid(row = 1, column = 0, columnspan = 2)
        membID.grid(row = 1, column = 2)
        membNameLabel.grid(row = 2, column = 0, columnspan = 2)
        membName.grid(row = 2, column = 2)
        membFacLabel.grid(row = 3, column = 0, columnspan = 2)
        membFac.grid(row = 3, column = 2)
        membPNLabel.grid(row = 4, column = 0, columnspan = 2)
        membPN.grid(row = 4, column = 2)
        membEmLabel.grid(row = 5, column = 0, columnspan = 2)
        membEm.grid(row = 5, column = 2)

        createMembButton.grid(row = 6, column = 2)
        backToMembMenuB.grid(row = 6, column = 0, columnspan = 2)
        
        # create floating text
        membID.bind("<FocusIn>", tempTextID)
        membName.bind("<FocusIn>", tempTextName)
        membFac.bind("<FocusIn>", tempTextFac)
        membPN.bind("<FocusIn>", tempTextPN)
        membEm.bind("<FocusIn>", tempTextEm)

    ## Membership Deletion Menu ##
    def destroyMembDel():
        membDel.destroy()

    def membDelF():
        # Admin work
        global membDel
        membDel = Toplevel()
        # Design iconbitmap, geometry
        membDel.title("Membership Deletion")
        membDelHeader = Label(membDel, text = "To Delete Member, Please Enter Membership ID:", 
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)
        membIDLabel = Label(membDel, text = "Membership ID", font = font3)

        # Temp text
        def tempTextID(e):
            membID.delete(0, END)

        # Entry
        membID = Entry(membDel)
        membID.insert(0, "A unique alphanumeric id that distinguishes every member")
        
        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            membDel.destroy()

        def errorPop(msg):
            global error
            error = Toplevel(membDel)
            error.title("Error!")
            errorMessage = Label(error, text = msg)

            def errorToMembDel():
                destroyErrorPop()
                membDelF()
                membDel.lift()
                membDel.lift()

            returnButton = Button(error, text = "Back to Delete Function", command = errorToMembDel)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            membDel.destroy()

        def succPop(id, data):
            # popup admin
            global succ
            succ = Toplevel(membDel)
            succ.title("Confirm?")
            succMessage = Label(succ, text = "Please Confirm Details to Be Correct")
            membID = Label(succ, text = data[0])
            name = Label(succ, text = data[1])
            fac = Label(succ, text = data[2])
            pn = Label(succ, text = data[3])
            em = Label(succ, text = data[4])

            # check member has loans, reservations, fines
            loans = "SELECT memberID FROM Loan WHERE memberID = %s AND dueDate <= %s;"
            loansV = (data[0], date.today())
            cursor.execute(loans, loansV)
            loansR = cursor.fetchone()
            res = "SELECT memberID FROM Reservation WHERE memberID = %s;"
            resV = (data[0], )
            cursor.execute(res, resV)
            resR = cursor.fetchone()
            fines = "SELECT memberID FROM Fine WHERE memberID = %s AND amount != 0;"
            finesV = (data[0], )
            cursor.execute(fines, finesV)
            finesR = cursor.fetchone()

            def succToMembDel():
                destroySuccPop()
                membDelF()
                membDel.lift()
                membDel.lift()

            def checkDel():
                if (loansR != None or resR != None or finesR != None):
                    return errorPop("Member has loans, reservations or outstanding fines.")
                else:
                    return confirmDel()
            
            def confirmDel():
                sql = """DELETE FROM Member
                WHERE ID = %s
                """
                cursor.execute(sql, (id,))
                connect.commit()
                succToMembDel()

            confirmDelButton = Button(succ, text = "Confirm Deletion", command = checkDel)
            returnButton = Button(succ, text = "Back to Delete Function", command = succToMembDel)

            succMessage.grid(row = 0, column = 0)
            membID.grid(row = 1, column = 0)
            name.grid(row = 2, column = 0)
            fac.grid(row = 3, column = 0)
            pn.grid(row = 4, column = 0)
            em.grid(row = 5, column = 0)
            returnButton.grid(row = 6, column = 0)
            confirmDelButton.grid(row = 6, column = 1)

        def delMemb():
            id = membID.get()
             # check inside sql database
            try:
                sql = """SELECT ID, name, faculty, phoneNo, email
                FROM Member
                WHERE ID = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sql, (id, ))
                data = cursor.fetchone()

                # check if id alr inside system
                if data == None: 
                    return errorPop("Member does not exist!")
                else: 
                    return succPop(id, data)
            except Exception as e:
                print(e)

        # create back to memb create button and function
        backToMembMenuB = Button(membDel, text = "Back To Main Menu", command = membDelToMembMenu)
        delMembButton = Button(membDel, text = "Delete Member", command = delMemb)

        # Placements
        membDelHeader.grid(row = 0, columnspan = 3)
        membIDLabel.grid(row = 3, column = 0, columnspan = 2)
        membID.grid(row = 3, column = 2)

        delMembButton.grid(row = 6, column = 2)
        backToMembMenuB.grid(row = 6, column = 0, columnspan = 2)

        # Create floating text
        membID.bind("<FocusIn>", tempTextID)

    ## Membership Update Menu ##
    def destroyMembUpd():
        membUpd.destroy()

    def membUpdF():
        # Admin work
        global membUpd
        membUpd = Toplevel()
        # Design iconbitmap, geometry
        membUpd.title("Membership Update")
        membUpdHeader = Label(membUpd, text = "To Update a Member, Please Enter Membership ID:", 
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)
        membIDLabel = Label(membUpd, text = "Membership ID", font = font3)

        # Temp text
        def tempTextID(e):
            membID.delete(0, END)

        # Entry
        membID = Entry(membUpd)
        membID.insert(0, "A unique alphanumeric id that distinguishes every member")

        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            membUpd.destroy()

        def errorPop(msg):
            global error
            error = Toplevel(membUpd)
            error.title("Error!")
            errorMessage = Label(error, text = msg)

            def errorToMembUpd():
                destroyErrorPop()
                membUpdF()
                membUpd.lift()
                membUpd.lift()

            returnButton = Button(error, text = "Back to Update Function", command = errorToMembUpd)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)
        
        def checkID():
            id = membID.get()
             # check inside sql database
            try:
                sql = """SELECT ID, name, faculty, phoneNo, email
                FROM Member
                WHERE ID = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sql, (id, ))
                data = cursor.fetchone()

                # check if id alr inside system
                if data == None: 
                    return errorPop("Member does not exist!")
                else: 
                    print(data)
                    return membUpdToUpdMemb(data[0])
            except Exception as e:
                print(e)
        
        def updMembToMembUpdMenu():
            membUpdF()
            destroyUpdMemb()

        def membUpdToUpdMemb(id):
            updMembF(id)
            destroyMembUpd()

        def destroyUpdMemb():
            updMemb.destroy()

        def updMembF(id):
            global updMemb
            updMemb = Toplevel()
            updMemb.title("Update Membership Menu")
            updMembHeader = Label(updMemb, text = "Please Enter Requested Information Below:",
            font = font2, bg = "lightblue", fg = "black",
            pady = 20, padx = 200, borderwidth = 5)
            
            membIDLabel = Label(updMemb, text = "Membership ID", font = font3, fg = "black")
            membNameLabel = Label(updMemb, text = "Name", font = font3)
            membFacLabel = Label(updMemb, text = "Faculty", font = font3)
            membPNLabel = Label(updMemb, text = "Phone Number", font = font3)
            membEmLabel = Label(updMemb, text = "Email Address", font = font3)

            # Entry
            membID = Label(updMemb, text = "A unique alphanumeric id that distinguishes every member", fg = "grey")
            membName = Entry(updMemb)
            membName.insert(0, "Update member's name")
            membFac = Entry(updMemb)
            membFac.insert(0, "Update Faculty.. Computing, Engineering, Science, etc.")
            membPN = Entry(updMemb)
            membPN.insert(0, "Update Phone Number")
            membEm = Entry(updMemb)
            membEm.insert(0, "Update email address")

            ### POPUP ###
            def destroyErrorPop():
                error.destroy()
                membUpd.destroy()

            def errorPop(msg):
                global error
                error = Toplevel(membUpd)
                error.title("Error!")
                errorMessage = Label(error, text = msg)

                def errorToMembUpd():
                    destroyErrorPop()
                    membUpdF()
                    membUpd.lift()
                    membUpd.lift()

                returnButton = Button(error, text = "Back to Update Function", command = errorToMembUpd)

                errorMessage.grid(row = 0, column = 0)
                returnButton.grid(row = 2, column = 0)

            def destroySuccPop():
                succ.destroy()

            def succPop():
                global succ
                succ = Toplevel(updMemb)
                succ.title("Success!")
                succMessage = Label(succ, text = "ALS Membership Updated.")

                def succToMembUpd():
                    destroySuccPop()
                    destroyUpdMemb()
                    membUpdF()
                
                def succToUpdMemb():
                    destroySuccPop()

                createAnotherButton = Button(succ, text = "Confirm Update", command = succToMembUpd)
                returnButton = Button(succ, text = "Back to Update Function", command = succToUpdMemb)
                
                succMessage.grid(row = 0, column = 0)

                returnButton.grid(row = 1, column = 0)
                createAnotherButton.grid(row = 1, column = 1)


            def destroyConfPop():
                conf.destroy()
                membUpd.destroy()
                

            def confPop(id): #TODO
                # popup admin
                global conf
                conf = Toplevel(updMemb)
                conf.title("Confirm?")
                confMessage = Label(conf, text = "Please Confirm Updated Details to Be Correct")
                nameC = membName.get()
                facC = membFac.get()
                pnC = membPN.get()
                emC = membEm.get()


                membIDLabel = Label(conf, text = "ID: " + id)
                nameLabel = Label(conf, text = "Name: " + nameC)
                facLabel = Label(conf, text = "Faculty: " + facC)
                pnLabel = Label(conf, text = "Phone Number: " + pnC)
                emLabel = Label(conf, text = "Email Address: " + emC)

                def succToMembUpd():
                    destroyConfPop()

                def confToSuccPop():
                    destroyConfPop()
                    succPop()

                def confirmUpd(): # TODO
                    sql = """UPDATE Member 
                    SET name = %s, faculty = %s, phoneNo = %s, email = %s
                    WHERE ID = %s;
                    """
                    sqlV = (nameC, facC, pnC, emC, id)
                    cursor.execute(sql, sqlV)
                    connect.commit()
                    confToSuccPop()
                    
                confirmUpdButton = Button(conf, text = "Confirm Update", command = confirmUpd)
                returnButton = Button(conf, text = "Back to Update Function", command = succToMembUpd)

                confMessage.grid(row = 0, column = 0)
                membIDLabel.grid(row = 1, column = 0)
                nameLabel.grid(row = 2, column = 0)
                facLabel.grid(row = 3, column = 0)
                pnLabel.grid(row = 4, column = 0)
                emLabel.grid(row = 5, column = 0)
                returnButton.grid(row = 6, column = 0)
                confirmUpdButton.grid(row = 6, column = 1)



            def updateMemb(val):
                id = val
                # check inside sql database
                try:
                    sql = """SELECT ID, name, faculty, phoneNo, email
                    FROM Member
                    WHERE ID = %s;
                    """

                    # execute select
                    connect.ping(True)
                    cursor.execute(sql, (id, ))
                    data = cursor.fetchone()

                    # check if id alr inside system
                    if data == None: 
                        return errorPop("Missing or Incomplete fields.")
                    else: 
                        print(data)
                        return confPop(id)
                except Exception as e:
                    print(e)


            # create back to memb create button and function
            backToMembUpdB = Button(updMemb, text = "Back To Main Menu", command = updMembToMembUpdMenu)
            updateMemb1Button = Button(updMemb, text = "Update Member", command = lambda: updateMemb(id))

            # Float Functions
            def tempTextName(e):
                membName.delete(0, END)
            def tempTextFac(e):
                membFac.delete(0, END)
            def tempTextPN(e):
                membPN.delete(0, END)
            def tempTextEm(e):
                membEm.delete(0, END)
            

            # Placements
            updMembHeader.grid(row = 0, pady = 50, columnspan = 3)
            membIDLabel.grid(row = 1, column = 0, columnspan = 2)
            membID.grid(row = 1, column = 2)
            membNameLabel.grid(row = 2, column = 0, columnspan = 2)
            membName.grid(row = 2, column = 2)
            membFacLabel.grid(row = 3, column = 0, columnspan = 2)
            membFac.grid(row = 3, column = 2)
            membPNLabel.grid(row = 4, column = 0, columnspan = 2)
            membPN.grid(row = 4, column = 2)
            membEmLabel.grid(row = 5, column = 0, columnspan = 2)
            membEm.grid(row = 5, column = 2)

            updateMemb1Button.grid(row = 6, column = 2)
            backToMembUpdB.grid(row = 6, column = 0, columnspan = 2)

            # create floating text
            membName.bind("<FocusIn>", tempTextName)
            membFac.bind("<FocusIn>", tempTextFac)
            membPN.bind("<FocusIn>", tempTextPN)
            membEm.bind("<FocusIn>", tempTextEm)

        # create back to memb create button and function
        backToMembMenuB = Button(membUpd, text = "Back To Main Menu", command = membUpdToMembMenu)
        updMembButton = Button(membUpd, text = "Update Member", command = checkID)

        # Placements
        membUpdHeader.grid(row = 0, columnspan = 3)
        membIDLabel.grid(row = 3, column = 0, columnspan = 2)
        membID.grid(row = 3, column = 2)

        updMembButton.grid(row = 6, column = 2)
        backToMembMenuB.grid(row = 6, column = 0, columnspan = 2)

        # Create floating text
        membID.bind("<FocusIn>", tempTextID)

    # Functions
    def membToMain():
        mainMenuF()
        destroyMembMenu()
        mainMenu.lift()
        mainMenu.lift()
    
    def membMenuToMembCre():
        membCreF()
        destroyMembMenu()
        membCre.lift()
        membCre.lift()

    def membMenuToMembDel():
        membDelF()
        destroyMembMenu()
        membDel.lift()
        membDel.lift()

    def membMenuToMembUpd():
        membUpdF()
        destroyMembMenu()
        membUpd.lift()
        membUpd.lift()
    
    def membCreToMembMenu():
        membMenuF()
        destroyMembCre()
        membMenu.lift()
        membMenu.lift()
    
    def membDelToMembMenu():
        membMenuF()
        destroyMembDel()
        membMenu.lift()
        membMenu.lift()

    def membUpdToMembMenu():
        membMenuF()
        destroyMembUpd()
        membMenu.lift()
        membMenu.lift()

    # Buttons
    membCreButton = Button(membMenu, text = "Membership Creation", command = membMenuToMembCre, 
    font = font2,
    pady = 50, padx = 70)
    membDelButton = Button(membMenu, text = "Membership Deletion", command = membMenuToMembDel, 
    font = font2,
    pady = 50, padx = 70)
    membUpdButton = Button(membMenu, text = "Membership Update", command = membMenuToMembUpd,
    font = font2,
    pady = 50, padx = 70)
    membToMainButton = Button(membMenu, text = "Back to Main Menu", command = membToMain, 
    font = font3, bg = "lightblue", fg = "black",
    pady = 10, padx = 200, borderwidth = 5)

    # Placement of Buttons
    membMenuHeader.grid(row = 0, column = 0, pady = 25, columnspan = 3)
    membCreButton.grid(row = 1, column = 1, pady = 25)
    membDelButton.grid(row = 2, column = 1, pady = 25)
    membUpdButton.grid(row = 3, column = 1, pady = 25)
    membToMainButton.grid(row = 4, column = 0, pady = 15, columnspan = 3)

## 3 Books Menu ##

def destroyBooksMenu():
    booksMenu.destroy()

def booksMenuF():
    global booksMenu
    # Admin
    booksMenu = Toplevel()
    # Design iconbitmap, geometry
    booksMenu.title("Books")
    booksMenuHeader = Label(booksMenu, text = "Select one of the Options below:",
    font = font2, bg = "lightblue", fg = "black",
    pady = 20, padx = 200, borderwidth = 5)

    # Functions for Faces for Acquisition and Withdrawal

    ### (1/2) Book Acquisition ###
    def booksToAcq():
        bookAcqF()
        destroyBooksMenu()
        bookAcq.lift()
        bookAcq.lift()

    def destroyBookAcq():
        bookAcq.destroy()

    def bookAcqF():
        global bookAcq
        # Design iconbitmap, geometry
        bookAcq = Toplevel()
        bookAcq.title("Book Acquisition")
        bookAcqHeader = Label(bookAcq, text = "For New Book Acquisition, Please Enter Required Information Below:",
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)

        accNoLabel = Label(bookAcq, text = "Accession Number", font = font3)
        titleLabel = Label(bookAcq, text = "Title", font = font3)
        authorsLabel = Label(bookAcq, text = "Authors", font = font3)
        isbnLabel = Label(bookAcq, text = "ISBN", font = font3)
        pubLabel = Label(bookAcq, text = "Publisher", font = font3)
        pubYearLabel = Label(bookAcq, text = "Publication Year", font = font3)

        # Entry
        accNo = Entry(bookAcq)
        accNo.insert(0, "Used to identify an instance of book")
        title = Entry(bookAcq)
        title.insert(0, "Book Title")
        authors = Entry(bookAcq)
        authors.insert(0, "There can be multiple authors for a book")
        isbn = Entry(bookAcq)
        isbn.insert(0, "ISBN Number")
        pub = Entry(bookAcq)
        pub.insert(0, "Random House, Penguin, Cengage, Springer, etc.")
        pubYear = Entry(bookAcq)
        pubYear.insert(0, "Edition year")

        def destroyErrorPop():
            error.destroy()
            bookAcq.destroy()

        def errorPop():
            global error
            error = Toplevel(bookAcq)
            error.title("Error!")
            errorMessage = Label(error, text = "Book already added; Duplicate, Missing or Incomplete fields.")

            def errorToBookAcq():
                destroyErrorPop()
                bookAcqF()
                bookAcq.lift()
                bookAcq.lift()

            returnButton = Button(error, text = "Back to AcquisitionFunction", command = errorToBookAcq)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            bookAcq.destroy()

        def succPop(accNo, title, authors, isbn, pub, pubYear):
            # add the data into db
            sql1 = """INSERT IGNORE INTO Book(accessionNo, title, isbn, publisher, pubDate) VALUES
            (%s, %s, %s, %s, %s);
            """
            cursor.execute(sql1, (accNo, title, isbn, pub, pubYear))

            sql2 = """INSERT IGNORE INTO Authors(accessionNo, author) VALUES
            (%s, %s);
            """
            cursor.execute(sql2, (accNo, authors))
            connect.commit()

            # popup admin
            global succ
            succ = Toplevel(bookAcq)
            succ.title("Success!")
            succMessage = Label(succ, text = "New Book added in Library.")

            def succToBookAcq():
                destroySuccPop()
                bookAcqF()
                bookAcq.lift()
                bookAcq.lift()

            returnButton = Button(succ, text = "Back to Acquisition Function", command = succToBookAcq)

            succMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def addBook():
            accNoC = accNo.get()
            titleC = title.get()
            authorsC = authors.get()
            isbnC = isbn.get()
            pubC = pub.get()
            pubYearC = pubYear.get()

            if (accNoC == "" or titleC == "" or authorsC == "" or isbnC == "" or pubC == "" or pubYearC == ""):
                return errorPop()
            else:
                try:
                    sql = """SELECT accessionNo
                    FROM Book
                    WHERE accessionNo = %s;
                    """
                    sqlV = (accNoC, )


                    # execute select
                    connect.ping(True)
                    cursor.execute(sql, sqlV)
                    data = cursor.fetchone()

                    # check if id alr inside system
                    if data == None: # empty means no clashing ID 
                        return succPop(accNoC, titleC, authorsC, isbnC, pubC, pubYearC)
                    else: # not empty means clash, return errorPop
                        return errorPop()
                except Exception as e:
                    print(e)

        def acqToBooksMenu():
            booksMenuF()
            destroyBookAcq()
            booksMenu.lift()
            booksMenu.lift()

        acqToBooksButton = Button(bookAcq, text = "Back To Books Menu", command = acqToBooksMenu)
        addBookButton = Button(bookAcq, text = "Add New Book", command = addBook)
        


        # Float Functions
        def tempTextAccNo(e):
            accNo.delete(0, END)
        def tempTextTitle(e):
            title.delete(0, END)
        def tempTextAuthors(e):
            authors.delete(0, END)
        def tempTextISBN(e):
            isbn.delete(0, END)
        def tempTextPub(e):
            pub.delete(0, END)
        def tempTextPubYear(e):
            pubYear.delete(0, END)

        # Placements
        bookAcqHeader.grid(row = 0, column = 0, columnspan = 3)
        accNoLabel.grid(row = 1, column = 0, columnspan = 2)
        accNo.grid(row = 1, column = 2)
        titleLabel.grid(row = 2, column = 0, columnspan = 2)
        title.grid(row = 2, column = 2)
        authorsLabel.grid(row = 3, column = 0, columnspan = 2)
        authors.grid(row = 3, column = 2)
        isbnLabel.grid(row = 4, column = 0, columnspan = 2)
        isbn.grid(row = 4, column = 2)
        pubLabel.grid(row = 5, column = 0, columnspan = 2)
        pub.grid(row = 5, column = 2)
        pubYearLabel.grid(row = 6, column = 0, columnspan = 2)
        pubYear.grid(row = 6, column = 2)
        acqToBooksButton.grid(row = 7, column = 0)
        addBookButton.grid(row = 7, column = 1)

        # create Floating Texts

        accNo.bind("<FocusIn>", tempTextAccNo)
        title.bind("<FocusIn>", tempTextTitle)
        authors.bind("<FocusIn>", tempTextAuthors)
        isbn.bind("<FocusIn>", tempTextISBN)
        pub.bind("<FocusIn>", tempTextPub)
        pubYear.bind("<FocusIn>", tempTextPubYear)


    ### (2/2) Book Withdrawal ###
    def booksToWith():
        bookWithF()
        destroyBooksMenu()
        bookWith.lift()
        bookWith.lift()
    
    def destroyBookWith():
        bookWith.destroy()

    def bookWithF():
        global bookWith
        # Design iconbitmap, geometry
        bookWith = Toplevel()
        bookWith.title("Book Withdrawal")
        bookWithHeader = Label(bookWith, text = "To Remove Outdated Books From System, Please Enter Required Information Below:",
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)

        accNoLabel = Label(bookWith, text = "Accession Number", font = font3)
        

        # Entry
        accNo = Entry(bookWith)
        accNo.insert(0, "Used to identify an instance of book")
        
        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            bookWith.destroy()

        def errorPop(msg):
            global error
            error = Toplevel(bookWith)
            error.title("Error!")
            errorMessage = Label(error, text = msg)

            def errorToBookWith():
                destroyErrorPop()
                bookWithF()
                bookWith.lift()
                bookWith.lift()

            returnButton = Button(error, text = "Back to Withdrawal Function", command = errorToBookWith)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            bookWith.destroy()

        def succPop(data):
            # popup admin
            global succ
            succ = Toplevel(bookWith)
            succ.title("Confirm?")
            succMessage = Label(succ, text = "Please Confirm Details to Be Correct")
            accNo = Label(succ, text = data[0])
            title = Label(succ, text = data[1])
            isbn = Label(succ, text = data[2])
            pub = Label(succ, text = data[3])
            pubYear = Label(succ, text = data[4])


            def succToBookWith():
                destroySuccPop()
                bookWithF()
                bookWith.lift()
                bookWith.lift()
            
            def confirmWith():
                sql = """DELETE FROM Book
                WHERE accessionNo = %s;
                """
                try:
                    connect.ping(True)
                    cursor.execute(sql, (data[0], ))
                    connect.commit()
                except Exception as e:
                    print(e)
                succToBookWith()

            confirmWithButton = Button(succ, text = "Confirm Withdrawal", command = confirmWith)
            returnButton = Button(succ, text = "Back to Withdrawal Function", command = succToBookWith)

            succMessage.grid(row = 0, column = 0)
            accNo.grid(row = 1, column = 0)
            title.grid(row = 2, column = 0)
            isbn.grid(row = 3, column = 0)
            pub.grid(row = 4, column = 0)
            pubYear.grid(row = 5, column = 0)
            returnButton.grid(row = 6, column = 0)
            confirmWithButton.grid(row = 6, column = 1)

        def withBook():
            access = accNo.get()
             # check inside sql database
            try:
                sql = """SELECT accessionNo, title, isbn, publisher, pubDate
                FROM Book
                WHERE accessionNo = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sql, (access, ))
                data = cursor.fetchone()

                ## check if have loans or reservations
                sqlLoan = """SElECT accessionNo 
                FROM Loan
                WHERE accessionNo = %s
                """
                sqlRes = """SELECT accessionNo
                FROM Reservation
                WHERE accessionNo = %s
                """
                cursor.execute(sqlLoan, (access, ))
                checkLoan = cursor.fetchone()
                cursor.execute(sqlRes, (access, ))
                checkRes = cursor.fetchone()

                # check if id alr inside system
                if data == None: 
                    return errorPop("Book does not exist!")
                elif checkLoan != None:
                    return errorPop("Book is currently on Loan.")
                elif checkRes != None:
                    return errorPop("Book is currently Reserved.")
                else: 
                    return succPop(data)
            except Exception as e:
                print(e)

        def withToBooksMenu():
            booksMenuF()
            destroyBookWith()
            booksMenu.lift()
            booksMenu.lift()

        # create back to memb create button and function
        withToBooksMenuB = Button(bookWith, text = "Back To Books Menu", command = withToBooksMenu)
        withBookButton = Button(bookWith, text = "Withdraw Book", command = withBook)

        # Float
        def tempTextAccNo(e):
            accNo.delete(0, END)

        # Placements
        bookWithHeader.grid(row = 0, column = 0, columnspan = 3)
        accNoLabel.grid(row = 1, column = 0, columnspan = 2)
        accNo.grid(row = 1, column = 2)

        withToBooksMenuB.grid(row = 2, column = 0)
        withBookButton.grid(row = 2, column = 1)

        # Floating text
        accNo.bind("<FocusIn>", tempTextAccNo)


    def booksToMain():
        mainMenuF()
        destroyBooksMenu()
        mainMenu.lift()
        mainMenu.lift()

    # Buttons
    bookAcqButton = Button(booksMenu, text = "Book Acquisition", command = booksToAcq)
    bookWithButton = Button(booksMenu, text = "Book Withdrawal", command = booksToWith)
    booksToMainButton = Button(booksMenu, text = "Back to Main Menu", command = booksToMain)

    # Placement of Buttons
    booksMenuHeader.grid(row = 0, column = 0, columnspan = 3)
    bookAcqButton.grid(row = 1, column = 0)
    bookWithButton.grid(row = 2, column = 0)
    booksToMainButton.grid(row = 3, column = 0)

## 4 Loans Menu ##

def destroyLoansMenu():
    loansMenu.destroy()

def loansMenuF():
    global loansMenu
    # Admin
    loansMenu = Toplevel()
    # Design iconbitmap, geometry
    loansMenu.title("Loans")
    loansMenuHeader = Label(loansMenu, text = "Select one of the Options below:",
    font = font2, bg = "lightblue", fg = "black",
    pady = 20, padx = 200, borderwidth = 5)

    # Functions for Faces for Borrowing and Returning

    ### (1/2) Book Borrowing ###
    def loansToBorrow():
        borrowF()
        destroyLoansMenu()
        borrow.lift()
        borrow.lift()

    def destroyBorrow():
        borrow.destroy()

    def borrowF():
        global borrow
        # Design iconbitmap, geometry
        borrow = Toplevel()
        borrow.title("Book Borrowing")
        borrowHeader = Label(borrow, text = "To Borrow a Book, Please Enter Information Below:",
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)

        accNoLabel = Label(borrow, text = "Accession Number", font = font3)
        membIDLabel = Label(borrow, text = "Membership ID", font = font3)


        # Entry
        accNo = Entry(borrow)
        accNo.insert(0, "Used to identify an instance of book")
        membID = Entry(borrow)
        membID.insert(0, "A unique alphanumeric id that distinguishes every member")

        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            borrow.destroy()

        def errorPop(msg):
            global error
            error = Toplevel(borrow)
            error.title("Error!")
            errorMessage = Label(error, text = msg)

            def errorToBorrow():
                destroyErrorPop()
                borrowF()
                borrow.lift()
                borrow.lift()

            returnButton = Button(error, text = "Back to Borrow Function", command = errorToBorrow)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            borrow.destroy()

        def succPop(dataB, dataM):
            # popup admin
            global succ
            succ = Toplevel(borrow)
            succ.title("Confirm?")
            succMessage = Label(succ, text = "Please Confirm Loan Details to Be Correct")
            accNo = dataB[0]
            title = dataB[1]
            borrowDate = date.today()
            dueDate = borrowDate + timedelta(days = 14)
            membID = dataM[0]
            name = dataM[1]

            accNoL = Label(succ, text = accNo)
            titleL = Label(succ, text = title)
            borrowDateL = Label(succ, text = borrowDate)
            dueDateL = Label(succ, text = dueDate)
            membIDL = Label(succ, text = membID)
            nameL = Label(succ, text = name)

            def succToBorrow():
                destroySuccPop()
                borrowF()
            
            def confirmBorrow():
                sql = """INSERT IGNORE INTO Loan(accessionNo, borrowDate, dueDate, memberID) VALUES
                (%s, %s, %s, %s);
                """
                try:
                    connect.ping(True)
                    cursor.execute(sql, (accNo, borrowDate, dueDate, membID))
                    connect.commit()
                except Exception as e:
                    print(e)
                succToBorrow()

            confirmBorrowButton = Button(succ, text = "Confirm Loan", command = confirmBorrow)
            returnButton = Button(succ, text = "Back to Borrow Function", command = succToBorrow)

            succMessage.grid(row = 0, column = 0)
            accNoL.grid(row = 1, column = 0)
            titleL.grid(row = 2, column = 0)
            borrowDateL.grid(row = 3, column = 0)
            dueDateL.grid(row = 4, column = 0)
            membIDL.grid(row = 5, column = 0)
            nameL.grid(row = 6, column = 0)
            returnButton.grid(row = 7, column = 0)
            confirmBorrowButton.grid(row = 8, column = 1)

        def borrowBook():
            access = accNo.get()
            id = membID.get()
                # check inside sql database
            try:
                sqlB = """SELECT accessionNo, title
                FROM Book
                WHERE accessionNo = %s;
                """
                sqlM = """SELECT ID, name
                FROM Member
                WHERE ID = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sqlB, (access, ))
                data1 = cursor.fetchone()
                cursor.execute(sqlM, (id, ))
                data2 = cursor.fetchone()

                ## check if have loans or reservations
                # check for fines
                sqlFine = """SELECT memberID
                FROM Fine
                WHERE memberID = %s;
                """
                # check if loaned by others
                sqlLoanByOther = """SELECT accessionNo 
                FROM Loan
                WHERE accessionNo = %s AND memberID != %s;
                """
                # check if book count > 2
                sqlBookCount = """SELECT accessionNo, memberID
                FROM Loan
                WHERE accessionNo = %s AND memberID = %s;
                """

                sqlRes = """SELECT accessionNo
                FROM Reservation
                WHERE accessionNo = %s AND memberID = %s;
                """
                
                cursor.execute(sqlFine, (id, ))
                checkFine = cursor.fetchone()
                
                cursor.execute(sqlLoanByOther, (access, id))
                checkLoanByOther = cursor.fetchone()

                cursor.execute(sqlBookCount, (access, id))
                checkBookCount = len(cursor.fetchall())
                
                cursor.execute(sqlRes, (access, id))
                checkRes = cursor.fetchone()

                # check if id alr inside system
                if data1 == None: 
                    return errorPop("Book does not exist!")
                elif data2 == None: 
                    return errorPop("Member does not exist!")
                elif checkRes != None:
                    return errorPop("Book reserved by someone else.")
                elif checkFine != None:
                    return errorPop("Member has outstanding fines.")
                elif checkLoanByOther != None:
                    return errorPop("Book currently on Loan until: " + checkLoanByOther[2])
                elif checkBookCount >= 2:
                    return errorPop("Member loan quota exceeded.")
                else: 
                    return succPop(data1, data2)
            except Exception as e:
                print(e)

        def borrowToLoansMenu():
            loansMenuF()
            destroyBorrow()
            loansMenu.lift()
            loansMenu.lift()

        borrowToloansButton = Button(borrow, text = "Back To Loans Menu", command = borrowToLoansMenu)
        borrowBookButton = Button(borrow, text = "Borrow Book", command = borrowBook)
        
        # Float Functions
        def tempTextAccNo(e):
            accNo.delete(0, END)
        def tempTextMembID(e):
            membID.delete(0, END)

        # Placements
        borrowHeader.grid(row = 0, column = 0, columnspan = 3)
        
        accNoLabel.grid(row = 1, column = 0, columnspan = 2)
        accNo.grid(row = 1, column = 2)
        membIDLabel.grid(row = 2, column = 0, columnspan = 2)
        membID.grid(row = 2, column = 2)
        
        borrowToloansButton.grid(row = 3, column = 0)
        borrowBookButton.grid(row = 3, column = 1)

        # create Floating Texts

        accNo.bind("<FocusIn>", tempTextAccNo)
        membID.bind("<FocusIn>", tempTextMembID)
        


    ### (2/2) Book Returning ###
    def loansToReturnB():
        returnBF()
        destroyLoansMenu()
        returnB.lift()
        returnB.lift()
    
    def destroyreturnB():
        returnB.destroy()

    def returnBF():
        global returnB
        # Design iconbitmap, geometry
        returnB = Toplevel()
        returnB.title("Book Returning")
        returnBHeader = Label(returnB, text = "To Return a Book, Please Enter Information Below:",
        font = font2, bg = "lightblue", fg = "black",
        pady = 20, padx = 200, borderwidth = 5)

        accNoLabel = Label(returnB, text = "Accession Number", font = font3)
        returnDateLabel = Label(returnB, text = "Return Date", font = font3)

        # Entry
        accNo = Entry(returnB)
        accNo.insert(0, "Used to identify an instance of book")
        returnDate = Entry(returnB)
        returnDate.insert(0, "Date of book return")
        
        
        ### POPUP ###
        def destroyErrorPop():
            error.destroy()
            returnB.destroy()

        def errorPop(msg):
            global error
            error = Toplevel(returnB)
            error.title("Error!")
            errorMessage = Label(error, text = msg)

            def errorToReturnB():
                destroyErrorPop()
                returnBF()

            returnButton = Button(error, text = "Back to Return Function", command = errorToReturnB)

            errorMessage.grid(row = 0, column = 0)
            returnButton.grid(row = 2, column = 0)

        def destroySuccPop():
            succ.destroy()
            returnB.destroy()


        def succPop(dataL):
            # popup admin
            global succ
            succ = Toplevel(returnB)
            succ.title("Confirm?")
            succMessage = Label(succ, text = "Confirm Return Details to Be Correct")

            accNo = dataL[0]
            borrowDate = dataL[1]
            dueDate = dataL[2]
            membID = dataL[3]
            returnDate = date.today()

            sqlB = """SELECT title
            FROM Book
            WHERE accessionNo = %s;
            """
            cursor.execute(sqlB, (accNo, ))
            dataB = cursor.fetchone()

            sqlM = """SELECT name
            FROM Member
            WHERE ID = %s;
            """
            cursor.execute(sqlM, (membID, ))
            dataM = cursor.fetchone()

            fAmount = (returnDate - dueDate).days
            if fAmount < 0:
                fAmount = 0

            accNoL = Label(succ, text = accNo)
            titleL = Label(succ, text = dataB[0])
            borrowDateL = Label(succ, text = borrowDate)
            dueDateL = Label(succ, text = dueDate)
            membIDL = Label(succ, text = membID)
            nameL = Label(succ, text = dataM[0])
            fAmountL = Label(succ, text = fAmount)
            returnDateL = Label(succ, text = date.today())

            def succToReturnB():
                destroySuccPop()
                returnBF()
            

            def confirmReturn():
                # Remove from loan
                sqlL = """DELETE FROM Loan
                WHERE accessionNo = %s AND memberID = %s;
                """

                # Insert into returns
                sqlR = """INSERT INTO returns VALUES
                (%s, %s, %s);
                """

                # Insert into Fine
                sqlF = """INSERT INTO Fine VALUES
                (%s, %s, %s);
                """
                try:
                    connect.ping(True)
                    cursor.execute(sqlL, (accNo, membID))
                    cursor.execute(sqlR, (date.today(), accNo, membID))
                    cursor.execute(sqlF, (date.today(), fAmount, membID))
                    connect.commit()
                except Exception as e:
                    print(e)
                succToReturnB()

            confirmBorrowButton = Button(succ, text = "Confirm Return", command = confirmReturn)
            returnButton = Button(succ, text = "Back to Return Function", command = succToReturnB)

            succMessage.grid(row = 0, column = 0)
            accNoL.grid(row = 1, column = 0)
            titleL.grid(row = 2, column = 0)
            membIDL.grid(row = 3, column = 0)
            nameL.grid(row = 4, column = 0)
            returnDateL.grid(row = 5, column = 0)
            fAmountL.grid(row = 6, column = 0)
            returnButton.grid(row = 7, column = 0)
            confirmBorrowButton.grid(row = 8, column = 1)


        def returnBook():
            access = accNo.get()
            returnD = returnDate.get()
                # check inside sql database
            try:
                sqlL = """SELECT accessionNo, borrowDate, dueDate, memberID
                FROM Loan
                WHERE accessionNo = %s;
                """

                # execute select
                connect.ping(True)
                cursor.execute(sqlL, (access, ))
                data1 = cursor.fetchone()

                # check if id alr inside system
                if data1 == None: 
                    return errorPop("Loan does not exist!")
                else: 
                    return succPop(data1)
            except Exception as e:
                print(e)


        def returnBToLoansMenu():
            loansMenuF()
            destroyreturnB()
            loansMenu.lift()
            loansMenu.lift()
        
        
        returnBToloansButton = Button(returnB, text = "Back To Loans Menu", command = returnBToLoansMenu)
        returnBookButton = Button(returnB, text = "Return Book", command = returnBook)
        # Float
        def tempTextAccNo(e):
            accNo.delete(0, END)
        def tempTextReturnDate(e):
            returnDate.delete(0, END)

        # Placements
        returnBHeader.grid(row = 0, column = 0, columnspan = 3)

        accNoLabel.grid(row = 1, column = 0, columnspan = 2)
        accNo.grid(row = 1, column = 2)
        returnDateLabel.grid(row = 2, column = 0, columnspan = 2)
        returnDate.grid(row = 2, column = 2)

        returnBToloansButton.grid(row = 3, column = 0)
        returnBookButton.grid(row = 3, column = 1)

        # Floating text
        accNo.bind("<FocusIn>", tempTextAccNo)
        returnDate.bind("<FocusIn>", tempTextReturnDate)

    def loansToMain():
        mainMenuF()
        destroyLoansMenu()
        mainMenu.lift()
        mainMenu.lift()

    # Buttons
    borrowButton = Button(loansMenu, text = "Book Borrowing", command = loansToBorrow)
    returnBButton = Button(loansMenu, text = "Book Returning", command = loansToReturnB)
    loansToMainButton = Button(loansMenu, text = "Back to Main Menu", command = loansToMain)

    # Placement of Buttons
    loansMenuHeader.grid(row = 0, column = 0, columnspan = 3)
    borrowButton.grid(row = 1, column = 0)
    returnBButton.grid(row = 2, column = 0)
    loansToMainButton.grid(row = 3, column = 0)


## 5 Reservation Menu ##
def destroyResMenu():
    resMenu.destroy()

def resMenuF():
    # Admin Work
    global resMenu
    resMenu = Toplevel()
    # Design iconbitmap, geometry
    resMenu.title("Reservations")
    resMenu.geometry("1280x720")
    
    # Functions
    def resToMain():
        mainMenuF()
        destroyResMenu()

    def resMenuToBookRes():
        bookResF()
        destroyResMenu()

    def resMenuToResCan():
        resCanF()
        destroyResMenu()

    ## Book Reservation Menu ##
    def bookResF():
        global bookRes
        bookRes = Toplevel()
        bookRes.title("Book Reservation Menu")
        bookRes.geometry("1280x720")

        header = Label(bookRes, text = "To Reserve a Book, Please Enter Information Below:", borderwidth=5, bg="lightblue", padx=350,fg="black", pady=20)
        accNoLabel = Label(bookRes, text = "Accession Number")
        membIDLable = Label(bookRes, text = "Membership ID")
        resDateLabel = Label(bookRes, text = "Reserve date")

        accNo = Entry(bookRes)
        membID = Entry(bookRes)
        resDate = Label(bookRes, text = date.today())

        def popReserveDetail(result):
            global reserveDetail
            reserveDetail = Toplevel()
            reserveDetail.title("Confirmation")
            reserveDetail.geometry("500x800")
            reserveDetail.config(bg="green")

            # showing information
            message = Label(reserveDetail, text = "Confirm Reservation Details To Be Correct")
            accLabel = Label(reserveDetail, text = result[0])
            titleLabel = Label(reserveDetail, text = result[1])
            idLabel = Label(reserveDetail, text = result[2])
            nameLable= Label(reserveDetail, text = result[3])
            dateLabel = Label(reserveDetail, text = date.today())
            
            # Function
            def backToReserve():
                reserveDetail.destroy()

            def addReservation(accessionNo, reserveDate, memberID):
                try:
                    sql = "INSERT INTO reservation(accessionNo, reserveDate, memberID) VALUES (%s, DATE %s, %s)"
                    data = (accessionNo, reserveDate, memberID)
                    cursor.execute(sql, data)
                except Exception as e:
                    print(e)
                else:
                    connect.commit()
                return backToReserve

            # Button
            confirmButton = Button(reserveDetail, text="Confirm Reservation", command = addReservation(result[0], date.today(),result[2]))
            backButton = Button(reserveDetail, text = "Back to Reserve Function", command = backToReserve)

            # Placement of label and buttons
            message.grid(row=0, column=0, columnspan=2)
            accLabel.grid(row=1, column=0, columnspan=2)
            titleLabel.grid(row=2, column=0, columnspan=2)
            idLabel.grid(row=3, column=0, columnspan=2)
            nameLable.grid(row=4, column=0, columnspan=2)
            dateLabel.grid(row=5, column=0, columnspan=2)
            confirmButton.grid(row=6, column=0, columnspan=1)
            backButton.grid(row=6, column=1, columnspan=1)

        # Function
        def backToResMenu():
            resMenuF()
            bookRes.destroy()

        def popError(errorMessage):
            global errorPop
            errorPop = Toplevel()
            errorPop.title("Error")
            errorPop.geometry("500x800")
            errorPop.config(bg="red")

            header = Label(errorPop, text = "Error!")
            message = Label(errorPop, text = errorMessage)
            
            def backToReserve():
                errorPop.destroy()
                
            backButton = Button(errorPop, text = "Back to Reserve Function", command = backToReserve)

            header.grid(row=0)
            message.grid(row=1)
            backButton.grid(row=2)

        def tryReserve():
            accessionNo = accNo.get()
            memberID = membID.get()

            def BookOnLoan(accessionNo):
                sql = "SELECT * FROM loan WHERE accessionNo = %s"
                cursor.execute(sql, accessionNo)
                return cursor.rowcount > 0  # true on loan, false not on loan

            def memberExist(memberID):
                sql = "SELECT * FROM member WHERE ID = %s"
                cursor.execute(sql, memberID)
                return cursor.rowcount > 0 

            def memberLimit(memberID):
                sql = "SELECT * FROM reservation WHERE memberID = %s"
                cursor.execute(sql, memberID)
                return cursor.rowcount >= 2 # true has 2 reservations
            
            def memberFine(memberID):
                sql = "SELECT * FROM fine WHERE memberID = %s"
                cursor.execute(sql, memberID)
                if cursor.rowcount == 0:
                    return 0
                else:
                    fine = cursor.fetchone()
                    return fine[1] # 0 if no fine.

            if BookOnLoan(accessionNo):
                if memberExist(memberID):
                    if memberLimit(memberID):
                        return popError("Member currently has 2 Books on Reservation.")
                    elif memberFine(memberID) > 0:
                        return popError(f"Member has Outstanding Fine of: ${memberFine(memberID)}")
                    else:
                        try:
                            sql = "SELECT accessionNo, title, ID, name FROM book, member WHERE (accessionNo = %s AND ID = %s)"
                            data = (accessionNo, memberID)
                            cursor.execute(sql, data)
                            result = cursor.fetchone()
                            return popReserveDetail(result)
                        except Exception as e:
                            return popError(e)
                else:
                    return popError("Wrong membership ID")
            else:
                return popError("Book cannot be reserved or Wrong accession number")

                
        resBookButton = Button(bookRes, text = "Reserve Book", command = tryReserve)
        backToResMenuButton = Button(bookRes, text = "Back to Reservations Menu", command = backToResMenu)

        # Placement of Lables and Buttons
        header.grid(row = 0, column=0, pady=50, columnspan=3)
        accNoLabel.grid(row = 1, column = 0)
        membIDLable.grid(row = 2, column = 0)
        resDateLabel.grid(row = 3, column = 0)
        accNo.grid(row = 1, column = 1)
        membID.grid(row = 2, column = 1)
        resDate.grid(row = 3, column = 1)
        resBookButton.grid(row = 4, column = 0)
        backToResMenuButton.grid(row = 4, column = 1)

    ## Reservation Cancellation Menu ##
    # slide 38
    def resCanF():
        global resCancel
        resCancel = Toplevel()
        # Design
        resCancel.title("Reservation Cancellation Menu")
        resCancel.geometry("1280x720")

        header = Label(resCancel, text = "To Cancel a Reservation, Please Enter Information Below:", borderwidth=5, bg="lightblue", padx=350,fg="black", pady=20)
        accNoLabel = Label(resCancel, text = "Accession Number")
        membIDLable = Label(resCancel, text = "Membership ID")
        canDateLabel = Label(resCancel, text = "Cancel date")

        accNo = Entry(resCancel)
        membID = Entry(resCancel)
        canDate = Label(resCancel, text = date.today())
        
        def popCancelDetail(result):
            global cancelDetail
            cancelDetail = Toplevel()
            cancelDetail.title("Confirmation")
            cancelDetail.geometry("500x800")
            cancelDetail.config(bg="green")

            # showing information
            message = Label(cancelDetail, text = "Confirm Cancellation Details To Be Correct")
            accLabel = Label(cancelDetail, text = result[0])
            titleLabel = Label(cancelDetail, text = result[1])
            idLabel = Label(cancelDetail, text = result[2])
            nameLable= Label(cancelDetail, text = result[3])
            dateLabel = Label(cancelDetail, text = date.today())
            
            # Function
            def backToCancel():
                cancelDetail.destroy()

            def deleteReservation(accessionNo, memberID):
                try:
                    sql = "DELETE FROM reservation WHERE (accessionNo = %s AND memberID = %s)"
                    data = (accessionNo, memberID)
                    cursor.execute(sql, data)
                except Exception as e:
                    print(e)
                else:
                    connect.commit()
                return backToCancel

            # Button
            confirmButton = Button(cancelDetail, text="Confirm Cancellation", command = deleteReservation(result[0],result[2]))
            backButton = Button(cancelDetail, text = "Back to Cancellation Function", command = backToCancel)

            # Placement of label and buttons
            message.grid(row=0, column=0, columnspan=2)
            accLabel.grid(row=1, column=0, columnspan=2)
            titleLabel.grid(row=2, column=0, columnspan=2)
            idLabel.grid(row=3, column=0, columnspan=2)
            nameLable.grid(row=4, column=0, columnspan=2)
            dateLabel.grid(row=5, column=0, columnspan=2)
            confirmButton.grid(row=6, column=0, columnspan=1)
            backButton.grid(row=6, column=1, columnspan=1)

        def popError(errorMessage):
            global errorPop
            errorPop = Toplevel()
            errorPop.title("Error")
            errorPop.geometry("500x800")
            errorPop.config(bg="red")

            header = Label(errorPop, text = "Error!")
            message = Label(errorPop, text = errorMessage)
            
            def backToReserve():
                errorPop.destroy()
                
            backButton = Button(errorPop, text = "Back to Cancellation Function", command = backToReserve)

            header.grid(row=0)
            message.grid(row=1)
            backButton.grid(row=2)

        def tryCancel():
            accessionNo = accNo.get()
            memberID = membID.get()
            
            def reservationExist(accessionNo, memberID):
                sql = "SELECT * FROM reservation WHERE (accessionNo = %s AND memberID = %s)"
                data = (accessionNo, memberID)
                cursor.execute(sql, data)
                return cursor.rowcount > 0 # true 
            
            def bookOnLoan(accessionNo):
                sql = "SELECT * FROM loan WHERE accessionNo = %s"
                cursor.execute(sql, accessionNo)
                return cursor.rowcount > 0 # true on loan, false not on loan
            
            if reservationExist(accessionNo, memberID):
                if bookOnLoan(accessionNo):
                    try:
                        sql = "SELECT accessionNo, title, ID, name FROM book, member WHERE (accessionNo = %s AND ID = %s)"
                        data = (accessionNo, memberID)
                        cursor.execute(sql, data)
                        result = cursor.fetchone()
                        return popCancelDetail(result)
                    except Exception as e:
                        popError(e)
                else:
                    popError("Cannot cancel reservation.")
            else:
                popError("Member has no such reservation.")

        def backToResMenu():
            resMenuF()
            resCancel.destroy()

        cancelButton = Button(resCancel, text = "Cancel Reservation", command = tryCancel)
        backToResMenuButton = Button(resCancel, text = "Back to Reservations Menu", command = backToResMenu)

        # Placement of Lables and Buttons
        header.grid(row = 0, column=0, pady=50, columnspan=3)
        accNoLabel.grid(row = 1, column = 0)
        membIDLable.grid(row = 2, column = 0)
        canDateLabel.grid(row = 3, column = 0)
        accNo.grid(row = 1, column = 1)
        membID.grid(row = 2, column = 1)
        canDate.grid(row = 3, column = 1)
        cancelButton.grid(row = 4, column = 0)
        backToResMenuButton.grid(row = 4, column = 1)

    #Buttons
    resBookButton = Button(resMenu, text = "Book Reservation", command = resMenuToBookRes)
    cancelResButton = Button(resMenu, text = "Reservation Cancellation", command = resMenuToResCan)
    resToMainButton = Button(resMenu, text = "Back to Main Menu", command = resToMain)

    # Placement of Buttons
    resBookButton.grid(row = 0, column = 0)
    cancelResButton.grid(row = 1, column = 0)
    resToMainButton.grid(row = 3, column = 0)


## 6 Fine Menu ## 
# slide 41    
def destroyFineMenu():
    fineMenu.destroy()

def fineMenuF():
    # Admin Work
    global fineMenu
    fineMenu = Toplevel()
    # Design iconbitmap, geometry
    fineMenu.title("Fines")
    fineMenu.geometry("1280x720")

    # Functions
    def fineToMain():
        mainMenuF()
        destroyFineMenu()

    def fineMenuToPayment():
        paymentF()
        destroyFineMenu()

    # Fine Payment Menu #
    def paymentF():
        global payment
        payment = Toplevel()
        # Design
        payment.title("Fine Payment Menu")
        payment.geometry("1280x720")

        header = Label(payment, text = "To Pay a Fine, Please Enter Information Below:", borderwidth=5, bg="lightblue", padx=350,fg="black", pady=20)
        membIDLable = Label(payment, text = "Membership ID")
        payDateLabel = Label(payment, text = "Payment date")
        payAmtLabel = Label(payment, text = "Payment Amount")

        membID = Entry(payment)
        payDate = Label(payment, text = date.today())
        payAmt = Entry(payment)

        def popDetail(memberID, payAmount):
            global payDetail
            payDetail = Toplevel()
            payDetail.title("Confirmation")
            payDetail.geometry("500x800")
            payDetail.config(bg="green")

            # showing information
            amount = "Payment Due: $" + payAmount
            message = Label(payDetail, text = "Please Confirm Details to Be Correct")
            paymentLabel = Label(payDetail, text = amount  )
            feeLabel = Label(payDetail, text = "Exact Fee Only")
            membLabel = Label(payDetail, text = memberID)
            dateLabel = Label(payDetail, text = date.today())
            
            # Function
            def backToPay():
                payDetail.destroy()

            def clearFine(paymentDate, memberID):
                try:
                    sql = "UPDATE fine SET paymentDate = DATE %s , amount = %s WHERE memberID = %s"
                    data = (paymentDate, 0, memberID)
                    cursor.execute(sql, data)
                except Exception as e:
                    print(e)
                else:
                    connect.commit()
                return backToPay

            # Button
            confirmButton = Button(payDetail, text="Confirm Payment", command = clearFine(date.today(), memberID))
            backButton = Button(payDetail, text = "Back to Payment Function", command = backToPay)

            # Placement of label and buttons
            message.grid(row=0, column=0, columnspan=2)
            paymentLabel.grid(row=1, column=0)
            feeLabel.grid(row=2, column=0)
            membLabel.grid(row=1, column=1)
            dateLabel.grid(row=2, column=1)
            confirmButton.grid(row=3, column=0)
            backButton.grid(row=3, column=1)


        def popError(errorMessage):
            global errorPop
            errorPop = Toplevel()
            errorPop.title("Error")
            errorPop.geometry("500x800")
            errorPop.config(bg="red")

            header = Label(errorPop, text = "Error!")
            message = Label(errorPop, text = errorMessage)
            
            def backToPay():
                errorPop.destroy()
                
            backButton = Button(errorPop, text = "Back to Payment Function", command = backToPay)

            header.grid(row=0)
            message.grid(row=1)
            backButton.grid(row=2)
            
        def tryPay():
            memberID = membID.get()
            payAmount = payAmt.get()

            def memberHasFine(memberID):
                sql = "SELECT * FROM fine WHERE memberID = %s"
                cursor.execute(sql, memberID)
                if cursor.rowcount == 0:
                    return False
                else:
                    result = cursor.fetchone()
                    if result[1] == 0:
                        return False
                    else:
                        return True

            def rightAmount(memberID):
                sql = "SELECT * FROM fine WHERE memberID = %s"
                cursor.execute(sql, memberID)
                result = cursor.fetchone()
                return result[1]
            
            if memberHasFine(memberID):
                if int(payAmount) == rightAmount(memberID):
                    return popDetail(memberID, payAmount)
                else:
                    popError("Incorrect fine payment amount.")
            else:
                popError("Member has no fine")
            
        def backToFineMenu():
            fineMenuF()
            payment.destroy()
        
        payButton = Button(payment, text = "Pay Fine", command = tryPay)
        backButton = Button(payment, text = "Back to Fines Menu", command = backToFineMenu)

        # Placement of Labels and Buttons
        header.grid(row = 0, column=0, pady=50, columnspan=3)
        membIDLable.grid(row = 1, column = 0)
        payDateLabel.grid(row = 2, column = 0)
        payAmtLabel.grid(row = 3, column = 0)
        membID.grid(row = 1, column = 1)
        payDate.grid(row = 2, column = 1)
        payAmt.grid(row = 3, column = 1)
        payButton.grid(row = 4, column = 0)
        backButton.grid(row = 4, column = 1)

    #Buttons
    paymentButton = Button(fineMenu, text = "Fine Payment", command = fineMenuToPayment)
    fineToMainButton = Button(fineMenu, text = "Back to Main Menu", command = fineToMain)

    # Placement of Buttons
    paymentButton.grid(row = 0, column = 0)
    fineToMainButton.grid(row = 1, column = 0)

## 7 Reports Menu ##
def destroyReportMenu():
    reportMenu.destroy()

def reportMenuF():
    global reportMenu
    reportMenu = Toplevel()
    # Design iconbitmap, geometry
    reportMenu.title("Reports")
    reportMenu.geometry("1280x720")

    # Book Search Menu #
    def bookSearchF():
        global bookSearch
        bookSearch = Toplevel()
        # Design iconbitmap, geometry
        bookSearch.title("Book Search")
        bookSearch.geometry("1280x720")
        
        header = Label(bookSearch, text = "Search based on one of the categories below:", borderwidth=5, bg="lightblue", padx=350,fg="black", pady=20)
        titleLabel = Label(bookSearch, text = "Title")
        authorsLabel = Label(bookSearch, text = "Authors")
        isbnLabel = Label(bookSearch, text = "ISBN")
        publisherLabel = Label(bookSearch, text = "Publisher")
        pubYearLabel = Label(bookSearch, text = "Publication Year")

        title = Entry(bookSearch)
        authors = Entry(bookSearch)
        isbn = Entry(bookSearch)
        publisher = Entry(bookSearch)
        pubYear = Entry(bookSearch)
        
        def showResult():
            global table
            table = Toplevel()
            table.title("Book Search Results")
            table.geometry("1280x720")

            header = Label(table, text = "Book Search Results")
            header.grid(row = 0)

            ## Treeview
            columns = ("Accession Number","Title","Authors", "ISBN", "Publisher","Year")
            tree = ttk.Treeview(table, columns = columns, show = "headings")

            tree.heading("Accession Number",text='Accession Number',anchor=CENTER)
            tree.heading("Title",text="Title",anchor=CENTER)
            tree.heading("Authors",text="Authors",anchor=CENTER)
            tree.heading("ISBN",text="ISBN",anchor=CENTER)
            tree.heading("Publisher",text="Publisher",anchor=CENTER)
            tree.heading("Year",text="Year",anchor=CENTER)

            if title.get():
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo \
                        WHERE title LIKE %s"
                data = "%" + title.get() + "%" 
                cursor.execute(sql, data)
            elif authors.get():
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo \
                        WHERE author LIKE %s"
                data = "%" + authors.get() + "%" 
                cursor.execute(sql, data)
            elif isbn.get():
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo \
                        WHERE isbn = %s"
                data = isbn.get()
                cursor.execute(sql, data)
            elif publisher.get():
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo \
                        WHERE publisher like %s"
                data = "%" + publisher.get() +"%"
                cursor.execute(sql, data)
            elif pubYear.get():
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo \
                        WHERE pubDate = %s"
                data = pubYear.get()
                cursor.execute(sql, data)
            else:
                sql = "SELECT DISTINCT book.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                        FROM book INNER JOIN authors on book.accessionNo = authors.accessionNo"
                cursor.execute(sql)

            result = cursor.fetchall()
            
            i = 0
            if len(result) != 0:
                for row in result:
                    tree.insert(parent = '',index='end',iid=i,text=i+1,values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                    i+=1
            
            tree.grid(row=1)

            def back():
                table.destroy()

            backButton = Button(table, text = "Back To Search Function", command = back)
            backButton.grid(row = 2)

        def searchBackToReport():
            reportMenuF()
            bookSearch.destroy()
    
        searchButton = Button(bookSearch, text = "Search Book", command = showResult)
        backButton = Button(bookSearch, text = "Back to Reports Menu", command = searchBackToReport)

        # Placements of Labels and Buttons
        header.grid(row = 0, column=0, pady=50, columnspan=3)
        titleLabel.grid(row = 1, column = 0)
        authorsLabel.grid(row = 2, column = 0)
        isbnLabel.grid(row = 3, column = 0)
        publisherLabel.grid(row = 4, column = 0)
        pubYearLabel.grid(row = 5, column = 0) 
        title.grid(row = 1, column = 1) 
        authors.grid(row = 2, column = 1) 
        isbn.grid(row = 3, column = 1) 
        publisher.grid(row = 4, column = 1) 
        pubYear.grid(row = 5, column = 1) 
        searchButton.grid(row = 6, column = 0) 
        backButton.grid(row = 6, column = 1) 

    # Book on Loan #
    def bookLoanF():
        global bookLoan
        bookLoan = Toplevel()

        # Design iconbitmap, geometry
        bookLoan.title("Book on Loan Report")
        bookLoan.geometry("1280x720")

        header = Label(bookLoan, text = "Books on Loan Report")
        header.grid(row = 0)

        ## Treeview
        columns = ("Accession Number", "Title","Authors","ISBN", "Publisher","Year")
        tree = ttk.Treeview(bookLoan, columns = columns, show = "headings")

        tree.heading("Accession Number",text="Accession Number",anchor=CENTER)
        tree.heading("Title",text="Title",anchor=CENTER)
        tree.heading("Authors",text='Authors',anchor=CENTER)
        tree.heading("ISBN",text="ISBN",anchor=CENTER)
        tree.heading("Publisher",text='Publisher',anchor=CENTER)
        tree.heading("Year",text='Year',anchor=CENTER)

        sql = "SELECT loan.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
            FROM loan \
            INNER JOIN book ON loan.accessionNo = book.accessionNo \
            INNER JOIN authors ON loan.accessionNo = authors.accessionNo"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        i = 0
        if len(result) != 0:
            for row in result:
                tree.insert(parent = '',index='end',iid=i,text=i+1,values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                i+=1
        
        tree.grid(row=1)

        def backToReportMenu():
            reportMenuF()
            bookLoan.destroy()

        backButton = Button(bookLoan, text = "Back To Reports Menu", command = backToReportMenu)
        backButton.grid(row = 2)
    
    # Book on Reservation Report #
    def bookReservationF():
        global bookReservation
        bookReservation = Toplevel()

        # Design iconbitmap, geometry
        bookReservation.title("Book on Reservation Report")
        bookReservation.geometry("1280x720")

        header = Label(bookReservation, text = "Books on Reservation Report")
        header.grid(row=0)

        ## Treeview
        columns = ("Accession Number","Title","Membership ID", "Name")
        tree = ttk.Treeview(bookReservation, columns = columns, show = "headings")

        tree.heading("Accession Number",text='Accession Number',anchor=CENTER)
        tree.heading("Title",text="Title",anchor=CENTER)
        tree.heading("Membership ID",text="Membership ID",anchor=CENTER)
        tree.heading("Name",text="Name",anchor=CENTER)

        sql = "SELECT reservation.accessionNo, title, memberID, name FROM reservation \
                INNER JOIN book ON reservation.accessionNo = book.accessionNo \
                INNER JOIN member on reservation.memberID = member.ID"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        i = 0
        if len(result) != 0:
            for row in result:
                tree.insert(parent = '',index='end',iid=i,text=i+1,values = (row[0],row[1],row[2],row[3]))
                i+=1
        
        tree.grid(row=1)

        def backToReportMenu():
            reportMenuF()
            bookReservation.destroy()

        backButton = Button(bookReservation, text = "Back To Reports Menu", command = backToReportMenu)
        backButton.grid(row=2)
    
    # Members With Outstanding Fines #
    def memberFineF():
        global memberFine
        memberFine = Toplevel()

        # Design iconbitmap, geometry
        memberFine.title("Members With Outstanding Fines")
        memberFine.geometry("1280x720")

        header = Label(memberFine, text = "Books on Reservation Report")
        header.grid(row = 0)

        ## Treeview
        columns = ("Membership ID", "Name","Faculty","Phone Number", "Email Address")
        tree = ttk.Treeview(memberFine, columns = columns, show = "headings")

        tree.heading("Membership ID",text="Membership ID",anchor=CENTER)
        tree.heading("Name",text="Name",anchor=CENTER)
        tree.heading("Faculty",text='Faculty',anchor=CENTER)
        tree.heading("Phone Number",text="Phone Number",anchor=CENTER)
        tree.heading("Email Address",text='Email Address',anchor=CENTER)

        sql = "SELECT memberID, name, faculty, phoneNo, email FROM fine \
                INNER JOIN member ON fine.memberID = member.ID \
                WHERE amount > 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        i = 0
        if len(result) != 0:
            for row in result:
                tree.insert(parent = '',index='end',iid=i,text=i+1,values = (row[0],row[1],row[2],row[3],row[4]))
                i+=1
        
        tree.grid(row=1)

        def backToReportMenu():
            reportMenuF()
            memberFine.destroy()

        backButton = Button(memberFine, text = "Back To Reports Menu", command = backToReportMenu)
        backButton.grid(row = 2)

    # Books on Loan to Member
    def bkToMembF():
        global bkToMemb
        bkToMemb = Toplevel()
        # Design iconbitmap, geometry
        bkToMemb.title("Books on Loan to Member")
        bkToMemb.geometry("1280x720")

        header = Label(bkToMemb, text = "Books on Loan to Member")
        memberIDLabel = Label(bkToMemb, text = "Membership ID")
        memberID = Entry(bkToMemb)

        # slide 53
        def membBookLoanF():
            global membBookLoan
            membBookLoan = Toplevel()
            membBookLoan.title("Books on Loan to Member")
            membBookLoan.geometry("1280x720")

            header = Label(membBookLoan, text = "Books on Loan to Member")
            header.grid(row = 0)
             ## Treeview
            columns = ("Accession Number", "Title","Authors","ISBN", "Publisher","Year")
            tree = ttk.Treeview(membBookLoan, columns = columns, show = "headings")

            tree.heading("Accession Number",text="Accession Number",anchor=CENTER)
            tree.heading("Title",text="Title",anchor=CENTER)
            tree.heading("Authors",text='Authors',anchor=CENTER)
            tree.heading("ISBN",text="ISBN",anchor=CENTER)
            tree.heading("Publisher",text='Year',anchor=CENTER)

            sql = "SELECT loan.accessionNo, book.title, authors.author, book.isbn, book.publisher, book.pubDate \
                    FROM loan \
                    INNER JOIN book ON loan.accessionNo = book.accessionNo \
                    INNER JOIN authors ON loan.accessionNo = authors.accessionNo \
                    WHERE memberID = %s"
            data = memberID.get()
            cursor.execute(sql,data)
            result = cursor.fetchall()
            
            i = 0
            if len(result) != 0:
                for row in result:
                    tree.insert(parent = '',index='end',iid=i,text=i+1,values = (row[0],row[1],row[2],row[3],row[4],row[5]))
                    i+=1
            
            tree.grid(row=1)

            def backToReport():
                reportMenuF()
                membBookLoan.destroy()

            backButton = Button(membBookLoan, text = "Back to Reports Menu", command = backToReport)
            backButton.grid(row = 2)

        def showSearch():
            membBookLoanF()
            bkToMemb.destroy()

        def backToReport():
            reportMenuF()
            bkToMemb.destroy()

        searchButton = Button(bkToMemb, text = "Search Member", command = showSearch)
        backButton = Button(bkToMemb, text = "Back to Reports Menu", command = backToReport)

        # Placements of Labels and Button
        header.grid(row = 0)
        memberIDLabel.grid(row=1,column=0)
        memberID.grid(row=1, column=1)
        searchButton.grid(row=2,column=0)
        backButton.grid(row=2, column=1)


    # Functions
    def reportToBkSearch():
        bookSearchF()
        destroyReportMenu()

    def reportToBkLoan():
        bookLoanF()
        destroyReportMenu()

    def toBookOnReserve():
        bookReservationF()
        destroyReportMenu()

    def toMemberFine():
        memberFineF()
        destroyReportMenu()

    def toMemberBookLoan():
        bkToMembF()
        destroyReportMenu()

    def reportToMain():
        mainMenuF()
        destroyReportMenu()

    header = Label(reportMenu, text = "Select one of the Options below:", borderwidth=5, bg="lightblue", padx=350,fg="black", pady=20)
    bkSearchButton = Button(reportMenu, text = "Book Search", command = reportToBkSearch)
    bkOnLoanButton = Button(reportMenu, text = "Books on Loan", command = reportToBkLoan)
    bkOnResButton = Button(reportMenu, text = "Books on Reservation", command = toBookOnReserve)
    outFinesButton = Button(reportMenu, text = "Outstanding Fines", command = toMemberFine)
    bkToMembButton = Button(reportMenu, text = "Books on Loan to Member", command = toMemberBookLoan)
    backToMainButton = Button(reportMenu, text = "Back To Main Menu", command = reportToMain)

    # Placements of Buttons
    header.grid(row = 0)
    bkSearchButton.grid(row = 1)
    bkOnLoanButton.grid(row = 2)
    bkOnResButton.grid(row = 3)
    outFinesButton.grid(row = 4)
    bkToMembButton.grid(row = 5)
    backToMainButton.grid(row = 6)


mainMenuF()
mainloop()