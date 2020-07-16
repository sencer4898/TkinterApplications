import tkinter as tk
import sqlite3
from tkinter import messagebox

# Create the window   

root = tk.Tk()
root.geometry("700x700")
root.title("Contact Book")
root.configure(background="white")
root.iconbitmap("book_icon.ico")
root.resizable(False,False)

def createTable():
    con = sqlite3.connect('contact_book.db')
    cursor = con.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS contacts(name TEXT, adress TEXT, phone TEXT, email TEXT)')
    
    con.commit()
    con.close()

createTable()

class ContactBook():   

    # Add Find Delete Update List
    name = tk.StringVar(value='')
    adress = tk.StringVar(value='')
    phone = tk.StringVar(value='')
    email = tk.StringVar(value='')
    id=tk.StringVar(value='')
    
    menu_number = 0

    def __init__ (self,parent):
        self.parent = parent

    def mainMenu(self):
        self.main_menu_title = tk.Label(self.parent,text="Welcome to Contact Book!".upper())
        self.main_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.main_menu_title.pack(pady=50)

        self.add_contact_button = tk.Button(self.parent,text="Add a contact".upper(),command=self.insertMenu)
        self.add_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.add_contact_button.pack(pady=15)

        self.find_contact_button = tk.Button(self.parent,text="Find a contact".upper(),command=self.findMenu)
        self.find_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.find_contact_button.pack(pady=15)

        self.delete_contact_button = tk.Button(self.parent,text="Delete a contact".upper(),command=self.deleteMenu)
        self.delete_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.delete_contact_button.pack(pady=15)

        self.update_contact_button = tk.Button(self.parent,text="Update a contact".upper(),command=self.updateMenu)
        self.update_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.update_contact_button.pack(pady=15)

        self.list_contacts_button = tk.Button(self.parent,text="List all contacts".upper(),command=self.listMenu)
        self.list_contacts_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.list_contacts_button.pack(pady=15)

        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.pack(pady=30)
    
    def destroyMainMenu(self):
        self.main_menu_title.pack_forget()
        self.add_contact_button.pack_forget()
        self.find_contact_button.pack_forget()
        self.delete_contact_button.pack_forget()
        self.update_contact_button.pack_forget()
        self.list_contacts_button.pack_forget()
        self.exit_button.pack_forget()

    def add_main_menu(self):
        
        if(self.menu_number==1):
            self.destroyInsertMenu()
        elif(self.menu_number==2):
            self.destroyFindMenu()
        elif(self.menu_number==3):
            self.destroyDeleteMenu()
        elif(self.menu_number==4):
            self.destroyUpdateMenu()
        elif(self.menu_number==5):
            self.destroyListMenu()
            
        self.menu_number=0
        
        self.mainMenu()

    def insertMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=1

        self.add_menu_title = tk.Label(self.parent,text="Add a Contact".upper())
        self.add_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.add_menu_title.place(x=220,y=50)

        # Name

        self.name_label = tk.Label(self.parent,text="Name : ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 130, y= 150)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230,y=150)

        # Adress

        self.adress_label = tk.Label(self.parent,text="Adress : ")
        self.adress_label.configure(font='Helvetica 18', bg="white")
        self.adress_label.place(x= 130, y= 200)

        self.adress_entry = tk.Entry(self.parent)
        self.adress_entry.configure(font='Helvetica 18', bg="white")
        self.adress_entry.place(x=230,y=200)

        # Phone

        self.phone_label = tk.Label(self.parent,text="Phone : ")
        self.phone_label.configure(font='Helvetica 18', bg="white")
        self.phone_label.place(x= 130, y= 250)

        self.phone_entry = tk.Entry(self.parent)
        self.phone_entry.configure(font='Helvetica 18', bg="white")
        self.phone_entry.place(x=230,y=250)

        # Email

        self.email_label = tk.Label(self.parent,text="Email : ")
        self.email_label.configure(font='Helvetica 18', bg="white")
        self.email_label.place(x= 130, y= 300)

        self.email_entry = tk.Entry(self.parent)
        self.email_entry.configure(font='Helvetica 18', bg="white")
        self.email_entry.place(x=230,y=300)
        
        # Buttons
        
        self.add_button = tk.Button(self.parent,
                                    text='Add the contact',command=self.add)
        self.add_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.add_button.place(x=230,y=350)
        
        self.main_menu_button = tk.Button(self.parent, text='Main Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=420)
        
        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=490)
        
    def destroyInsertMenu(self):
        self.add_menu_title.place_forget()
        
        self.name_label.destroy()
        self.name_entry.destroy()
        
        self.adress_label.destroy()
        self.adress_entry.destroy()
        
        self.phone_label.destroy()
        self.phone_entry.destroy()
        
        self.email_label.destroy()
        self.email_entry.destroy()
        
        self.add_button.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
        
    def add(self):
        self.name = self.name_entry.get()
        self.adress = self.adress_entry.get()
        self.phone = self.phone_entry.get()
        self.email = self.email_entry.get()
        
        if len((self.name+self.adress+self.phone+self.email).strip())==0:
            messagebox.showerror('Contact Book','Information missing.')
        else:
            
            self.name_entry.delete(0,'end')
            self.adress_entry.delete(0,'end')
            self.phone_entry.delete(0,'end')
            self.email_entry.delete(0,'end')
            
            con = sqlite3.connect("contact_book.db")
            cursor = con.cursor()
            
            cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)",
                           (self.name,self.adress,self.phone,self.email))
    
            con.commit()
            con.close()
        
            messagebox.showinfo('Contact Book','Contact added successfully.')

    def findMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=2
        
        self.find_menu_title = tk.Label(self.parent,text="Find Contact".upper())
        self.find_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.find_menu_title.place(x=242,y=50)

        # Name

        self.name_label = tk.Label(self.parent,text="Name : ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 130, y= 150)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230,y=150)
        
        # Found contacts
        
        self.labels = tk.Label(self.parent,text=" ID     Name         Adress         Phone         Email")
        self.labels.configure(background='white',font='Helvetica 12 bold')
        self.labels.place(x= 185, y = 270)
        
        self.found_contacts = tk.Frame(self.parent, width=50,height=250)
        self.found_contacts.place(x=185, y= 300)
        
        self.scrollbar=tk.Scrollbar(self.found_contacts)
        self.scrollbar.pack(side="right",fill='y')
        
        self.contact_list = tk.Listbox(self.found_contacts, yscrollcommand = self.scrollbar.set,width=37)
        self.contact_list.configure(font='Helvetica 12')
        self.contact_list.pack( side = "left", fill = "both")
        self.scrollbar.config( command = self.contact_list.yview )
        
        # Buttons
        
        self.find_button = tk.Button(self.parent,
                                    text='Find',command=self.find)
        self.find_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.find_button.place(x=230,y=215)
        
        self.main_menu_button = tk.Button(self.parent, text='Main Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=610)
        
    def destroyFindMenu(self):
        self.find_menu_title.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.labels.destroy()
        self.found_contacts.destroy()
        self.find_button.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
    
    def find(self):      
        self.name = self.name_entry.get()
        
        con = sqlite3.connect('contact_book.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT oid,* FROM contacts WHERE name=?',(self.name,))
        self.found_people=cursor.fetchall()
        
        self.contact_list.delete(0,'end')
        
        if len(self.found_people)==0:
            messagebox.showinfo('Contact Book','No such contact is found.')
        else:
            for person in self.found_people:
                self.contact_list.insert(0,
               str(list(person)[0])+" "+list(person)[1]+" "+list(person)[2]+" "+list(person)[3]+" "+list(person)[4])
            
        con.close()
        
    def deleteMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=3
        
        self.delete_menu_title = tk.Label(self.parent,text="Delete Contact".upper())
        self.delete_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.delete_menu_title.place(x=220,y=50)
        
        # ID

        self.id_label = tk.Label(self.parent,text="ID : ")
        self.id_label.configure(font='Helvetica 18', bg="white")
        self.id_label.place(x= 130, y= 150)

        self.id_entry = tk.Entry(self.parent)
        self.id_entry.configure(font='Helvetica 18', bg="white")
        self.id_entry.place(x=230,y=150)
        
        # Deleted Contacts
        
        self.deleted_contacts_label = tk.Label(self.parent,bg='white')
        self.deleted_contacts_label.place(x=0,y=0)
        
        
        # Buttons
        
        self.delete_button = tk.Button(self.parent,
                                    text='Delete',command=self.delete)
        self.delete_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.delete_button.place(x=230,y=215)
        
        self.main_menu_button = tk.Button(self.parent, text='Main Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=610)
        
    def destroyDeleteMenu(self):
        self.delete_menu_title.destroy()
        self.id_label.destroy()
        self.id_entry.destroy()
        self.delete_button.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
        self.deleted_contacts_label.destroy()

    def delete(self):
        self.id = self.id_entry.get()
        
        if len(self.id)>0:
            con=sqlite3.connect('contact_book.db')
            cursor = con.cursor()
            
            cursor.execute('SELECT * FROM contacts WHERE oid=?',(self.id,))
            self.found_contact = cursor.fetchall()
            if len(self.found_contact)==0:
                messagebox.showerror('Contact Book','Invalid ID!')
            else:
                string="Deleted: "+self.found_contact[0][0]+"  "+self.found_contact[0][1]+"  "+self.found_contact[0][2]+"  "+self.found_contact[0][3]
                self.deleted_contacts_label.destroy()
                self.deleted_contacts_label=tk.Label(self.parent,text=string)
                self.deleted_contacts_label.configure(bg='white',font='Helvetica 18')
                self.deleted_contacts_label.place(x=130,y=380)
                cursor.execute('DELETE FROM contacts WHERE oid=?',(self.id,))
                con.commit()
                messagebox.showinfo('Contact Book','Contact Deleted Successfully.')
            
            con.close()
        else:
            messagebox.showerror('Contact Book','ID Missing!')

    def updateMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=4
        self.id=-1
        
        
        self.update_menu_title = tk.Label(self.parent,text="Add a Contact".upper())
        self.update_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.update_menu_title.place(x=220,y=50)

        # Id
        
        self.id_label = tk.Label(self.parent,text="      ID : ")
        self.id_label.configure(font='Helvetica 18', bg="white")
        self.id_label.place(x= 130, y= 150)

        self.id_entry = tk.Entry(self.parent)
        self.id_entry.configure(font='Helvetica 18', bg="white")
        self.id_entry.place(x=230,y=150)

        # Name

        self.name_label = tk.Label(self.parent,text="Name : ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 130, y=250)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230, y=250)

        # Adress

        self.adress_label = tk.Label(self.parent,text="Adress : ")
        self.adress_label.configure(font='Helvetica 18', bg="white")
        self.adress_label.place(x= 130, y= 300)

        self.adress_entry = tk.Entry(self.parent)
        self.adress_entry.configure(font='Helvetica 18', bg="white")
        self.adress_entry.place(x=230,y= 300)

        # Phone

        self.phone_label = tk.Label(self.parent,text="Phone : ")
        self.phone_label.configure(font='Helvetica 18', bg="white")
        self.phone_label.place(x= 130, y= 350)

        self.phone_entry = tk.Entry(self.parent)
        self.phone_entry.configure(font='Helvetica 18', bg="white")
        self.phone_entry.place(x=230, y = 350)

        # Email

        self.email_label = tk.Label(self.parent,text="Email : ")
        self.email_label.configure(font='Helvetica 18', bg="white")
        self.email_label.place(x= 130, y = 400)

        self.email_entry = tk.Entry(self.parent)
        self.email_entry.configure(font='Helvetica 18', bg="white")
        self.email_entry.place(x=230,y = 400)
        
        # Buttons
        
        self.open_contact_button = tk.Button(self.parent,
                                    text='Open the Contact',command=self.open_contact)
        self.open_contact_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.open_contact_button.place(x=230,y=190)
        
        self.update_button = tk.Button(self.parent,
                                    text='Update the Contact',command=self.update)
        self.update_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.update_button.place(x=230,y=450)
        
        self.main_menu_button = tk.Button(self.parent, text='Main Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=520)
        
        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=590)
        
        

    def destroyUpdateMenu(self):
        self.update_menu_title.destroy()
        
        self.id_label.destroy()
        self.id_entry.destroy()
        
        self.name_label.destroy()
        self.name_entry.destroy()
        
        self.adress_label.destroy()
        self.adress_entry.destroy()
        
        self.phone_label.destroy()
        self.phone_entry.destroy()
        
        self.email_label.destroy()
        self.email_entry.destroy()
        
        self.open_contact_button.destroy()
        self.update_button.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
        
    
    def open_contact(self):
        self.id = self.id_entry.get()
        
        self.name_entry.delete(0,'end')
        self.adress_entry.delete(0,'end')
        self.phone_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        
        
        con = sqlite3.connect('contact_book.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM contacts WHERE oid=?',(self.id,))
        self.found_people=cursor.fetchall()
        
        if len(self.found_people)==0:
            messagebox.showinfo('Contact Book','Invalid ID!')
        else:
            for person in self.found_people:
                self.name_entry.insert(0,person[0])
                self.adress_entry.insert(0,person[1])
                self.phone_entry.insert(0,person[2])
                self.email_entry.insert(0,person[3])
            
        con.close()
    
    def update(self):
        
        self.name=self.name_entry.get()
        self.adress=self.adress_entry.get()
        self.phone=self.phone_entry.get()
        self.email=self.email_entry.get()
        
        con = sqlite3.connect('contact_book.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM contacts WHERE oid=?',(self.id,))
        self.found_contact = cursor.fetchall()
        if len(self.found_contact)>0:
            cursor.execute('UPDATE contacts SET name=?, adress=?, phone=?, email=? WHERE oid=?',(self.name,self.adress,
                                                                                             self.phone,self.email,
                                                                                             self.id))
            messagebox.showinfo('Contact Book', 'Contact Updated Successfully!')
        else:
            messagebox.showerror('Contact Book','Invalid ID!')
            
        con.commit()
        con.close()
    
    def listMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=5
        
        self.list_all_menu_title = tk.Label(self.parent,text="List All Contacts".upper())
        self.list_all_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.list_all_menu_title.place(x=195,y=50)
        
        # Found contacts
        
        self.labels = tk.Label(self.parent,text=" ID     Name         Adress         Phone         Email")
        self.labels.configure(background='white',font='Helvetica 12 bold')
        self.labels.place(x= 185, y = 200)
        
        self.found_contacts = tk.Frame(self.parent, width=50,height=250)
        self.found_contacts.place(x=185, y= 230)
        
        self.scrollbar=tk.Scrollbar(self.found_contacts)
        self.scrollbar.pack(side="right",fill='y')
        
        self.contact_list = tk.Listbox(self.found_contacts, yscrollcommand = self.scrollbar.set,width=37)
        self.contact_list.configure(font='Helvetica 12')
        self.contact_list.pack( side = "left", fill = "both")
        self.scrollbar.config( command = self.contact_list.yview)
        
        con = sqlite3.connect('contact_book.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT oid,* FROM contacts ORDER BY name DESC')
        self.found_people=cursor.fetchall()
        
        if len(self.found_people)==0:
            messagebox.showinfo('Contact Book','Contact Book Is Empty.')
        else:
            for person in self.found_people:
                self.contact_list.insert(0,
               str(list(person)[0])+" "+list(person)[1]+" "+list(person)[2]+" "+list(person)[3]+" "+list(person)[4])
            
        con.close()
        
        # Buttons
        
        self.main_menu_button = tk.Button(self.parent, text='Main Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Exit".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=610)
    
    def destroyListMenu(self):
        self.list_all_menu_title.destroy()
        self.labels.destroy()
        self.found_contacts.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
    
myBook = ContactBook(root)
myBook.mainMenu()

root.mainloop()
