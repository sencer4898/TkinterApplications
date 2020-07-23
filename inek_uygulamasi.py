import tkinter as tk
import sqlite3
from tkinter import messagebox
import datetime

# Create the window   

root = tk.Tk()
root.geometry("700x700")
root.title("Inek Uygulamasi")
root.configure(background="white")
root.resizable(False,False)

def createTable():
    con = sqlite3.connect('inek_defteri.db')
    cursor = con.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS inekler(kulakNo TEXT, dogumTarihi TEXT, gebelikTarihi TEXT, hastaliklar TEXT, asilar TEXT)')
    
    con.commit()
    con.close()

createTable()



class ContactBook():   

    # Add Find Delete Update List
    
    menu_number = 0

    def __init__ (self,parent):
        self.parent = parent
        
    def kuruDonemi(self):
        con = sqlite3.connect('inek_defteri.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM inekler")
        inek_listesi = cursor.fetchall()
        
        kuru_listesi=[]
        
        for inek in inek_listesi:
            gebelik_tarihi = inek[2]
            
            date = datetime.datetime.strptime(gebelik_tarihi,"%d.%m.%Y")        
            past=datetime.datetime.timestamp(date)
            
            now = datetime.datetime.now().timestamp()      
            
            kuru_zamani_date1 = datetime.datetime.strptime('01.01.2001',"%d.%m.%Y")
            kuru_zamani_date2 = datetime.datetime.strptime('01.10.2001',"%d.%m.%Y")
            kuru_zamani_date3 = datetime.datetime.strptime('15.10.2001',"%d.%m.%Y")
            kuru_zamani1= datetime.datetime.timestamp(kuru_zamani_date1)
            kuru_zamani2= datetime.datetime.timestamp(kuru_zamani_date2)
            kuru_zamani3= datetime.datetime.timestamp(kuru_zamani_date3)
            kuru_zamani = kuru_zamani2 - kuru_zamani1
            gebelik_limit=kuru_zamani3 - kuru_zamani1
            
            gebelik_suresi = now-past
            
            if (gebelik_suresi>kuru_zamani) and (gebelik_suresi<gebelik_limit):
               kuru_listesi.append(inek[0]) 
        
        kuru_string = "Kuruya Cikacak Inekler: "
        
        for kulakNo in kuru_listesi:
            kuru_string +=  "\n" + kulakNo
        
        if not len(kuru_listesi)==0:    
            messagebox.showinfo('Inek Defteri',kuru_string)
        else:
            messagebox.showinfo('Inek Defteri','Kuruya cikmasi gereken inek bulunmamaktadir.')
        
        con.close()
    
    def gebelikDonemi(self):
        con = sqlite3.connect('inek_defteri.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM inekler")
        inek_listesi = cursor.fetchall()
        
        kuru_listesi=[]
        
        for inek in inek_listesi:
            gebelik_tarihi = inek[2]
            
            date = datetime.datetime.strptime(gebelik_tarihi,"%d.%m.%Y")        
            past=datetime.datetime.timestamp(date)
            
            now = datetime.datetime.now().timestamp()      
            
            kuru_zamani_date1 = datetime.datetime.strptime('01.01.2001',"%d.%m.%Y")
            kuru_zamani_date2 = datetime.datetime.strptime('01.10.2001',"%d.%m.%Y")
            kuru_zamani_date3 = datetime.datetime.strptime('15.10.2001',"%d.%m.%Y")
            kuru_zamani1= datetime.datetime.timestamp(kuru_zamani_date1)
            kuru_zamani2= datetime.datetime.timestamp(kuru_zamani_date2)
            kuru_zamani3= datetime.datetime.timestamp(kuru_zamani_date3)
            kuru_zamani = kuru_zamani2 - kuru_zamani1
            gebelik_limit=kuru_zamani3 - kuru_zamani1
            
            gebelik_suresi = now-past
            
            
            if (gebelik_suresi>kuru_zamani) and (gebelik_suresi<gebelik_limit):
               kuru_listesi.append(inek[0]) 
        
        kuru_string = "Dogurmasina 10 gunden az kalan inekler: "
        
        for kulakNo in kuru_listesi:
            kuru_string +=  "\n" + kulakNo
        
        if not len(kuru_listesi)==0:    
            messagebox.showinfo('Inek Defteri',kuru_string)
        else:
            messagebox.showinfo('Inek Defteri','Dogurmasina 10 gunden az kalan inek bulunmamaktadir.')
        
        con.close()
    
    def mainMenu(self):
        self.main_menu_title = tk.Label(self.parent,text="Inek Kayit Uygulamasi".upper())
        self.main_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.main_menu_title.pack(pady=50)

        self.add_contact_button = tk.Button(self.parent,text="Inek Ekle".upper(),command=self.insertMenu)
        self.add_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.add_contact_button.pack(pady=15)

        self.find_contact_button = tk.Button(self.parent,text="Inek Bul".upper(),command=self.findMenu)
        self.find_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.find_contact_button.pack(pady=15)

        self.delete_contact_button = tk.Button(self.parent,text="Inek Sil".upper(),command=self.deleteMenu)
        self.delete_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.delete_contact_button.pack(pady=15)

        self.update_contact_button = tk.Button(self.parent,text="Inek Guncelle".upper(),command=self.updateMenu)
        self.update_contact_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.update_contact_button.pack(pady=15)

        self.list_contacts_button = tk.Button(self.parent,text="Inekleri Listele".upper(),command=self.listMenu)
        self.list_contacts_button.configure(font='Helvetica 18',bd=2, bg="white",relief="solid",width=18)
        self.list_contacts_button.pack(pady=15)

        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.pack(pady=15)
        
        self.kuru_butonu = tk.Button(self.parent,text='Kuruya Cikacaklar',command=self.kuruDonemi)
        self.kuru_butonu.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.kuru_butonu.pack(pady=5)
        
        self.gebe_butonu = tk.Button(self.parent,text='Doguma 10 Kalanlar',command=self.gebelikDonemi)
        self.gebe_butonu.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.gebe_butonu.pack(pady=5)
    
    def destroyMainMenu(self):
        self.main_menu_title.pack_forget()
        self.add_contact_button.pack_forget()
        self.find_contact_button.pack_forget()
        self.delete_contact_button.pack_forget()
        self.update_contact_button.pack_forget()
        self.list_contacts_button.pack_forget()
        self.exit_button.pack_forget()
        self.kuru_butonu.pack_forget()
        self.gebe_butonu.pack_forget()

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

        self.add_menu_title = tk.Label(self.parent,text="Inek Ekle".upper())
        self.add_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.add_menu_title.place(x=280,y=50)

        # Name

        self.name_label = tk.Label(self.parent,text="Kulak No : ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 100, y= 150)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230,y=150)

        # Adress

        self.adress_label = tk.Label(self.parent,text="Dogum Tarihi : ")
        self.adress_label.configure(font='Helvetica 18', bg="white")
        self.adress_label.place(x= 50, y= 200)

        self.adress_entry = tk.Entry(self.parent)
        self.adress_entry.configure(font='Helvetica 18', bg="white")
        self.adress_entry.place(x=230,y=200)

        # Phone

        self.phone_label = tk.Label(self.parent,text="Gebelik Tarihi : ")
        self.phone_label.configure(font='Helvetica 18', bg="white")
        self.phone_label.place(x= 50, y= 250)

        self.phone_entry = tk.Entry(self.parent)
        self.phone_entry.configure(font='Helvetica 18', bg="white")
        self.phone_entry.place(x=230,y=250)

        # Email

        self.email_label = tk.Label(self.parent,text="Hastaliklar : ")
        self.email_label.configure(font='Helvetica 18', bg="white")
        self.email_label.place(x= 80, y= 300)

        self.email_entry = tk.Entry(self.parent)
        self.email_entry.configure(font='Helvetica 18', bg="white")
        self.email_entry.place(x=230,y=300)
        
        # Family

        self.family_label = tk.Label(self.parent,text="Asilar : ")
        self.family_label.configure(font='Helvetica 18', bg="white")
        self.family_label.place(x= 130, y= 350)

        self.family_entry = tk.Entry(self.parent)
        self.family_entry.configure(font='Helvetica 18', bg="white")
        self.family_entry.place(x=230,y=350)
        
        # Buttons
        
        self.add_button = tk.Button(self.parent,
                                    text='Inegi Ekle',command=self.add)
        self.add_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.add_button.place(x=230,y=400)
        
        self.main_menu_button = tk.Button(self.parent, text='Ana Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=470)
        
        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=540  )
        
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
        
        self.family_label.destroy()
        self.family_entry.destroy()
        
        self.add_button.destroy()
        self.main_menu_button.destroy()
        self.exit_button.destroy()
        
    def add(self):
        self.name = self.name_entry.get()
        self.adress = self.adress_entry.get()
        self.phone = self.phone_entry.get()
        self.email = self.email_entry.get()
        self.family = self.family_entry.get()
        
        if len((self.name+self.adress+self.phone+self.email+self.family).strip())==0:
            messagebox.showerror('Inek Defteri','Lutfen bilgileri tamamlayiniz.')
        else:
            
            self.name_entry.delete(0,'end')
            self.adress_entry.delete(0,'end')
            self.phone_entry.delete(0,'end')
            self.email_entry.delete(0,'end')
            self.family_entry.delete(0,'end')
            
            con = sqlite3.connect("inek_defteri.db")
            cursor = con.cursor()
            
            cursor.execute("INSERT INTO inekler VALUES (?,?,?,?,?)",
                           (self.name,self.adress,self.phone,self.email,self.family))
    
            con.commit()
            con.close()
        
            messagebox.showinfo('Inek Defteri','Inek ekleme basarili.')

    def findMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=2
        
        self.find_menu_title = tk.Label(self.parent,text="Inek Bul".upper())
        self.find_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.find_menu_title.place(x=280,y=50)

        # Name

        self.name_label = tk.Label(self.parent,text="Kulak No :  ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 100, y= 150)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230,y=150)
        
        # Found contacts
        
        self.labels = tk.Label(self.parent,text="Kulak No    Dogum    Gebelik    Hastaliklar   Asilar")
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
                                    text='Bul',command=self.find)
        self.find_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.find_button.place(x=230,y=215)
        
        self.main_menu_button = tk.Button(self.parent, text='Ana Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
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
        
        con = sqlite3.connect('inek_defteri.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM inekler WHERE kulakNo=?',(self.name,))
        self.found_people=cursor.fetchall()
        
        self.contact_list.delete(0,'end')
        
        if len(self.found_people)==0:
            messagebox.showinfo('Inek Defteri','Inek bulunamadi.')
        else:
            for person in self.found_people:
                self.contact_list.insert(0,
               str(list(person)[0])+" "+list(person)[1]+" "+list(person)[2]+" "+list(person)[3]+" "+list(person)[4])
            
        con.close()
        
    def deleteMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=3
        
        self.delete_menu_title = tk.Label(self.parent,text="Inek Sil".upper())
        self.delete_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.delete_menu_title.place(x=285,y=50)
        
        # ID

        self.id_label = tk.Label(self.parent,text="Kulak No : ")
        self.id_label.configure(font='Helvetica 18', bg="white")
        self.id_label.place(x= 100, y= 150)

        self.id_entry = tk.Entry(self.parent)
        self.id_entry.configure(font='Helvetica 18', bg="white")
        self.id_entry.place(x=230,y=150)
        
        # Deleted Contacts
        
        self.deleted_contacts_label = tk.Label(self.parent,bg='white')
        self.deleted_contacts_label.place(x=0,y=0)
        
        
        # Buttons
        
        self.delete_button = tk.Button(self.parent,
                                    text='Sil',command=self.delete)
        self.delete_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.delete_button.place(x=230,y=215)
        
        self.main_menu_button = tk.Button(self.parent, text='Ana Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
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
            con=sqlite3.connect('inek_defteri.db')
            cursor = con.cursor()
            
            cursor.execute('SELECT * FROM inekler WHERE kulakNo=?',(self.id,))
            self.found_contact = cursor.fetchall()
            if len(self.found_contact)==0:
                messagebox.showerror('Inek Defteri','Gecersiz Kulak No!')
            else:
                string="Silindi: "+self.found_contact[0][0]+"  "+self.found_contact[0][1]+"  "+self.found_contact[0][2]+"  "+self.found_contact[0][3]+" "+self.found_contact[0][4]
                self.deleted_contacts_label.destroy()
                self.deleted_contacts_label=tk.Label(self.parent,text=string)
                self.deleted_contacts_label.configure(bg='white',font='Helvetica 18')
                self.deleted_contacts_label.place(x=130,y=380)
                cursor.execute('DELETE FROM inekler WHERE kulakNo=?',(self.id,))
                con.commit()
                messagebox.showinfo('Inek Defteri','Inek basariyla silindi.')
            
            con.close()
        else:
            messagebox.showerror('Inek Defteri','Lutfen kulak numarasi giriniz!')

    def updateMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=4
        self.id=-1
        
        
        self.update_menu_title = tk.Label(self.parent,text="Inek Guncelle".upper())
        self.update_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.update_menu_title.place(x=220,y=50)

        # Id
        
        self.id_label = tk.Label(self.parent,text="Kulak No : ")
        self.id_label.configure(font='Helvetica 18', bg="white")
        self.id_label.place(x= 100, y= 150)

        self.id_entry = tk.Entry(self.parent)
        self.id_entry.configure(font='Helvetica 18', bg="white")
        self.id_entry.place(x=230,y=150)
        
        # Name

        self.name_label = tk.Label(self.parent,text="Kulak No : ")
        self.name_label.configure(font='Helvetica 18', bg="white")
        self.name_label.place(x= 100, y= 250)

        self.name_entry = tk.Entry(self.parent)
        self.name_entry.configure(font='Helvetica 18', bg="white")
        self.name_entry.place(x=230,y=250)

        # Adress

        self.adress_label = tk.Label(self.parent,text="Dogum Tarihi : ")
        self.adress_label.configure(font='Helvetica 18', bg="white")
        self.adress_label.place(x= 50, y= 300)

        self.adress_entry = tk.Entry(self.parent)
        self.adress_entry.configure(font='Helvetica 18', bg="white")
        self.adress_entry.place(x=230,y=300)

        # Phone

        self.phone_label = tk.Label(self.parent,text="Gebelik Tarihi : ")
        self.phone_label.configure(font='Helvetica 18', bg="white")
        self.phone_label.place(x= 50, y= 350)

        self.phone_entry = tk.Entry(self.parent)
        self.phone_entry.configure(font='Helvetica 18', bg="white")
        self.phone_entry.place(x=230,y=350)

        # Email

        self.email_label = tk.Label(self.parent,text="Hastaliklar : ")
        self.email_label.configure(font='Helvetica 18', bg="white")
        self.email_label.place(x= 80, y= 400)

        self.email_entry = tk.Entry(self.parent)
        self.email_entry.configure(font='Helvetica 18', bg="white")
        self.email_entry.place(x=230,y=400)
        
        # Family

        self.family_label = tk.Label(self.parent,text="Asilar : ")
        self.family_label.configure(font='Helvetica 18', bg="white")
        self.family_label.place(x= 130, y= 450)

        self.family_entry = tk.Entry(self.parent)
        self.family_entry.configure(font='Helvetica 18', bg="white")
        self.family_entry.place(x=230,y=450)
        
        # Buttons
        
        self.open_contact_button = tk.Button(self.parent,
                                    text='Inegi Ac',command=self.open_contact)
        self.open_contact_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.open_contact_button.place(x=230,y=190)
        
        self.update_button = tk.Button(self.parent,
                                    text='Inegi Guncelle',command=self.update)
        self.update_button.configure(font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.update_button.place(x=230,y=500)
        
        self.main_menu_button = tk.Button(self.parent, text='Ana Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=570)
        
        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
        self.exit_button.configure(font='Helvetica 12',bd=2, bg="white",relief="solid")
        self.exit_button.place(x=330,y=640)
             

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
        
        self.family_label.destroy()
        self.family_entry.destroy()
        
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
        self.family_entry.delete(0,'end')
        
        
        con = sqlite3.connect('inek_defteri.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM inekler WHERE kulakNo=?',(self.id,))
        self.found_people=cursor.fetchall()
        
        if len(self.found_people)==0:
            messagebox.showinfo('Inek Defteri','Gecersiz Kulak Numarasi!')
        else:
            for person in self.found_people:
                self.name_entry.insert(0,person[0])
                self.adress_entry.insert(0,person[1])
                self.phone_entry.insert(0,person[2])
                self.email_entry.insert(0,person[3])
                self.family_entry.insert(0,person[4])
            
        con.close()
    
    def update(self):
        
        self.name=self.name_entry.get()
        self.adress=self.adress_entry.get()
        self.phone=self.phone_entry.get()
        self.email=self.email_entry.get()
        self.family = self.family_entry.get()
        
        con = sqlite3.connect('inek_defteri.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM inekler WHERE kulakNo=?',(self.id,))
        self.found_contact = cursor.fetchall()
        if len(self.found_contact)>0:
            cursor.execute('UPDATE inekler SET kulakNo=?, dogumTarihi=?, gebelikTarihi=?, hastaliklar=?, asilar=? WHERE kulakNo=?',(self.name,self.adress,
                                                                                             self.phone,self.email,
                                                                                             self.family,self.id))
            messagebox.showinfo('Inek Defteri', 'Inek basariyla guncellendi!')
        else:
            messagebox.showerror('Inek Defteri','Gecersiz Kulak Numarasi!')
            
        con.commit()
        con.close()
    
    def listMenu(self):
        self.destroyMainMenu()
        
        self.menu_number=5
        
        self.list_all_menu_title = tk.Label(self.parent,text="Tum inekleri sirala".upper())
        self.list_all_menu_title.configure(font='Helvetica 24 bold', bg="white")
        self.list_all_menu_title.place(x=195,y=50)
        
        # Found contacts
        
        self.labels = tk.Label(self.parent,text="Kulak No    Dogum    Gebelik    Hastaliklar   Asilar")
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
        
        con = sqlite3.connect('inek_defteri.db')
        cursor=con.cursor()
        
        cursor.execute('SELECT * FROM inekler ORDER BY kulakNo DESC')
        self.found_people=cursor.fetchall()
        
        if len(self.found_people)==0:
            messagebox.showinfo('Inek Defteri','Inek Defteri Bos!')
        else:
            for person in self.found_people:
                self.contact_list.insert(0,
               str(list(person)[0])+" "+list(person)[1]+" "+list(person)[2]+" "+list(person)[3]+" "+list(person)[4])
            
        con.close()
        
        # Buttons
        
        self.main_menu_button = tk.Button(self.parent, text='Ana Menu',command =self.add_main_menu)
        self.main_menu_button.configure(
            font='Helvetica 18', bg='white', bd=2, relief='solid',width = 18)
        self.main_menu_button.place(x=230,y=540)
        
        self.exit_button = tk.Button(self.parent,text="Cikis".upper(), command=self.parent.quit)
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
