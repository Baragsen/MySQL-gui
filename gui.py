import customtkinter
import mysql_con

def login_success(frame , host_entry  ,port_entry ,username_entry , password_entry ) :
    con = mysql_con.handle_login(hostname= host_entry.get(),username= username_entry.get(),passw= password_entry.get() , port=port_entry.get())
    if con == True :
        frame.destroy()


app = customtkinter.CTk()
app.geometry("800x600")

def create_login_page(): 
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=20 , padx=60 , fill="both" , expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login" , font=("Roboto" , 30))
    label.pack(padx=20 , pady=22)

    host_entry = customtkinter.CTkEntry(frame, placeholder_text="hostname" , height=35)
    host_entry.pack(padx=10,pady=22)

    port_entry = customtkinter.CTkEntry(frame, placeholder_text="port(3306 by default)" , height=35)
    port_entry.pack(padx=10,pady=22)


    username_entry= customtkinter.CTkEntry(frame, placeholder_text="Username" , height=35)
    username_entry.pack(padx=10,pady=22)

    password_entry= customtkinter.CTkEntry(frame, placeholder_text="Password" , show="*" , height=35)
    password_entry.pack(padx=10,pady=22)

    login_button= customtkinter.CTkButton(master=frame , text="Login" , command= lambda:login_success(frame , host_entry , port_entry , username_entry , password_entry))
    login_button.pack(padx=10,pady=22 )
create_login_page()

app.mainloop()



