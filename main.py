import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import shelve

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.resizable(False, False)  # set the window to non-resizable

        pygame.init()

        # Set the window to the center of the monitor
        self.login_width = 470
        self.login_height = 600
        self.ws, self.hs = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        x, y = (self.ws - self.login_width) // 2, (self.hs - self.login_height) // 2
        self.master.geometry(f"{self.login_width}x{self.login_height}+{int(x)}+{int(y)}")

        # Set the background color of the main window
        self.master.configure(bg="#121212")

        # Initialize the user list
        self.userList = []

        # Load the saved user credentials
        self.load_credentials()

        # Add some users to the list
        self.userList.append(User("user1", "password1"))
        self.userList.append(User("user2", "password2"))

        # Load the sound effect
        music_files = ['Rickroll.mp3']

        # Choose a random music file to play
        music_file = random.choice(music_files)

        # Load the sound effect
        pygame.mixer.music.load(music_file)

        # Play the music
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.4)

        # Create a Frame to hold the login form
        loginFrame = Frame(self.master, padx=20, pady=20,background="#121212")
        loginFrame.pack()

        # Add a title
        titleLabel = Label(loginFrame, text="Welcome Back!", font=("SF Pro", 30), bg="#121212", fg="white")
        titleLabel.pack(side=TOP, pady=(0, 20))

        # Add a logo
        logoImg = Image.open("GroupOfCats.png")
        logoImg = logoImg.resize((335, 230), Image.LANCZOS)  # Resize the image
        logoImg = ImageTk.PhotoImage(logoImg)
        logoLabel = Label(loginFrame, image=logoImg, bg="#121212")
        logoLabel.image = logoImg
        logoLabel.pack()

        # Add a username field
        usernameLabel = Label(loginFrame, text="Username:", font=("Arial", 16), fg="white", bg="#121212")
        usernameLabel.pack(pady=(20, 0))
        self.usernameEntry = Entry(loginFrame, font=("Arial", 16), width=30)
        self.usernameEntry.pack()

        # Add a password field
        passwordLabel = Label(loginFrame, text="Password:", font=("Arial", 16), fg="white", bg="#121212")
        passwordLabel.pack(pady=(20, 0))
        self.passwordEntry = Entry(loginFrame, font=("Arial", 16), show="*", width=30)
        self.passwordEntry.pack()

        # Add a login button
        loginButton = Button(loginFrame, text="Login", bg="#f2c400", fg="#000000", font=("Arial", 16),
                             command=self.login, foreground="#121212")
        loginButton.pack(pady=(20, 0))
        loginButton.config(width=20, height=1)

        # Bind the "<Return>" event to the login button
        self.master.bind("<Return>", lambda event: loginButton.invoke())

        # Add a register link
        registerLink = Label(loginFrame, text="Don't have an account? Register now!", fg="white", cursor="hand2",
                             bg='#121212')
        registerLink.pack(pady=(10, 0))
        registerLink.bind("<Button-1>", lambda event: self.register())

    def load_credentials(self):
        # Load the saved user credentials
        with shelve.open("users") as db:
            try:
                self.userList = db["users"]
            except KeyError:
                # If no user credentials are found, create an empty list
                self.userList = []

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        # Check if the username and password are in the user list
        for user in self.userList:
            if username == user.username and password == user.password:
                messagebox.showinfo("Success", "Login successful!")
                self.usernameEntry.delete(0, END)
                self.passwordEntry.delete(0, END)
                return

        # If the username and password are not in the user list, show an error message
        messagebox.showerror("Error", "Invalid username or password!")

    def register(self):
        # Closes the login page
        self.master.withdraw()

        # Create a new window for registration
        registerWindow = Toplevel(self.master)
        registerWindow.title("Registration Page")
        registerWindow.resizable(False, False)  # set the window to non-resizable

        # Set the window to the center of the monitor
        registerWidth = 450
        registerHeight = 600
        ws, hs = registerWindow.winfo_screenwidth(), registerWindow.winfo_screenheight()
        x, y = (ws - registerWidth) // 2, (hs - registerHeight) // 2
        registerWindow.geometry(f"{registerWidth}x{registerHeight}+{int(x)}+{int(y)}")

        # Create a Frame to hold the registration form
        registerFrame = Frame(registerWindow, padx=20, pady=20, bg="#121212")  # change background color
        registerFrame.pack()

        #Add a back button link
        backButton = Label(registerFrame, text="Back", fg="white", cursor="hand2", bg='#121212',font=("Ariall",10))
        backButton.pack(side="left", pady=(530, 0), padx=(50, 0))
        backButton.config(width=5, height=1)
        backButton.bind("<Button-1>", lambda event: (registerWindow.destroy(), self.master.deiconify()))

        # Add a title
        titleLabel = Label(registerFrame, text="Create an Account", font=("SF Pro", 30), bg="#121212", fg="white")
        titleLabel.pack(side=TOP, pady=(0, 10))

        # Add a logo
        logoImg = Image.open("Cat.png")
        logoImg = logoImg.resize((250, 240), Image.LANCZOS)  # Resize the image
        logoImg = ImageTk.PhotoImage(logoImg)
        logoLabel = Label(registerFrame, image=logoImg, bg="#121212")
        logoLabel.image = logoImg
        logoLabel.place(relx=0.5, rely=0.37, anchor="center")

        # Set the background color of the main window
        registerWindow.configure(bg="#121212")

        # Add a username field
        usernameLabel = Label(registerFrame, text="Username:", font=("Arial", 16), bg="#121212", fg="white")
        usernameLabel.place(relx=0.5, rely=0.54, anchor="center")
        self.registerUsernameEntry = Entry(registerFrame, font=("Arial", 16), width=30)
        self.registerUsernameEntry.place(relx=0.5, rely=0.60, anchor="center")

        # Add a password field
        passwordLabel = Label(registerFrame, text="Password:", font=("Arial", 16), bg="#121212", fg="white")
        passwordLabel.place(relx=0.5, rely=0.67, anchor="center")
        self.registerPasswordEntry = Entry(registerFrame, show="*", font=("Arial", 16), width=30)
        self.registerPasswordEntry.place(relx=0.5, rely=0.73, anchor="center")

        # Add a confirm password field
        confirmPasswordLabel = Label(registerFrame, text="Confirm Password:", font=("Arial", 16), bg="#121212",
                                     fg="white")
        confirmPasswordLabel.place(relx=0.5, rely=0.8, anchor="center")
        self.confirmPasswordEntry = Entry(registerFrame, show="*", font=("Arial", 16), width=30)
        self.confirmPasswordEntry.place(relx=0.5, rely=0.86, anchor="center")

        # Add a register button
        registerButton = Button(registerFrame, text="Register", bg="#f2c400", fg="#000000", font=("Arial", 16),
                                command=self.addUser)
        registerButton.place(relx=0.5, rely=0.98, anchor="center")
        registerButton.config(width=10, height=1)

        # Bind the Enter key to the register button
        registerWindow.bind('<Return>', lambda event: registerButton.invoke())

        # Destroy the root window when the registration page is closed
        registerWindow.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def addUser(self):
        username = self.registerUsernameEntry.get()
        password = self.registerPasswordEntry.get()
        confirmPassword = self.confirmPasswordEntry.get()

        # Check if the username and password fields are not empty
        if username == "" or password == "" or confirmPassword == "":
            messagebox.showerror("Error", "Please fill all the fields!")
            return

        # Check if the password and confirm password fields match
        if password != confirmPassword:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Load the user list from disk
        with shelve.open("users") as db:
            self.userList = db.get("users", [])

        # Check if the username already exists in the user list
        for user in self.userList:
            if username == user.username:
                messagebox.showerror("Error", "Username already exists!")
                return

        # Check if the length of the username is valid
        if len(username) < 8 or len(username) > 16:
            messagebox.showerror("Error", "Username must be between 8 and 16 characters!")
            return

        # Check if the length of the password is valid
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters!")
            return

        # Create a new user object and add it to the user list
        newUser = User(username, password)
        self.userList.append(newUser)

        # Save the user list to disk
        with shelve.open("users") as db:
            db["users"] = self.userList

        # Show a success message
        messagebox.showinfo("Success", "Registration successful!")

        # Clear the registration form fields
        self.registerUsernameEntry.delete(0, END)
        self.registerPasswordEntry.delete(0, END)
        self.confirmPasswordEntry.delete(0, END)

root = Tk()
app = Login(root)
root.mainloop()