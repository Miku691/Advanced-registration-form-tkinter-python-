from tkinter import *
from tkinter import messagebox as tmsg
import tempfile
import os
from tkinter import filedialog

root = Tk()

root.geometry("850x600")
root.title("EATM registration form")
root.wm_iconbitmap("img\\favicon.ico")

# ======== All Variables ========
studentFName = StringVar()
studentLName = StringVar()
studentEmail = StringVar()
emailSet = StringVar()
studentPhone = StringVar()
admission = StringVar(root)
regBack = StringVar()
gender = StringVar()
gender.set("male")
scBranch = StringVar()


scCollege = StringVar()
scMark = StringVar()
scAge = StringVar()
scAge.set("")
scDate = StringVar()
scMonth = StringVar()
scYear = StringVar()

collegeAddress = StringVar()
yourAddress = StringVar()


# ========== All Functiona======

        # =============== Submit Form =============
def submitForm():
    Name = studentFName.get()+" "+ studentLName.get()
    email = emailEntry.get()+emailSet.get()
    DOB = scDate.get()+"-"+scMonth.get()+"-"+scYear.get()
    

    if scCollege.get() == '' or scMark.get() == '' or scAge.get() == '' or collegeAddress.get() == '' or yourAddress.get() == '':
        tmsg.showerror("Error" , "All boxes have to be filled")

    elif scDate.get() == 'Date' or scMonth.get() == 'Month' or scYear.get() == 'Year':
        tmsg.showerror("Error" , "Choose Your Date Of Birth")

    else:
        tmsg.showinfo("Submit","Are sure to submit these data \n"+scCollege.get()+"\n"+scMark.get()+"\n"+collegeAddress.get()+"\n"+yourAddress.get()+"\n"+email+"\n"+DOB)

        # print(f"The name of the student is {Name}, {email} and {DOB} and {gender.get()} {scBranch.get()}")
        if admission.get() == 'B.Tech':
            if regBack.get() == 'Regular':
                with open('regularRecord.txt' , 'a') as f:
                    f.write(f"New Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n+2 Science College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n")
                    tmsg.showinfo("Success" , "Your Data for B.Tech Regular has been submitted successfully")
                    f.close()

            else:
                with open('lateralRecord.txt' , 'a') as f:
                    f.write(f"New Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \nDiploma College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal CGPA: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n")
                    tmsg.showinfo("Success" , "Your Data for B.Tech Lateral has been submitted successfully")
                    f.close()

        elif admission.get() == 'Diploma':
            with open('diplomaRecord.txt' , 'a') as f:
                    f.write(f"New Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n")
                    tmsg.showinfo("Success" , "Your Data for Diploma has been submitted successfully")
                    f.close()

        else:
            with open('scienceRecord.txt' , 'a') as f:
                    f.write(f"New Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \n \n")
            
                    tmsg.showinfo("Success" , "Your Data for +2 Science has been submitted successfully")
                    f.close()

        
            # ================== Reset Form =================

def resetForm():
    if scCollege.get() == '' and scMark.get() == '' and scAge.get() == '' and collegeAddress.get() == '' and yourAddress.get() == '':
        tmsg.showinfo("Info" , "Already empty! Please fill Data")
    else:
        if(tmsg.askokcancel("Warning" , "Are you sure to reset your data ?")):    
            scCollege.set('')     
            scMark.set('')
            scAge.set('')  
            collegeAddress.set('')
            yourAddress.set('')
            scDate.set('Date')
            scMonth.set('Month')
            scYear.set('Year')
            scBranch.set('Branch')


            # ====================== Print form ===================

def printForm():
    Name = studentFName.get()+" "+ studentLName.get()
    email = emailEntry.get()+emailSet.get()
    DOB = scDate.get()+"-"+scMonth.get()+"-"+scYear.get()
    if admission.get() == 'B.Tech':
        if regBack.get() == 'Regular':
            printData = f"B.Tech Regular Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n+2 Science College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
            fileName = tempfile.mktemp(".txt")
            open (fileName,"w").write(printData)
            os.startfile(fileName, "print")

        else:
            printData = f"B.Tech Lateral Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \nDiploma College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal CGPA: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
            fileName = tempfile.mktemp(".txt")
            open (fileName,"w").write(printData)
            os.startfile(fileName, "print")

    elif admission.get() == 'Diploma':
        printData = f"B.Tech Diploma Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
        fileName = tempfile.mktemp(".txt")
        open (fileName,"w").write(printData)
        os.startfile(fileName, "print")

    else:
        printData = f"B.Tech Science Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \n \n"
        fileName = tempfile.mktemp(".txt")
        open (fileName,"w").write(printData)
        os.startfile(fileName, "print")
        
            
                # ======================== Save form ===================

def saveForm():
    Name = studentFName.get()+" "+ studentLName.get()
    email = emailEntry.get()+emailSet.get()
    DOB = scDate.get()+"-"+scMonth.get()+"-"+scYear.get()

    if admission.get() == 'B.Tech':
        if regBack.get() == 'Regular':
            open_file = filedialog.asksaveasfile(mode='w' , defaultextension = ".txt")
            if open_file is None:
                return
            saveData = f"B.Tech Regular Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n+2 Science College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
            open_file.write(saveData)
            open_file.close()

        else:
            open_file = filedialog.asksaveasfile(mode='w' , defaultextension = ".txt")
            if open_file is None:
                return
            saveData = f"B.Tech Lateral Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \nDiploma College: {scCollege.get()} \nCollege Address: {collegeAddress.get()} \nTotal CGPA: {scMark.get()} \nStudent Age: {scAge.get()} \nDate Of Birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
            open_file.write(saveData)
            open_file.close()

    elif admission.get() == 'Diploma':
        open_file = filedialog.asksaveasfile(mode='w' , defaultextension = ".txt")
        if open_file is None:
            return
        saveData = f"B.Tech Diploma Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \nBranch: {scBranch.get()} \n \n"
        open_file.write(saveData)
        open_file.close()

    else:
        open_file = filedialog.asksaveasfile(mode='w' , defaultextension = ".txt")
        if open_file is None:
            return
        saveData = f"B.Tech Science Record \nStudetn name: {Name} \nmail id: {email} \nPhone No. : {studentPhone.get()} \nGender: {gender.get()} \n10th School: {scCollege.get()} \nSchool Address: {collegeAddress.get()} \nTotal mark: {scMark.get()} \nStudent Age: {scAge.get()} \nDate of birth: {DOB} \nYour Address: {yourAddress.get()} \n \n"
        open_file.write(saveData)
        open_file.close()


            # ============= B.Tech Regular Design ================

def btechReg():
    btechRegFrame = Frame(root, width = 750 , height = 350 )
    btechRegFrame.place(x = 40 , y = 290)

    scCollegeLb = Label(btechRegFrame,text = "+2 Science College:" , font = ("" , 15) , fg = "green")
    scCollegeLb.grid(row = 0 , column = 0 , padx = 15)
    scCollegeEntry = Entry(btechRegFrame , font = ("" , 13),textvariable = scCollege )
    scCollegeEntry.grid(row = 0, column = 1)
    
    scTextLb = Label(btechRegFrame ,text = "College Address:", font = ("" , 15), fg = "green")
    scTextLb.grid(row = 1 , column = 0 , padx = 15)
    scTextEntry = Entry(btechRegFrame , font = ("" , 15),textvariable = collegeAddress)
    scTextEntry.grid(row = 1, column = 1)
    
    scMarkLb = Label(btechRegFrame,text = "+2 Science Marks:" , font = ("" , 15), fg = "green")
    scMarkLb.grid(row = 2 , column = 0 , padx = 15)
    scMarkEntry = Entry(btechRegFrame , font = ("" , 13),textvariable = scMark )
    scMarkEntry.grid(row = 2, column = 1)

    scAgeLb = Label(btechRegFrame,text = "Student Age:" , font = ("" , 15), fg = "green")
    scAgeLb.grid(row = 3 , column = 0 , padx = 15)
    scAgeEntry = Entry(btechRegFrame , font = ("" , 13),textvariable = scAge )
    scAgeEntry.grid(row = 3, column = 1)

    scDOBLb = Label(btechRegFrame,text = "Date Of Birth:" , font = ("" , 15), fg = "green")
    scDOBLb.grid(row = 4 , column = 0 , padx = 15)

    scDateList = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30" ,"31" ]
    scDate.set("Date")
    scDateOp = OptionMenu(btechRegFrame , scDate , *scDateList)
    scDateOp.grid(row = 4 , column = 1 , padx = 8, pady = 10 )

    scMonthList = ["January" ,"February" ,"March" ,"April" ,"May" ,"June" ,"July" ,"August" ,"Septmber" ,"October" ,"November" ,"December" ]
    scMonth.set("Month")
    scMonthOp = OptionMenu(btechRegFrame , scMonth , *scMonthList)
    scMonthOp.grid(row = 4 , column = 2 ,padx = 8, pady = 10 )

    scYearList = ["1995" ,"1996" ,"1997" ,"1998" ,"1999" ,"2000" ,"2001" ,"2002" ,"2003" ,"2004" ,"2005" ,"2006" ,"2007" ,"2008" ,"2009" ,"2010"]
    scYear.set("Year")
    scYearOp = OptionMenu(btechRegFrame , scYear , *scYearList)
    scYearOp.grid(row = 4 , column = 3 , padx = 8, pady = 10 )

    stAddressLb = Label(btechRegFrame ,text = "Your Address:", font = ("" , 15), fg = "green")
    stAddressLb.grid(row = 5 , column = 0 , padx = 15)
    stAddressEntry = Entry(btechRegFrame , font = ("" , 15),textvariable = yourAddress)
    stAddressEntry.grid(row = 5, column = 1)
    
    scBranchLb = Label(btechRegFrame,text = "Choose Branch:" , font = ("" , 15), fg = "green")
    scBranchLb.grid(row = 5 , column = 2 , padx = 15)
    scBranchList = ["CSE" ,"ME" ,"Civil Engg." ,"EE" ,"EEE" ,"ECE" ,"CS"]
    scBranch.set("Branch")
    scBranchOp = OptionMenu(btechRegFrame , scBranch , *scBranchList)
    scBranchOp.grid(row = 5 , column = 3 , padx = 8, pady = 10 )

    allButton()
    

            # ============= B.Tech Lateral Design ================

def btechBack():
    btechBackFrame = Frame(root, width = 750 , height = 350 )
    btechBackFrame.place(x = 40 , y = 290)

    scCollegeLb = Label(btechBackFrame,text = "Diploma College:" , font = ("" , 15),fg = "red")
    scCollegeLb.grid(row = 0 , column = 0 , padx = 15)
    scCollegeEntry = Entry(btechBackFrame , font = ("" , 13),textvariable = scCollege )
    scCollegeEntry.grid(row = 0, column = 1)

    scTextLb = Label(btechBackFrame ,text = "College Address:", font = ("" , 15),fg = "red")
    scTextLb.grid(row = 1 , column = 0 , padx = 15)
    scTextEntry = Entry(btechBackFrame , font = ("" , 15), textvariable = collegeAddress )
    scTextEntry.grid(row = 1, column = 1)


    scMarkLb = Label(btechBackFrame,text = "Diploma CGPA:" , font = ("" , 15),fg = "red")
    scMarkLb.grid(row = 2 , column = 0 , padx = 15)
    scMarkEntry = Entry(btechBackFrame , font = ("" , 13),textvariable = scMark )
    scMarkEntry.grid(row = 2, column = 1)

    scAgeLb = Label(btechBackFrame,text = "Student Age:" , font = ("" , 15),fg = "red")
    scAgeLb.grid(row = 3 , column = 0 , padx = 15)
    scAgeEntry = Entry(btechBackFrame , font = ("" , 13),textvariable = scAge )
    scAgeEntry.grid(row = 3, column = 1)

    scDOBLb = Label(btechBackFrame,text = "Date Of Birth:" , font = ("" , 15),fg = "red")
    scDOBLb.grid(row = 4 , column = 0 , padx = 15)

    scDateList = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30" ,"31" ]
    scDateOp = OptionMenu(btechBackFrame , scDate , *scDateList)
    scDate.set("Date")
    scDateOp.grid(row = 4 , column = 1 , padx = 8, pady = 10 )

    scMonthList = ["January" ,"February" ,"March" ,"April" ,"May" ,"June" ,"July" ,"August" ,"Septmber" ,"October" ,"November" ,"December" ]
    scMonthOp = OptionMenu(btechBackFrame , scMonth , *scMonthList)
    scMonth.set("Month")
    scMonthOp.grid(row = 4 , column = 2 ,padx = 8, pady = 10 )

    scYearList = ["1995" ,"1996" ,"1997" ,"1998" ,"1999" ,"2000" ,"2001" ,"2002" ,"2003" ,"2004" ,"2005" ,"2006" ,"2007" ,"2008" ,"2009" ,"2010"]
    scYearOp = OptionMenu(btechBackFrame , scYear , *scYearList)
    scYear.set("Year")
    scYearOp.grid(row = 4 , column = 3 , padx = 8, pady = 10 )

    stAddressLb = Label(btechBackFrame ,text = "Your Address:", font = ("" , 15),fg = "red")
    stAddressLb.grid(row = 5 , column = 0 , padx = 15)
    stAddressEntry = Entry(btechBackFrame , font = ("" , 15) ,textvariable = yourAddress)
    stAddressEntry.grid(row = 5, column = 1)

    scBranchLb = Label(btechBackFrame,text = "Choose Branch:" , font = ("" , 15),fg = "red")
    scBranchLb.grid(row = 5 , column = 2 , padx = 15)
    scBranchList = ["CSE" ,"ME" ,"Civil Engg." ,"EE" ,"EEE" ,"ECE" ,"CS"]
    scBranch.set("Branch")
    scBranchOp = OptionMenu(btechBackFrame , scBranch , *scBranchList)
    scBranchOp.grid(row = 5 , column = 3 , padx = 8, pady = 10 )

    allButton()

            # ============= Choose Regular or Lateral ================
def btechRegFunc():
    regBackLb = Label(root,text = "choose admission type:" , font = ("" , 15))
    regBackLb.grid(row = 6 , column = 0 , padx = 8 , pady = 3)
    regBackList = ["Regular" , "Lateral"]
    regBack.set("choose")
    regBackOp = OptionMenu(root , regBack , *regBackList)
    regBackOp.grid(row = 6 , column = 2 , padx = 8, pady = 10 )

    Button(root,text = "next" , command = regOrBack, font = ("" , 12 , "bold")).grid(row = 6, column = 3, pady = 3)
    
def regOrBack():
    if regBack.get() == 'Regular':
        btechReg()
        
    elif regBack.get() == 'Lateral':
        btechBack()
        

            # ============= Doploma form Design ================
def diplomaFunc():
    diplomaFrame = Frame(root, width = 750 , height = 350)
    diplomaFrame.place(x = 40 , y = 290)

    scCollegeLb = Label(diplomaFrame,text = "10th School:" , font = ("" , 15),fg = "orange")
    scCollegeLb.grid(row = 0 , column = 0 , padx = 15)
    scCollegeEntry = Entry(diplomaFrame , font = ("" , 13),textvariable = scCollege )
    scCollegeEntry.grid(row = 0, column = 1)

    scTextLb = Label(diplomaFrame ,text = "School Address:", font = ("" , 15),fg = "orange")
    scTextLb.grid(row = 1 , column = 0 , padx = 15)
    scTextEntry = Entry(diplomaFrame , font = ("" , 15), textvariable = collegeAddress)
    scTextEntry.grid(row = 1, column = 1)


    scMarkLb = Label(diplomaFrame,text = "10th Marks:" , font = ("" , 15),fg = "orange")
    scMarkLb.grid(row = 2 , column = 0 , padx = 15)
    scMarkEntry = Entry(diplomaFrame , font = ("" , 13),textvariable = scMark )
    scMarkEntry.grid(row = 2, column = 1)

    scAgeLb = Label(diplomaFrame,text = "Student Age:" , font = ("" , 15),fg = "orange")
    scAgeLb.grid(row = 3 , column = 0 , padx = 15)
    scAgeEntry = Entry(diplomaFrame , font = ("" , 13),textvariable = scAge )
    scAgeEntry.grid(row = 3, column = 1)

    scDOBLb = Label(diplomaFrame,text = "Date Of Birth:" , font = ("" , 15),fg = "orange")
    scDOBLb.grid(row = 4 , column = 0 , padx = 15)

    scDateList = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30" ,"31" ]
    scDate.set("Date")
    scDateOp = OptionMenu(diplomaFrame , scDate , *scDateList)
    scDateOp.grid(row = 4 , column = 1 , padx = 8, pady = 10 )

    scMonthList = ["January" ,"February" ,"March" ,"April" ,"May" ,"June" ,"July" ,"August" ,"Septmber" ,"October" ,"November" ,"December" ]
    scMonth.set("Month")
    scMonthOp = OptionMenu(diplomaFrame , scMonth , *scMonthList)
    scMonthOp.grid(row = 4 , column = 2 ,padx = 8, pady = 10 )

    scYearList = ["1995" ,"1996" ,"1997" ,"1998" ,"1999" ,"2000" ,"2001" ,"2002" ,"2003" ,"2004" ,"2005" ,"2006" ,"2007" ,"2008" ,"2009" ,"2010"]
    scYear.set("Year")
    scYearOp = OptionMenu(diplomaFrame , scYear , *scYearList)
    scYearOp.grid(row = 4 , column = 3 , padx = 8, pady = 10 )

    stAddressLb = Label(diplomaFrame ,text = "Your Address:", font = ("" , 15),fg = "orange")
    stAddressLb.grid(row = 5 , column = 0 , padx = 15)
    stAddressEntry = Entry(diplomaFrame , font = ("" , 15), textvariable = yourAddress )
    stAddressEntry.grid(row = 5, column = 1)

    scBranchLb = Label(diplomaFrame,text = "Choose Branch:" , font = ("" , 15),fg = "orange")
    scBranchLb.grid(row = 5 , column = 2 , padx = 15)
    scBranchList = ["CSE" ,"ME" ,"Civil Engg." ,"EE" ,"EEE" ,"ECE" ,"CS"]
    scBranch.set("Branch")
    scBranchOp = OptionMenu(diplomaFrame , scBranch , *scBranchList)
    scBranchOp.grid(row = 5 , column = 3 , padx = 8, pady = 10 )

    allButton()

            # ============= +2 science form design ================

def scienceFunc():
    scienceFrame = Frame(root, width = 750 , height = 350 )
    scienceFrame.place(x = 40 , y = 290)

    scCollegeLb = Label(scienceFrame,text = "10th School:" , font = ("" , 15))
    scCollegeLb.grid(row = 0 , column = 0 , padx = 15)
    scCollegeEntry = Entry(scienceFrame , font = ("" , 13), textvariable = scCollege )
    scCollegeEntry.grid(row = 0, column = 1)

    scTextLb = Label(scienceFrame ,text = "School Address:", font = ("" , 15))
    scTextLb.grid(row = 1 , column = 0 , padx = 15)
    scTextEntry = Entry(scienceFrame , font = ("" , 15), textvariable = collegeAddress )
    scTextEntry.grid(row = 1, column = 1)


    scMarkLb = Label(scienceFrame,text = "10th Marks:" , font = ("" , 15))
    scMarkLb.grid(row = 2 , column = 0 , padx = 15)
    scMarkEntry = Entry(scienceFrame , font = ("" , 13),textvariable = scMark )
    scMarkEntry.grid(row = 2, column = 1)

    scAgeLb = Label(scienceFrame,text = "Student Age:" , font = ("" , 15))
    scAgeLb.grid(row = 3 , column = 0 , padx = 15)
    scAgeEntry = Entry(scienceFrame , font = ("" , 13),textvariable = scAge )
    scAgeEntry.grid(row = 3, column = 1)

    scDOBLb = Label(scienceFrame,text = "Date Of Birth:" , font = ("" , 15))
    scDOBLb.grid(row = 4 , column = 0 , padx = 15)

    scDateList = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30" ,"31" ]
    scDate.set("Date")
    scDateOp = OptionMenu(scienceFrame , scDate , *scDateList)
    scDateOp.grid(row = 4 , column = 1 , padx = 8, pady = 10 )

    scMonthList = ["January" ,"February" ,"March" ,"April" ,"May" ,"June" ,"July" ,"August" ,"Septmber" ,"October" ,"November" ,"December" ]
    scMonth.set("Month")
    scMonthOp = OptionMenu(scienceFrame , scMonth , *scMonthList)
    scMonthOp.grid(row = 4 , column = 2 ,padx = 8, pady = 10 )

    scYearList = ["1995" ,"1996" ,"1997" ,"1998" ,"1999" ,"2000" ,"2001" ,"2002" ,"2003" ,"2004" ,"2005" ,"2006" ,"2007" ,"2008" ,"2009" ,"2010"]
    scYear.set("Year")
    scYearOp = OptionMenu(scienceFrame , scYear , *scYearList)
    scYearOp.grid(row = 4 , column = 3 , padx = 8, pady = 10 )

    stAddressLb = Label(scienceFrame ,text = "Your Address:", font = ("" , 15), padx = 25)
    stAddressLb.grid(row = 5 , column = 0, padx = 15 )
    stAddressEntry = Entry(scienceFrame , font = ("" , 15) , textvariable = yourAddress)
    stAddressEntry.grid(row = 5, column = 1, padx = 15)

    allButton()

def loadMore():
    # print("loading details")
    admissionValue = admission.get()
    if studentFName.get() == '' or studentLName.get() == '' or studentPhone.get() == '' or studentEmail.get() == '':
        # print("Please filled all fields")
        tmsg.showerror("Error" , "All boxes have to be filled")

    elif len(studentPhone.get()) != 10:
        tmsg.showerror("Error","Phone No. should be 10 digits")
    else:
        if admissionValue == 'B.Tech':

            btechRegFunc()

        elif admissionValue == "Diploma":

            diplomaFunc()

        elif admissionValue == "+2 Science":

            scienceFunc()
    
            # ============= Above Design ================

Label(root,text = "                    Get Registrated to EATM" , font = ("", 17 , "bold"), fg = "black"  , padx = 50).grid(row = 0, columnspan = 8, pady = 10)
photo = PhotoImage(file = "img\\logo.png")
photoLb = Label(image = photo )
photoLb.grid(row = 0)

studentFLabel = Label(root,text = "First Name:" , font = ("" , 15))
studentFLabel.grid(row = 1 , column = 0 , padx = 8)
studentFEntry = Entry(root , font = ("" , 13) ,textvariable = studentFName )
studentFEntry.grid(row = 1, column = 2, padx = 10)

studentLLabel = Label(root,text = "Last Name:" , font = ("" , 15))
studentLLabel.grid(row = 1 , column = 3 , padx = 5)
studentLEntry = Entry(root , font = ("" , 13),textvariable = studentLName )
studentLEntry.grid(row = 1, column = 4)

emailLb = Label(root,text = "Enter email:" , font = ("" , 15))
emailLb.grid(row = 2 , column = 0 , padx = 8 , pady = 3)
emailEntry = Entry(root , font = ("" , 13)  ,textvariable = studentEmail )
emailEntry.grid(row = 2, column = 2, padx = 10)
emailList = ["@gmail.com" , "@email.com" , "@yahoo.com"]
emailSet.set("@gmail.com")
emailOp = OptionMenu(root , emailSet , *emailList)
emailOp.grid(row = 2 , column = 3 , pady = 10 )

phoneLb = Label(root,text = "Phone No.:" , font = ("" , 15))
phoneLb.grid(row = 3 , column = 0 , padx = 8 , pady = 3)
phoneEntry = Entry(root , font = ("" , 13)  ,textvariable = studentPhone)
phoneEntry.grid(row = 3, column = 2, padx = 10)

genderLb = Label(root,text = "Gender:" , font = ("" , 15))
genderLb.grid(row = 4 , column = 0 , padx = 8 , pady = 3)
genderRadio1 = Radiobutton(root , text = "male" , font = ("" , 15, )  ,variable = gender , value = "male")
genderRadio2 = Radiobutton(root , text = "female" , font = ("" , 15, )  ,variable = gender , value = "female")
genderRadio3 = Radiobutton(root , text = "other" , font = ("" , 15, )  ,variable = gender , value = "other")
genderRadio1.grid(row = 4, column = 2, padx = 10)
genderRadio2.grid(row = 4, column = 3, padx = 10)
genderRadio3.grid(row = 4, column = 4, padx = 10)

admissionLb = Label(root,text = "choose admission for:" , font = ("" , 15))
admissionLb.grid(row = 5 , column = 0 , padx = 8 , pady = 3)
admissionList = ["B.Tech" , "Diploma" , "+2 Science"]
admission.set("choose")
admissionOp = OptionMenu(root , admission , *admissionList)
admissionOp.grid(row = 5 , column = 2 , padx = 8 , pady = 3)
# print(admission.get)

Button(root,text = "next" , command = loadMore, font = ("" , 12 , "bold")).grid(row = 5, column = 3, pady = 3)

def allButton():
    allButtonsFrame = Frame(root, width = 800 , height = 50)
    allButtonsFrame.place(x = 0 , y = 530)

    submitButton = Button(allButtonsFrame , text = "Submit",font = ("" , 15 , "bold"), command = submitForm )
    submitButton.grid(row = 0 , column = 0 , padx = 60)

    resetButton = Button(allButtonsFrame , text = "ReSet",font = ("" , 15 , "bold"), command = resetForm )
    resetButton.grid(row = 0 , column = 1 , padx = 60)

    printButton = Button(allButtonsFrame , text = "Print",font = ("" , 15 , "bold"), command = printForm )
    printButton.grid(row = 0 , column = 2 , padx = 60)

    saveButton = Button(allButtonsFrame , text = "Save",font = ("" , 15 , "bold"), command = saveForm )
    saveButton.grid(row = 0 , column = 3 , padx = 60)

root.mainloop()