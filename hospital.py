from tkinter import *
import messagebox
import mysql.connector as myconn
import random
from PIL import Image, ImageTk
from datetime import datetime, date, timedelta
from tkcalendar import DateEntry
from dateutil import parser


# ======================================================
def convert_date_format(date_str):
    parsed_date = parser.parse(date_str)
    formatted_date = parsed_date.strftime("%Y-%m-%d")
    return formatted_date


# ======================================================
root = Tk()
root.state("zoomed")
frame1 = Frame(root, bd=30, relief=SUNKEN)
root.title("Doctor appointment system")
Label(
    frame1,
    text="WELCOME TO DOCTOR APPOINTMENT SYSTEM",
    padx=10,
    bg="yellow",
    fg="red",
    font=("chiller 70 bold"),
    relief=GROOVE,
    bd=10,
).pack(side=TOP, fill=BOTH, expand=TRUE)
frame_choice = Frame(frame1, bd=5, relief=SUNKEN, bg="#88cffa")

# bg_image = PhotoImage(file="images/front page.png")

# bg_label = Label(frame_choice, image=bg_image)
# bg_label.place(x=0,y=0)

Label(
    frame_choice,
    text="SELECT WHAT TYPE OF USER YOU ARE",
    font=("bold", 20, "italic", "underline"),
    bg="#88cffa",
).pack(fill=X, expand=TRUE)
user = StringVar(value=NONE)
doctor = Radiobutton(
    frame_choice,
    text="DOCTOR",
    variable=user,
    value="DOCTOR",
    font=("bold", 18),
    bg="#88cffa",
    activebackground="#88cffa",
).pack(fill=X, expand=TRUE)
patient = Radiobutton(
    frame_choice,
    text="PATIENT",
    variable=user,
    value="PATIENT",
    font=("bold", 18),
    bg="#88cffa",
    activebackground="#88cffa",
).pack(fill=X, expand=TRUE)
frame_choice.pack(fill=BOTH, expand=TRUE)
frame1.pack(fill=BOTH, expand=TRUE)


# ================================================================================================
def reset_tables():
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()

    query = "SELECT table_name FROM daily_reset_table"
    cursor.execute(query)
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]

        query = f"SELECT last_reset_date FROM daily_reset_table WHERE table_name = '{table_name}'"
        cursor.execute(query)
        last_reset_date = cursor.fetchone()[0]

        current_date = date.today()

        if current_date > last_reset_date:
            query = f"UPDATE {table_name} SET status=NULL,app_date='{current_date}'"
            cursor.execute(query)
            query = f"UPDATE daily_reset_table SET last_reset_date = '{current_date}' WHERE table_name = '{table_name}'"
            cursor.execute(query)
            mydb.commit()
    cursor.close()
    mydb.close()


reset_tables()


# =============================================================================
def btn_click():
    if user.get() == "PATIENT":
        frame1.pack_forget()
        user_patient()
    elif user.get() == "DOCTOR":
        frame1.pack_forget()
        user_doctor()
    else:
        messagebox.showerror("Error!", "Please Select User Type")


# =============================================================================
def user_doctor():
    global frame_doctor
    frame_doctor = Frame(root, bd=30, relief=SUNKEN, bg="#05f283")

    def show_pass():
        if e2.cget("show") == "*":
            e2.config(show="")
            chk.config(text="Hide password")
        elif e2.cget("show") == "":
            e2.config(show="*")
            chk.config(text="Show password")

    def back():
        frame_doctor.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    def home():
        frame_doctor.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    global e1, e2
    Label(
        frame_doctor,
        text="DOCTOR LOGIN",
        font=("chiller 80 bold"),
        padx=10,
        pady=10,
        bg="yellow",
        fg="red",
        bd=20,
        relief=SUNKEN,
    ).pack(fill=BOTH, expand=TRUE)
    Button(
        frame_doctor, text="HOME", bg="black", fg="white", command=home, width=15
    ).pack(side=LEFT)
    Button(
        frame_doctor, text="BACK", bg="black", fg="white", command=back, width=15
    ).pack(side=RIGHT)
    Label(frame_doctor, text="USERNAME", font=("italic 24 bold"), bg="#05f283").pack(
        fill=BOTH, expand=TRUE
    )
    e1 = Entry(frame_doctor, width=30, borderwidth=5)
    e1.pack()
    Label(frame_doctor, text="PASSWORD", font=("italic 24 bold"), bg="#05f283").pack(
        fill=BOTH, expand=TRUE
    )
    e2 = Entry(frame_doctor, show="*", width=30, borderwidth=5)
    e2.pack()
    chk = Checkbutton(
        frame_doctor,
        text="Show password",
        command=show_pass,
        bg="#05f283",
        activebackground="#05f283",
    )
    chk.pack(fill=BOTH, expand=TRUE)
    Button(
        frame_doctor,
        text="LOGIN",
        bg="black",
        fg="white",
        command=doctor_login,
        width=20,
    ).pack()
    frame_doctor.pack(fill=BOTH, expand=TRUE)


# ===========================================================================================
def doctor_login():
    dc_user = e1.get()
    dc_passw = e2.get()
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = (
        "select * from doctor where id='"
        + dc_user
        + "' and password='"
        + dc_passw
        + "'"
    )
    cursor.execute(query)
    cur = cursor.fetchall()
    n = len(cur)
    if n > 0:
        messagebox.showinfo("Success!", "Login Successful,Press OK to proceed")
        doctor_portal()
    else:
        messagebox.showwarning("Warning!", "Wrong Username or Password")


# ====================================================================================
def doctor_portal():
    global frame_doctor_portal, frame_prev_appointment, frame_button_doctor_portal
    frame_doctor.pack_forget()
    frame_prev_appointment = Frame(root)
    frame_doctor_portal = Frame(root, relief="sunken", bd=5, bg="#c676cf")
    frame_button_doctor_portal = Frame(root, bd=5, relief=SUNKEN, bg="#68f205")

    root.config(bg="#cf7696")

    def home():
        frame_doctor_portal.pack_forget()
        frame_button_doctor_portal.pack_forget()
        frame_prev_appointment.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    def back():
        frame_doctor_portal.pack_forget()
        frame_prev_appointment.pack_forget()
        frame_button_doctor_portal.pack_forget()
        frame_doctor.pack(fill=BOTH, expand=TRUE)

    def show_appointment():
        global status, lbl_status
        frame_prev_appointment.pack_forget()
        mydb = myconn.connect(
            host="localhost", username="root", password="Garg@231", db="hospital"
        )
        cursor = mydb.cursor()
        query = (
            "select p_id,p_name,payment_status,app_date,app_time,app_id from appointments where doc_id='"
            + e1.get()
            + "' and status is NULL and app_date>=CURRENT_DATE"
        )
        cursor.execute(query)
        cur = cursor.fetchall()
        num = 3
        status = StringVar(value=NONE)
        if len(cur) == 0:
            messagebox.showinfo("Sorry", "No appointments Left for approval")
            frame_doctor_portal.pack_forget()
        else:
            Label(
                frame_doctor_portal,
                text="Patient ID",
                relief="groove",
                width=30,
                height=5,
                bg="#c676cf",
            ).grid(row=2, column=0)
            Label(
                frame_doctor_portal,
                text="Name",
                relief="groove",
                width=30,
                height=5,
                bg="#c676cf",
            ).grid(row=2, column=1)
            Label(
                frame_doctor_portal,
                text="Payment Status",
                relief="groove",
                width=30,
                height=5,
                bg="#c676cf",
            ).grid(row=2, column=2)
            Label(
                frame_doctor_portal,
                text="Date",
                relief="groove",
                width=30,
                height=5,
                bg="#c676cf",
            ).grid(row=2, column=3)
            Label(
                frame_doctor_portal,
                text="Time",
                relief="groove",
                width=30,
                height=5,
                bg="#c676cf",
            ).grid(row=2, column=4)
            for i in cur:
                Label(
                    frame_doctor_portal,
                    text=i[0],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#c676cf",
                ).grid(row=num, column=0)
                Label(
                    frame_doctor_portal,
                    text=i[1],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#c676cf",
                ).grid(row=num, column=1)
                if i[2] != "YES":
                    lbl_status = Label(
                        frame_doctor_portal,
                        text="PENDING",
                        relief="groove",
                        width=30,
                        height=5,
                        bg="#c676cf",
                    ).grid(row=num, column=2)
                else:
                    lbl_status = Label(
                        frame_doctor_portal,
                        text=i[2],
                        relief="groove",
                        width=30,
                        height=5,
                        bg="#c676cf",
                    ).grid(row=num, column=2)
                Label(
                    frame_doctor_portal,
                    text=i[3],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#c676cf",
                ).grid(row=num, column=3)
                Label(
                    frame_doctor_portal,
                    text=i[4],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#c676cf",
                ).grid(row=num, column=4)
                Radiobutton(
                    frame_doctor_portal,
                    value=i[5],
                    variable=status,
                    relief="groove",
                    height=5,
                    bg="#c676cf",
                ).grid(row=num, column=5)
                num += 1
            Button(
                frame_doctor_portal,
                text="Approve",
                bg="black",
                fg="white",
                command=approve,
            ).grid(row=num, column=2)
        frame_doctor_portal.pack()

    Button(
        frame_button_doctor_portal, text="HOME", command=home, width=20, bg="#b3f584"
    ).grid(row=0, column=0)
    Button(
        frame_button_doctor_portal,
        text="SHOW APPOINTMENTS",
        command=show_appointment,
        width=20,
        bg="#b3f584",
    ).grid(row=1, column=0)
    Button(
        frame_button_doctor_portal,
        text="PREVIOUS APPOINTMENTS",
        command=show_prev_appointment,
        bg="#b3f584",
        width=20,
    ).grid(row=2, column=0)
    Button(
        frame_button_doctor_portal, text="BACK", command=back, width=20, bg="#b3f584"
    ).grid(row=3, column=0)
    frame_button_doctor_portal.pack(side=LEFT, fill=Y)


# ======================================================================================
def show_prev_appointment():
    frame_doctor_portal.pack_forget()
    frame_prev_appointment.config(relief=SUNKEN, bd=5, bg="#86fa43")
    root.config(bg="#235904")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = (
        f"select p_id,p_name,app_date,app_time,app_id from appointments where doc_id='"
        + e1.get()
        + "' and app_date<CURRENT_DATE"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    canvas = Canvas(frame_prev_appointment)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame_prev_appointment, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    row_frame1 = Frame(inner_frame)
    row_frame1.pack()
    Label(
        row_frame1, text="Patient ID", relief="groove", width=30, height=5, bg="#86fa43"
    ).pack(side=LEFT)
    Label(
        row_frame1, text="Name", relief="groove", width=30, height=5, bg="#86fa43"
    ).pack(side=LEFT)
    Label(
        row_frame1, text="Date", relief="groove", width=30, height=5, bg="#86fa43"
    ).pack(side=LEFT)
    Label(
        row_frame1, text="Time", relief="groove", width=30, height=5, bg="#86fa43"
    ).pack(side=LEFT)

    for i in data:
        row_frame = Frame(inner_frame)
        row_frame.pack()

        Label(
            row_frame, text=i[0], relief="groove", width=30, height=5, bg="#86fa43"
        ).pack(side=LEFT)
        Label(
            row_frame, text=i[1], relief="groove", width=30, height=5, bg="#86fa43"
        ).pack(side=LEFT)
        Label(
            row_frame, text=i[2], relief="groove", width=30, height=5, bg="#86fa43"
        ).pack(side=LEFT)
        Label(
            row_frame, text=i[3], relief="groove", width=30, height=5, bg="#86fa43"
        ).pack(side=LEFT)

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.config(height=700, width=860)

    mydb.commit()
    frame_prev_appointment.pack()


# ======================================================================================
def approve():
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"update appointments set status='APPROVED' where app_id={status.get()} "
    cursor.execute(query)
    mydb.commit()
    messagebox.showinfo("Success", "Appointment approved successfully")
    frame_doctor_portal.pack_forget()
    lbl_status.config(text="APPROVED")


# ========================================================================================
def user_patient():
    global frame_patient
    frame_patient = Frame(root, bd=30, relief=SUNKEN, bg="#0597f2")

    def show_pass():
        if e4.cget("show") == "*":
            e4.config(show="")
            chk.config(text="Hide password")
        elif e4.cget("show") == "":
            e4.config(show="*")
            chk.config(text="Show password")

    def back():
        frame_patient.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    def home():
        frame_patient.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    global e3, e4

    Label(
        frame_patient,
        text="PATIENT LOGIN",
        font=("chiller 80 bold"),
        padx=10,
        pady=10,
        bg="yellow",
        fg="red",
        relief=SUNKEN,
        bd=10,
    ).pack(fill=BOTH, expand=TRUE)

    Button(
        frame_patient, text="HOME", bg="black", fg="white", command=home, width=15
    ).pack(side=LEFT)
    Button(
        frame_patient, text="BACK", bg="black", fg="white", command=back, width=15
    ).pack(side=RIGHT)
    Label(frame_patient, text="USERNAME", font=("italic 24 bold"), bg="#0597f2").pack(
        fill=BOTH, expand=TRUE
    )
    e3 = Entry(frame_patient, width=30, borderwidth=5)
    e3.pack()
    Label(frame_patient, text="PASSWORD", font=("italic 24 bold"), bg="#0597f2").pack(
        fill=BOTH, expand=TRUE
    )
    e4 = Entry(frame_patient, show="*", width=30, borderwidth=5)
    e4.pack()
    chk = Checkbutton(
        frame_patient,
        text="Show password",
        command=show_pass,
        bg="#0597f2",
        activebackground="#0597f2",
    )
    chk.pack(fill=BOTH, expand=TRUE)
    Button(
        frame_patient,
        text="LOGIN",
        bg="black",
        fg="white",
        command=patient_login,
        width=20,
    ).pack()
    Label(frame_patient, text="Don't Have a Account?", bg="#0597f2").pack(
        pady=10, side=TOP
    )
    Button(
        frame_patient, text="SIGNUP", fg="black", command=patient_signup, width=20
    ).pack(pady=10, side=TOP)
    frame_patient.pack(fill=BOTH, expand=TRUE)


# ========================================================================================
def patient_login():
    patient_id = e3.get()
    patient_pass = e4.get()
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = (
        "select * from patients where userid='"
        + patient_id
        + "' and password='"
        + patient_pass
        + "'"
    )
    cursor.execute(query)
    cur = cursor.fetchall()
    n = len(cur)
    if n > 0:
        messagebox.showinfo("Success!", "Login Successful,Press OK to proceed")
        patient_portal()
    else:
        messagebox.showwarning("Warning!", "Wrong Username or Password")


# ========================================================================================
def patient_signup():
    global e5, e6, e7, gender, e8, frame_patient_signup, frame_details
    frame_patient.pack_forget()
    frame_patient_signup = Frame(root, bd=20, relief=SUNKEN, bg="#cdb4ed")
    frame_details = Frame(frame_patient_signup, bd=20, relief=SUNKEN, bg="#b603fc")

    def back():
        frame_patient_signup.pack_forget()
        frame_patient.pack(fill=BOTH, expand=TRUE)

    def home():
        frame_patient_signup.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    Label(
        frame_patient_signup,
        text="PATIENT SIGNUP",
        font=("chiller 80 bold"),
        padx=10,
        pady=10,
        bg="yellow",
        fg="red",
        relief=SUNKEN,
        bd=10,
    ).pack(fill=BOTH, expand=TRUE)
    Button(
        frame_patient_signup, text="HOME", bg="black", fg="white", command=home
    ).pack(side=LEFT)
    Button(
        frame_patient_signup, text="BACK", bg="black", fg="white", command=back
    ).pack(side=RIGHT)
    Label(frame_details, text="Name", bg="#b603fc").grid(row=0, column=0, pady=20)
    e5 = Entry(frame_details)
    e5.grid(row=0, column=1, pady=10)
    Label(frame_details, text="Age", bg="#b603fc").grid(row=1, column=0, pady=10)
    e6 = Entry(frame_details)
    e6.grid(row=1, column=1, pady=10)
    Label(frame_details, text="Gender", bg="#b603fc").grid(row=2, column=0, pady=10)
    gender = StringVar(value=NONE)
    Radiobutton(
        frame_details,
        text="MALE",
        variable=gender,
        value="M",
        bg="#b603fc",
        activebackground="#b603fc",
    ).grid(row=2, column=1, pady=10)
    Radiobutton(
        frame_details,
        text="FEMALE",
        variable=gender,
        value="F",
        bg="#b603fc",
        activebackground="#b603fc",
    ).grid(row=2, column=2, pady=10)
    Label(frame_details, text="Contact", bg="#b603fc").grid(row=3, column=0, pady=10)
    e7 = Entry(frame_details)
    e7.grid(row=3, column=1, pady=10)
    Label(frame_details, text="Password", bg="#b603fc").grid(
        row=4, column=0, padx=10, pady=10
    )
    e8 = Entry(frame_details)
    e8.grid(row=4, column=1, pady=10)
    Button(
        frame_details, text="Register", bg="black", fg="white", command=patient_register
    ).grid(row=5, column=1, padx=10, pady=10)
    frame_details.pack(pady=150)
    frame_patient_signup.pack(fill=BOTH, expand=TRUE, anchor=CENTER)


# ========================================================================================
def patient_register():
    p_name = e5.get()
    p_age = e6.get()
    p_gender = gender.get()
    p_contact = e7.get()
    p_password = e8.get()
    if p_name == "":
        messagebox.showwarning("Warning!", "Please enter your name")
    elif p_age == "":
        messagebox.showwarning("Warning!", "Please enter your age")
    elif p_gender == NONE:
        messagebox.showwarning("Warning!", "Please select your gender")
    elif p_contact == "":
        messagebox.showwarning("Warning!", "Please enter your Contact no.")
    elif p_password == "":
        messagebox.showwarning("Warning!", "Please select your password")
    else:
        mydb = myconn.connect(
            host="localhost", username="root", password="Garg@231", db="hospital"
        )
        cursor = mydb.cursor()
        id = str(random.randint(10000, 99999))

        query = "INSERT INTO patients (name, age, gender, contact,password,userid) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (p_name, p_age, p_gender, p_contact, p_password, id)

        cursor.execute(query, values)
        messagebox.showinfo(
            "Success", "Patient registered successfully! Your userid is '" + id + "'"
        )
        mydb.commit()


# ========================================================================================
# ========================================================================================
def patient_portal():
    frame_patient.pack_forget()
    root.config(bg="#f2053c")
    global frame_patient_portal, frame_check_status, frame_app_history, frame_reschedule, frame_reschedule_time, frame_cancel_appointment, frame_appointment, btn_patient_frame, frame_generate_bill, frame_payment
    btn_patient_frame = Frame(root, bd=6, relief=SUNKEN, bg="#05314d")
    frame_patient_portal = Frame(root, bg="#848a12")
    frame_check_status = Frame(root)
    frame_app_history = Frame(root)
    frame_reschedule = Frame(root)
    frame_generate_bill = Frame(root)
    frame_payment = Frame(root)
    frame_reschedule_time = Frame(root)
    frame_cancel_appointment = Frame(root)
    frame_appointment = Frame(root, bg="#fab996")
    frame_patient_inner_portal = Frame(
        frame_patient_portal, borderwidth=5, relief=SUNKEN, bg="#f3ff05"
    )

    def home():
        frame_patient_portal.pack_forget()
        frame_check_status.pack_forget()
        frame_app_history.pack_forget()
        frame_reschedule_time.pack_forget()
        frame_cancel_appointment.pack_forget()
        frame_appointment.pack_forget()
        frame_payment.pack_forget()
        frame_generate_bill.pack_forget()
        frame_reschedule.pack_forget()
        btn_patient_frame.pack_forget()
        frame1.pack(fill=BOTH, expand=TRUE)

    def back():
        frame_patient_portal.pack_forget()
        frame_check_status.pack_forget()
        frame_appointment.pack_forget()
        frame_generate_bill.pack_forget()
        frame_payment.pack_forget()
        frame_cancel_appointment.pack_forget()
        frame_reschedule.pack_forget()
        frame_reschedule_time.pack_forget()
        frame_app_history.pack_forget()
        btn_patient_frame.pack_forget()
        frame_patient.pack(fill=BOTH, expand=TRUE)

    def show_doctors():
        global doc_name
        frame_check_status.pack_forget()
        frame_generate_bill.pack_forget()
        frame_payment.pack_forget()
        frame_cancel_appointment.pack_forget()
        frame_reschedule.pack_forget()
        frame_patient_portal.pack_forget()
        frame_app_history.pack_forget()
        mydb = myconn.connect(
            host="localhost", username="root", password="Garg@231", db="hospital"
        )
        cursor = mydb.cursor()
        query = "select name,specialist,t_name from doctor"
        cursor.execute(query)
        cur = cursor.fetchall()
        num = 3
        doc_name = StringVar(value=NONE)
        Label(
            frame_patient_inner_portal,
            text="SELECT DOCTOR FROM BELOW",
            bg="#f3ff05",
            font=(18),
        ).grid(row=1, column=0, columnspan=3)
        Label(
            frame_patient_inner_portal,
            text="Name",
            relief="groove",
            width=50,
            bg="#f3ff05",
            height=5,
        ).grid(row=2, column=0)
        Label(
            frame_patient_inner_portal,
            text="Speciality",
            relief="groove",
            width=50,
            bg="#f3ff05",
            height=5,
        ).grid(row=2, column=1)
        for i in cur:
            Label(
                frame_patient_inner_portal,
                text=i[0],
                relief="groove",
                width=50,
                bg="#f3ff05",
                height=5,
            ).grid(row=num, column=0)
            Label(
                frame_patient_inner_portal,
                text=i[1],
                relief="groove",
                width=50,
                bg="#f3ff05",
                height=5,
            ).grid(row=num, column=1)
            Radiobutton(
                frame_patient_inner_portal,
                value=i[0],
                variable=doc_name,
                relief="groove",
                bg="#f3ff05",
                height=5,
            ).grid(row=num, column=2)
            num += 1
        Button(
            frame_patient_inner_portal,
            text="Proceed",
            bg="black",
            fg="white",
            command=appointment,
        ).grid(row=num, column=0, columnspan=2)
        frame_patient_inner_portal.pack()
        frame_patient_portal.pack(fill=BOTH, expand=TRUE)

    # -------------------------------------------------------------------------------#
    Button(btn_patient_frame, text="HOME", width=30, command=home, bg="#f0d8de").grid(
        row=0, column=0
    )
    Button(
        btn_patient_frame,
        text="BOOK APPOINTMENT",
        width=30,
        command=show_doctors,
        bg="#f0d8de",
    ).grid(row=1, column=0)
    Button(
        btn_patient_frame,
        text="RESCHEDULE APPOINTMENT",
        width=30,
        command=reschedule_appointment,
        bg="#f0d8de",
    ).grid(row=2, column=0)
    Button(
        btn_patient_frame,
        text="CANCEL APPOINTMENT",
        width=30,
        command=cancel_appointment,
        bg="#f0d8de",
    ).grid(row=3, column=0)
    Button(
        btn_patient_frame,
        text="CHECK APPOINTMENT STATUS",
        width=30,
        command=check_status,
        bg="#f0d8de",
    ).grid(row=4, column=0)
    Button(
        btn_patient_frame,
        text="APPOINTMENT HISTORY",
        width=30,
        command=app_history,
        bg="#f0d8de",
    ).grid(row=5, column=0)
    Button(btn_patient_frame, text="BACK", width=30, command=back, bg="#f0d8de").grid(
        row=6, column=0
    )
    btn_patient_frame.pack(side=LEFT, fill=Y)
    # --------------------------------------------------------------------------------#


# ========================================================================================
def check_status():
    frame_patient_portal.pack_forget()
    frame_cancel_appointment.pack_forget()
    frame_reschedule_time.pack_forget()
    frame_appointment.pack_forget()
    frame_app_history.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_reschedule.pack_forget()

    root.config(bg="#014525")
    frame_check_status.config(relief="sunken", bd=5, bg="#03ff89")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"select doctor_name,app_date,app_time,status from appointments where p_id='{e3.get()}' and app_date>=CURRENT_DATE"
    cursor.execute(query)
    cur = cursor.fetchall()
    num = 3
    if len(cur) == 0:
        messagebox.showinfo("Sorry", "No appointments to be shown")
    else:
        Label(
            frame_check_status,
            text="Doctor Name",
            relief="groove",
            width=30,
            height=5,
            bg="#03ff89",
        ).grid(row=2, column=0)
        Label(
            frame_check_status,
            text="Appointment Date",
            relief="groove",
            width=30,
            height=5,
            bg="#03ff89",
        ).grid(row=2, column=1)
        Label(
            frame_check_status,
            text="Appointment Time",
            relief="groove",
            width=30,
            height=5,
            bg="#03ff89",
        ).grid(row=2, column=2)
        Label(
            frame_check_status,
            text="Approval Status",
            relief="groove",
            width=30,
            height=5,
            bg="#03ff89",
        ).grid(row=2, column=3)
        for i in cur:
            Label(
                frame_check_status,
                text=i[0],
                relief="groove",
                width=30,
                height=5,
                bg="#03ff89",
            ).grid(row=num, column=0)
            Label(
                frame_check_status,
                text=i[1],
                relief="groove",
                width=30,
                height=5,
                bg="#03ff89",
            ).grid(row=num, column=1)
            Label(
                frame_check_status,
                text=i[2],
                relief="groove",
                width=30,
                height=5,
                bg="#03ff89",
            ).grid(row=num, column=2)
            if i[3] == "APPROVED":
                Label(
                    frame_check_status,
                    text=i[3],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#03ff89",
                ).grid(row=num, column=3)
            else:
                Label(
                    frame_check_status,
                    text="PENDING",
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#03ff89",
                ).grid(row=num, column=3)
            num += 1
    frame_check_status.pack()


# ========================================================================================
def reschedule_appointment():
    global app_id, new_date
    frame_patient_portal.pack_forget()
    frame_cancel_appointment.pack_forget()
    frame_appointment.pack_forget()
    frame_app_history.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_check_status.pack_forget()
    frame_reschedule_time.pack_forget()

    frame_reschedule.config(bg="#749ddb", relief=SUNKEN, bd=5)
    root.config(bg="#08439c")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"select doctor_name,app_date,app_time,status,app_id from appointments where p_id='{e3.get()}' and app_date>=CURRENT_DATE"
    cursor.execute(query)
    cur = cursor.fetchall()
    num = 3
    app_id = StringVar(value=NONE)
    if len(cur) == 0:
        messagebox.showinfo("Sorry", "No appointments to be rescheduled")
    else:
        Label(
            frame_reschedule,
            text="SELECT APPOINTMENT TO BE RESCHEDULED",
            font=(18),
            bg="#749ddb",
        ).grid(row=1, column=0, columnspan=4)
        Label(
            frame_reschedule,
            text="Doctor Name",
            relief="groove",
            width=30,
            height=5,
            bg="#749ddb",
        ).grid(row=2, column=0)
        Label(
            frame_reschedule,
            text="Appointment Date",
            relief="groove",
            width=30,
            height=5,
            bg="#749ddb",
        ).grid(row=2, column=1)
        Label(
            frame_reschedule,
            text="Appointment Time",
            relief="groove",
            width=30,
            height=5,
            bg="#749ddb",
        ).grid(row=2, column=2)
        Label(
            frame_reschedule,
            text="Approval Status",
            relief="groove",
            width=30,
            height=5,
            bg="#749ddb",
        ).grid(row=2, column=3)
        for i in cur:
            Label(
                frame_reschedule,
                text=i[0],
                relief="groove",
                width=30,
                height=5,
                bg="#749ddb",
            ).grid(row=num, column=0)
            Label(
                frame_reschedule,
                text=i[1],
                relief="groove",
                width=30,
                height=5,
                bg="#749ddb",
            ).grid(row=num, column=1)
            Label(
                frame_reschedule,
                text=i[2],
                relief="groove",
                width=30,
                height=5,
                bg="#749ddb",
            ).grid(row=num, column=2)
            if i[3] == "APPROVED":
                Label(
                    frame_reschedule,
                    text=i[3],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#749ddb",
                ).grid(row=num, column=3)
            else:
                Label(
                    frame_reschedule,
                    text="PENDING",
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#749ddb",
                ).grid(row=num, column=3)
            Radiobutton(
                frame_reschedule, value=i[4], variable=app_id, height=5, bg="#749ddb"
            ).grid(row=num, column=4)
            num += 1
        Button(frame_reschedule, text="NEXT", bg="yellow", command=reschedule).grid(
            row=num, column=1
        )
    frame_reschedule.pack()


# ========================================================================================
def select():
    global new_date
    new_date = cal1.get_date()
    if new_date < date.today():
        messagebox.showwarning("Warning!", "Please choose a valid Date")


def reschedule():
    global new_date, cal1
    frame_appointment.pack_forget()
    frame_cancel_appointment.pack_forget()
    frame_patient_portal.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_check_status.pack_forget()
    frame_app_history.pack_forget()
    frame_reschedule.pack_forget()

    root.config(bg="#0597f2")
    frame_reschedule_time.config(relief="sunken", bd=5, bg="#aed3eb")
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    cursor2 = mydb.cursor()
    cursor3 = mydb.cursor()
    query2 = "select doctor_name from appointments where app_id='" + app_id.get() + "'"
    cursor2.execute(query2)
    cur2 = cursor2.fetchall()
    for i in cur2:
        doctor_name = i[0]
    query3 = "select t_name from doctor where name='" + doctor_name + "'"
    cursor3.execute(query3)
    cur3 = cursor3.fetchall()
    for i in cur3:
        table = i[0]

    num = 3
    a = datetime.today()
    # ===============================
    query = f"SELECT time FROM {table}"
    cursor.execute(query)
    cur = cursor.fetchall()

    Label(frame_reschedule_time, text="Date", bg="#aed3eb").grid(row=1, column=0)
    cal1 = DateEntry(frame_reschedule_time, date_pattern="yyyy-mm-dd")
    cal1.grid(row=1, column=1, columnspan=2)
    Button(frame_reschedule_time, text="Select Date", command=select).grid(
        row=1, column=3
    )

    # =====================================
    Label(
        frame_reschedule_time, text="AVAILABLE APPOINTMENTS", bg="#aed3eb", font=(18)
    ).grid(row=0, column=0, columnspan=2)
    Label(
        frame_reschedule_time,
        text="Time Slot",
        relief="groove",
        width=30,
        height=5,
        bg="#aed3eb",
    ).grid(row=2, column=0)
    new_time = StringVar(value=NONE)
    for i in cur:
        Label(
            frame_reschedule_time,
            text=i[0],
            relief="groove",
            width=30,
            height=5,
            bg="#aed3eb",
        ).grid(row=num, column=0)
        Radiobutton(
            frame_reschedule_time,
            value=i[0],
            variable=new_time,
            relief="groove",
            bg="#aed3eb",
            height=5,
        ).grid(row=num, column=2)
        num += 1

    def confirm():
        sel_date1 = convert_date_format(str(cal1.get_date()))
        query_check = f"select * from appointments where app_time='{new_time}' and app_date='{sel_date1}' and doctor_name='{doctor_name}'"
        cursor.execute(query_check)
        cur6 = cursor.fetchall()
        n = len(cur6)
        if n >= 1:
            messagebox.showerror("Sorry!", "This slot has already been booked")
            cursor.close()
        else:
            if cal1.get_date() < date.today():
                messagebox.showwarning("Warning!", "Please choose a valid Date")
                frame_reschedule_time.pack_forget()
                frame_reschedule_time.pack()
            else:
                cursor_main = mydb.cursor()
                query_main = f"update appointments set app_date='{cal1.get_date()}' ,app_time='{new_time.get()}' where app_id={app_id.get()}"
                cursor_main.execute(query_main)
                messagebox.showinfo(
                    "Success!",
                    f"Appointment rescheduled successfully.Your new date is '{cal1.get_date()}' and new time is '{new_time.get()}'.",
                )
                mydb.commit()

    Button(frame_reschedule_time, text="Confirm", command=confirm).grid(
        row=num, column=2
    )
    frame_reschedule_time.pack()


# ========================================================================================
def cancel_appointment():
    global app_id
    frame_reschedule_time.pack_forget()
    frame_patient_portal.pack_forget()
    frame_appointment.pack_forget()
    frame_check_status.pack_forget()
    frame_app_history.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_reschedule.pack_forget()

    frame_cancel_appointment.config(relief="sunken", bd=5, bg="#f57de3")
    root.config(bg="#80056d")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"select doctor_name,app_date,app_time,status,app_id from appointments where p_id='{e3.get()}' and app_date>=CURRENT_DATE"
    cursor.execute(query)
    cur = cursor.fetchall()
    num = 3
    app_id = StringVar(value=NONE)
    if len(cur) == 0:
        messagebox.showinfo("Sorry", "No appointments to be cancelled")
    else:
        Label(
            frame_cancel_appointment,
            text="SELECT APPOINTMENT TO BE CANCELLED",
            font=(18),
            bg="#f57de3",
        ).grid(row=1, column=0, columnspan=4)
        Label(
            frame_cancel_appointment,
            text="Doctor Name",
            relief="groove",
            width=30,
            height=5,
            bg="#f57de3",
        ).grid(row=2, column=0)
        Label(
            frame_cancel_appointment,
            text="Appointment Date",
            relief="groove",
            width=30,
            height=5,
            bg="#f57de3",
        ).grid(row=2, column=1)
        Label(
            frame_cancel_appointment,
            text="Appointment Time",
            relief="groove",
            width=30,
            height=5,
            bg="#f57de3",
        ).grid(row=2, column=2)
        Label(
            frame_cancel_appointment,
            text="Approval Status",
            relief="groove",
            width=30,
            height=5,
            bg="#f57de3",
        ).grid(row=2, column=3)
        for i in cur:
            Label(
                frame_cancel_appointment,
                text=i[0],
                relief="groove",
                width=30,
                height=5,
                bg="#f57de3",
            ).grid(row=num, column=0)
            Label(
                frame_cancel_appointment,
                text=i[1],
                relief="groove",
                width=30,
                height=5,
                bg="#f57de3",
            ).grid(row=num, column=1)
            Label(
                frame_cancel_appointment,
                text=i[2],
                relief="groove",
                width=30,
                height=5,
                bg="#f57de3",
            ).grid(row=num, column=2)
            if i[3] == "APPROVED":
                Label(
                    frame_cancel_appointment,
                    text=i[3],
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#f57de3",
                ).grid(row=num, column=3)
            else:
                Label(
                    frame_cancel_appointment,
                    text="PENDING",
                    relief="groove",
                    width=30,
                    height=5,
                    bg="#f57de3",
                ).grid(row=num, column=3)
            Radiobutton(
                frame_cancel_appointment,
                value=i[4],
                variable=app_id,
                height=5,
                bg="#f57de3",
            ).grid(row=num, column=4)
            num += 1
        Button(frame_cancel_appointment, text="NEXT", bg="yellow", command=cancel).grid(
            row=num, column=1
        )
    frame_cancel_appointment.pack()


# ========================================================================================
def cancel():
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"delete from appointments where app_id={app_id.get()}"
    cursor.execute(query)
    mydb.commit()
    messagebox.showinfo("Sucess!", "Appointment Cancelled Successfully")


# ========================================================================================
def app_history():
    frame_patient_portal.pack_forget()
    frame_check_status.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_reschedule_time.pack_forget()
    frame_appointment.pack_forget()
    frame_reschedule.pack_forget()

    frame_app_history.config(relief="sunken", bd=5, bg="#f75c63")
    root.config(bg="#731217")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"select doctor_name,app_date,app_time from appointments where p_id='{e3.get()}' and app_date>='{datetime.today().date()-timedelta(days=5)}'"
    cursor.execute(query)
    cur = cursor.fetchall()
    num = 3
    Label(frame_app_history, text="APPOINTMENT HISTORY", font=(18), bg="#f75c63").pack(
    )
# =========================================
    canvas = Canvas(frame_app_history)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame_app_history, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    row_frame1 = Frame(inner_frame)
    row_frame1.pack()
    Label(
        row_frame1, text="Doctor Name", relief="groove", width=30, height=5, bg="#f75c63"
    ).pack(side=LEFT)
    Label(
        row_frame1, text="Appointment Date", relief="groove", width=30, height=5, bg="#f75c63"
    ).pack(side=LEFT)
    Label(
        row_frame1, text="Appointment Time", relief="groove", width=30, height=5, bg="#f75c63"
    ).pack(side=LEFT)

    for i in cur:
        row_frame = Frame(inner_frame)
        row_frame.pack()

        Label(
            row_frame, text=i[0], relief="groove", width=30, height=5, bg="#f75c63"
        ).pack(side=LEFT)
        Label(
            row_frame, text=i[1], relief="groove", width=30, height=5, bg="#f75c63"
        ).pack(side=LEFT)
        Label(
            row_frame, text=i[2], relief="groove", width=30, height=5, bg="#f75c63"
        ).pack(side=LEFT)

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.config(height=700, width=645)
# ==============================================================
    # Label(
    #     frame_app_history,
    #     text="Doctor Name",
    #     relief="groove",
    #     width=30,
    #     height=1,
    #     bg="#f75c63",
    # ).grid(row=2, column=0)
    # Label(
    #     frame_app_history,
    #     text="Appointment Date",
    #     relief="groove",
    #     width=30,
    #     height=1,
    #     bg="#f75c63",
    # ).grid(row=2, column=1)
    # Label(
    #     frame_app_history,
    #     text="Appointment Time",
    #     relief="groove",
    #     width=30,
    #     height=1,
    #     bg="#f75c63",
    # ).grid(row=2, column=2)
    # for i in cur:
    #     Label(
    #         frame_app_history,
    #         text=i[0],
    #         relief="groove",
    #         width=30,
    #         height=1,
    #         bg="#f75c63",
    #     ).grid(row=num, column=0)
    #     Label(
    #         frame_app_history,
    #         text=i[1],
    #         relief="groove",
    #         width=30,
    #         height=1,
    #         bg="#f75c63",
    #     ).grid(row=num, column=1)
    #     Label(
    #         frame_app_history,
    #         text=i[2],
    #         relief="groove",
    #         width=30,
    #         height=1,
    #         bg="#f75c63",
    #     ).grid(row=num, column=2)
    #     num += 1

    frame_app_history.pack()


# ========================================================================================
def appointment():
    global appointment_time, d_name, sel_date, cal
    frame_patient_portal.pack_forget()
    frame_app_history.pack_forget()
    frame_generate_bill.pack_forget()
    frame_payment.pack_forget()
    frame_reschedule_time.pack_forget()
    frame_app_history.pack_forget()

    root.config(relief="sunken", bd=10, bg="#f55905")
    frame_appointment.config(relief="sunken", bd=5)
    d_name = doc_name.get()
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    cursor2 = mydb.cursor()
    query2 = "select t_name from doctor where name='" + d_name + "'"
    cursor2.execute(query2)
    cur2 = cursor2.fetchall()
    for i in cur2:
        table = i[0]

    query = f"SELECT time FROM {table}"
    cursor.execute(query)
    cur = cursor.fetchall()
    num = 3
    a = datetime.today()
    appointment_time = StringVar(value=NONE)
    Label(
        frame_appointment, text="AVAILABLE APPOINTMENTS", font=(28), bg="#fab996"
    ).grid()
    # ===============================
    cal = DateEntry(frame_appointment, date_pattern="yyyy-mm-dd")

    def select():
        global sel_date
        sel_date = cal.get_date()
        if sel_date < date.today():
            messagebox.showwarning("Warning!", "Please choose a valid Date")

    Label(frame_appointment, text="Date", bg="#fab996").grid(row=1, column=0)
    cal.grid(row=1, column=1, columnspan=2)
    Button(frame_appointment, text="Select Date", command=select).grid(row=1, column=3)

    # =====================================
    Label(frame_appointment, text=f"Date:-{a.date()}", bg="#fab996").grid()
    Label(
        frame_appointment,
        text="Time Slot",
        relief="groove",
        width=30,
        height=5,
        font=(18),
        bg="#fab996",
    ).grid(row=2, column=0)
    for i in cur:
        Label(
            frame_appointment,
            text=i[0],
            relief="groove",
            width=30,
            height=5,
            font=(18),
            bg="#fab996",
        ).grid(row=num, column=0)
        Radiobutton(
            frame_appointment,
            value=i[0],
            variable=appointment_time,
            relief="groove",
            height=5,
            bg="#fab996",
        ).grid(row=num, column=2)
        num += 1
    Button(frame_appointment, text="Book Slot", command=book_slot).grid(
        row=num, column=1
    )
    Button(frame_appointment, text="Generate Bill", command=generate_bill).grid(
        row=num, column=2
    )
    frame_appointment.pack()


# ========================================================================================
def book_slot():
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    entry = int(e3.get())
    query5 = f"SELECT id FROM doctor WHERE name='{d_name}'"
    cursor.execute(query5)
    cur5 = cursor.fetchall()

    query2 = f"SELECT name FROM patients WHERE userid={entry}"
    cursor.execute(query2)
    cur2 = cursor.fetchall()

    query4 = f"SELECT t_name FROM doctor WHERE name='{d_name}'"
    cursor.execute(query4)
    cur4 = cursor.fetchall()
    for i in cur4:
        table = i[0]

    query3 = f"UPDATE {table} SET status='OK' WHERE time='{appointment_time.get()}'"
    cursor.execute(query3)

    p_name = cur2[0][0]

    d_id = cur5[0][0]
    app_id = random.randint(1000000, 9999999)
    # ============================================
    sel_date1 = convert_date_format(str(sel_date))
    query_check = f"select * from appointments where app_time='{appointment_time.get()}' and app_date='{sel_date1}' and doctor_name='{d_name}'"
    cursor.execute(query_check)
    cur6 = cursor.fetchall()
    n = len(cur6)
    if n >= 1:
        messagebox.showerror("Sorry!", "This slot has already been booked")
        cursor.close()
    else:
        if sel_date < date.today():
            messagebox.showwarning("Warning!", "Please choose a valid Date")
            frame_appointment.pack_forget()
            frame_appointment.pack()
        else:
            mydb = myconn.connect(
                host="localhost", username="root", password="Garg@231", db="hospital"
            )
            cursor = mydb.cursor()
            query = "INSERT INTO appointments (p_id, p_name, doctor_name,doc_id, app_id,app_date,app_time) VALUES (%s, %s, %s, %s, %s,%s,%s)"
            values = (
                e3.get(),
                p_name,
                doc_name.get(),
                d_id,
                app_id,
                sel_date1,
                appointment_time.get(),
            )
            cursor.execute(query, values)
            mydb.commit()  # Commit the changes to the database
            messagebox.showinfo(
                "Success!",
                f"Appointment booked successfully for '{doc_name.get()}' between '{appointment_time.get()}' on {sel_date1}. Please visit at the scheduled time.",
            )

    # Close the cursors and the database connection
    cursor.close()
    mydb.close()


# ========================================================================================
def generate_bill():
    frame_appointment.pack_forget()
    frame_generate_bill.config(relief="sunken", bd=5, bg="#CCF381")
    root.config(bg="#4831D4")

    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"select app_id,doctor_name,app_date,app_time from appointments where p_id={e3.get()} and payment_status is NULL and app_date>=CURRENT_DATE"
    cursor.execute(query)
    data = cursor.fetchall()
    count = 0
    num = 3
    if len(data) == 0:
        messagebox.showinfo("SORRY", "No appointments pending for payment")
        frame_appointment.pack()
    else:
        Label(
            frame_generate_bill,
            text="APPOINTMENT ID",
            relief="groove",
            width=30,
            height=5,
            bg="#CCF381",
        ).grid(row=2, column=0)
        Label(
            frame_generate_bill,
            text="DOCTOR NAME",
            relief="groove",
            width=30,
            height=5,
            bg="#CCF381",
        ).grid(row=2, column=1)
        Label(
            frame_generate_bill,
            text="APPOINTMENT DATE",
            relief="groove",
            width=30,
            height=5,
            bg="#CCF381",
        ).grid(row=2, column=2)
        Label(
            frame_generate_bill,
            text="APPOINTMENT TIME",
            relief="groove",
            width=30,
            height=5,
            bg="#CCF381",
        ).grid(row=2, column=3)
        for i in data:
            Label(
                frame_generate_bill,
                text=i[0],
                relief="groove",
                width=30,
                height=5,
                bg="#CCF381",
            ).grid(row=num, column=0)
            Label(
                frame_generate_bill,
                text=i[1],
                relief="groove",
                width=30,
                height=5,
                bg="#CCF381",
            ).grid(row=num, column=1)
            Label(
                frame_generate_bill,
                text=i[2],
                relief="groove",
                width=30,
                height=5,
                bg="#CCF381",
            ).grid(row=num, column=2)
            Label(
                frame_generate_bill,
                text=i[3],
                relief="groove",
                width=30,
                height=5,
                bg="#CCF381",
            ).grid(row=num, column=3)
            num += 1
            count += 1
        Label(
            frame_generate_bill,
            text=f"YOUR BILL TOTAL IS {count*200}RS TO PAY USING QR CODE CLICK BELOW",
            font=("bold 18"),
            bg="#CCF381",
        ).grid(row=num, column=0, columnspan=5, rowspan=2)
        Button(frame_generate_bill, text="Payment", command=payment).grid(
            row=num + 2, column=1, columnspan=2
        )
    frame_generate_bill.pack()


# ========================================================================================
def payment():
    frame_generate_bill.pack_forget()
    frame_payment.config(relief=SUNKEN, bd=5)
    root.config(bg="#317773")
    global payment_status
    payment_status = "NO"
    image1 = Image.open("images/payment.jpg")
    image1 = image1.resize((300, 350))
    img2 = ImageTk.PhotoImage(image1)
    pic2 = Label(frame_payment, image=img2)
    pic2.image = img2
    Label(frame_payment, text="SCAN HERE TO PAY", font=("bold", 28)).pack(pady=20)
    pic2.pack(pady=80)
    Button(
        frame_payment,
        text="MAKE PAYMENT",
        bg="black",
        fg="white",
        font=(14),
        width=30,
        borderwidth=2,
        command=final_pay,
    ).pack()
    frame_payment.pack()


# ========================================================================================
def final_pay():
    mydb = myconn.connect(
        host="localhost", username="root", password="Garg@231", db="hospital"
    )
    cursor = mydb.cursor()
    query = f"update appointments set payment_status='YES' where p_id={e3.get()} and payment_status is NULL and app_date>=CURRENT_DATE"
    cursor.execute(query)
    mydb.commit()
    messagebox.showinfo(
        "Success",
        "Payment Successfull. Kindly check your Appointment status through your login id and password",
    )


# ========================================================================================
Button(
    frame_choice,
    text="PROCEED",
    bg="black",
    fg="white",
    command=btn_click,
    font=(14),
    width=10,
    borderwidth=2,
    activebackground="black",
    activeforeground="green",
).pack(ipadx=2)
root.mainloop()
