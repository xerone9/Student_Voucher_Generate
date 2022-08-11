from tkinter import *
import datetime
import urllib.request, json
import webbrowser
from Student_Voucher_Generate import print_voucher



def callback(url):
    webbrowser.open_new(url)


def print_fee_voucher():
    enter_receipt_no_Label.configure(fg="black")
    student_id_no_Label.configure(fg="black")
    student_name_Label.configure(fg="black")
    voucher_type_noLabel.configure(fg="black")
    due_date_noLabel.configure(fg="black")
    amount_noLabel.configure(fg="black")

    if len(enter_receipt_no_Text.get()) > 0 and len(student_id_no_Text.get()) > 0 and len(student_name_Text.get()) > 0 and len(amount_noText.get()) > 0 and len(voucher_type_noText.get()) > 0 and len(due_date_noText.get()) > 0:
        print_voucher(str(enter_receipt_no_Text.get()), str(student_id_no_Text.get()), str(student_name_Text.get()), str(amount_noText.get()), str(voucher_type_noText.get()), str(due_date_noText.get()))
        enter_receipt_no_Text.delete(0, "end")
        student_id_no_Text.delete(0, "end")
        student_name_Text.delete(0, "end")
        amount_noText.delete(0, "end")
        enter_receipt_no_Text.focus()
    elif len(enter_receipt_no_Text.get()) < 1:
        enter_receipt_no_Label.configure(fg="red")
    elif len(student_id_no_Text.get()) < 1:
        student_id_no_Label.configure(fg="red")
    elif len(student_name_Text.get()) < 1:
        student_name_Label.configure(fg="red")
    elif len(amount_noText.get()) < 1:
        amount_noLabel.configure(fg="red")
    elif len(voucher_type_noText.get()) < 1:
        voucher_type_noLabel.configure(fg="red")
    elif len(due_date_noText.get()) < 1:
        due_date_noLabel.configure(fg="red")




def get_student_name():
    student_name_Label.configure(fg="black")
    student_id_no_Label.configure(fg="black")
    student_name_Text.delete(0, "end")
    if len(student_id_no_Text.get()) > 0:
        id = str(student_id_no_Text.get())
        with urllib.request.urlopen("https://indus.rubick.org/accounts/get_data_api.php?stu_id='" + id + "'") as url:
            data = json.loads(url.read().decode())
            if len(data) > 0:
                get_name = str(data[0]).split(":")
                get_name2 = str(get_name[3]).split(",")
                name_is = str(get_name2[0]).replace("'", "")
                student_name_Text.insert(0, str(name_is[1:]))
            else:
                student_name_Label.configure(fg="red")
    else:
        student_id_no_Label.configure(fg="red")

root = Tk()
root.resizable(0,0)
root.iconbitmap('icon.ico')
root.title('Student Voucher Generate - V-1.0')
root.geometry("440x630")
root.configure(bg="white")

date_1 = datetime.datetime.now()
end_date = date_1 + datetime.timedelta(days=5)
due_date = str(end_date.strftime("%d,%b,%y")).replace(",","-")

img=PhotoImage(file='iu_logo.png')
label = Label(root, image=img)
label.configure(foreground="black")
label.configure(bg="white")
label.place(x=50, y=10)

generate_voucher_heading = Label(root, text='"Generate Student Voucher"', font=("Inter", 20, 'bold'), justify='center')
generate_voucher_heading.configure(bg="white")
generate_voucher_heading.place(x=30, y=180)

enter_receipt_no_Label = Label(root, text="Receipt No: ", font=("Inter", 16, 'bold'), justify='center')
enter_receipt_no_Label.configure(bg="white")
enter_receipt_no_Label.place(x=15, y=247)
enter_receipt_no_Text = Entry(root, width=10, textvariable=(StringVar(root, value='')), foreground='blue', font=("Arial", 16, 'bold'))
enter_receipt_no_Text.place(x=150, y=248)

student_id_no_Label = Label(root, text="Student ID: ", font=("Inter", 16, 'bold'), justify='center')
student_id_no_Label.configure(bg="white")
student_id_no_Label.place(x=15, y=287)
global student_id_no_Text
student_id_no_Text = Entry(root, width=10, textvariable=(StringVar(root, value='')), foreground='blue', font=("Arial", 16, 'bold'))
student_id_no_Text.place(x=150, y=288)

student_name_Label = Label(root, text="Std Name: ", font=("Inter", 16, 'bold'), justify='center')
student_name_Label.configure(bg="white")
student_name_Label.place(x=15, y=327)
student_name_Text = Entry(root, width=20, textvariable=(StringVar(root, value='')), foreground='blue', font=("Arial", 16, 'bold'))
student_name_Text.place(x=150, y=328)

voucher_type_noLabel = Label(root, text="Fee Type: ", font=("Inter", 16, 'bold'), justify='center')
voucher_type_noLabel.configure(bg="white")
voucher_type_noLabel.place(x=15, y=367)
voucher_type_noText = Entry(root, width=20, textvariable=(StringVar(root, value='Tuition Fee')), foreground='blue', font=("Arial", 16, 'bold'))
voucher_type_noText.place(x=150, y=368)

due_date_noLabel = Label(root, text="Due Date: ", font=("Inter", 16, 'bold'), justify='center')
due_date_noLabel.configure(bg="white")
due_date_noLabel.place(x=15, y=407)
due_date_noText = Entry(root, width=20, textvariable=(StringVar(root, value=str(due_date))), foreground='blue', font=("Arial", 16, 'bold'))
due_date_noText.place(x=150, y=408)

amount_noLabel = Label(root, text="Amount: ", font=("Inter", 16, 'bold'), justify='center')
amount_noLabel.configure(bg="white")
amount_noLabel.place(x=15, y=447)
amount_noText = Entry(root, width=20, textvariable=(StringVar(root, value='')), foreground='blue', font=("Arial", 16, 'bold'))
amount_noText.place(x=150, y=448)

get_student_name_Button = Button(root, text="Get Student Name", font=("Arial", 8, 'bold'), justify='center', command=get_student_name)
get_student_name_Button.configure(foreground="black")
get_student_name_Button.configure(bg="grey")
get_student_name_Button.place(x=290, y=288)

startButton = Button(root, text="Generate Voucher", font=("Arial", 15, 'bold'), justify='center', command=print_fee_voucher)
startButton.configure(foreground="black")
startButton.configure(bg="light green")
startButton.place(x=125, y=528)

footer = Label(root, text="softwares.rubick.org", font=(14), cursor="hand2")
footer.bind("<Button-1>", lambda e: callback("http://softwares.rubick.org"))
footer.configure(foreground="white")
footer.configure(bg="black")
footer.pack(side=BOTTOM)

root.mainloop()