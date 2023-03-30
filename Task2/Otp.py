from tkinter import *
from tkinter import messagebox
import random
import smtplib

class OTPVerification:
    def __init__(self, master):
        self.master = master
        master.title("OTP Verification")
        master.geometry("300x250")
        master.resizable(False, False)

        # Create and pack the Email label and entry field
        self.email_label = Label(master, text="Enter Email Address:", font=("Arial", 12))
        self.email_label.pack()
        self.email_entry = Entry(master, font=("Arial", 12))
        self.email_entry.pack()

        # Create and pack the Generate OTP button
        self.generate_otp_button = Button(master, text="Generate OTP", font=("Arial", 12, "bold"), fg="white", bg="#3D4A55", command=self.generate_otp)
        self.generate_otp_button.pack(pady=10)

        # Create and pack the OTP label and entry field
        self.otp_label = Label(master, text="OTP:", font=("Arial", 12))
        self.otp_label.pack()
        self.otp_entry = Entry(master, font=("Arial", 12))
        self.otp_entry.pack()

        # Create and pack the Verify OTP button
        self.verify_button = Button(master, text="Verify OTP", font=("Arial", 12, "bold"), fg="white", bg="#3D4A55", command=self.verify_otp)
        self.verify_button.pack(pady=10)

        # Initialize the generated OTP to None
        self.generated_otp = None

    def generate_otp(self):
        self.generated_otp = random.randint(1000, 9999)
        email = self.email_entry.get()
        if email == "":
            messagebox.showerror("Error", "Email address cannot be empty!")
        else:
            # Send the OTP to the user's email address
            try:
                self.send_otp(email, self.generated_otp)
                messagebox.showinfo("OTP Generated", "OTP sent to your email address!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send OTP: {str(e)}")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == str(self.generated_otp):
            messagebox.showinfo("Success", "OTP Verified!")
        else:
            messagebox.showerror("Error", "Invalid OTP!")

    def send_otp(self, email, otp):
        # Set up the email server and login credentials
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('udayrajms2023@gmail.com',"cefrvkyloxqijysc")

        # Compose the email message
        subject = "OTP Verification"
        body = f"Your OTP is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail("your_email@gmail.com", email, message)

        # Close the email server connection
        server.quit()

root = Tk()
otp_verification = OTPVerification(root)
root.mainloop()
