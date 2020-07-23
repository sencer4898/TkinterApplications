# Interest Calculator

import tkinter as tk
from tkinter import messagebox

class InterestApp():
    
    def hesapla_dondur(self,ana_para,faiz,sene,senelik):
        
        if ana_para<=senelik :
            return ""
        
        else:
            odeme = str(senelik+ana_para*faiz)
            
            current= "\n" + "Sene "+ str(sene)+ " : "+odeme
            
            ana_para=ana_para-senelik
            sene+=1
            
            return current+self.hesapla_dondur(ana_para,faiz,sene,senelik)
    
    def hesapla(self):
        ana_para = int(self.ana_para.get())
        faiz = float(float(self.faiz.get())/100)
        sene = int(self.vade.get())
        
        senelik = int(ana_para/sene)
        
        try:
            faizler_new = 'Senelik Odemeleriniz :' + self.hesapla_dondur(ana_para,faiz,1,senelik)
            messagebox.showinfo('Faiz Uygulamasi',faizler_new)
        except:
            messagebox.showwarning('Faiz Uygulamasi', 'Lutfen gecerli degerler giriniz.')
        
    
    def mainMenu(self):    
        self.root = tk.Tk()
        self.root.title('Faiz Uygulamasi')
        self.root.geometry("300x230")
        self.ana_para_label = tk.Label(self.root,text='Ana Para')
        self.ana_para_label.pack(pady=(8,0))
        
        self.ana_para = tk.Entry(self.root)
        self.ana_para.pack(padx=10,pady=10)
        
        
        self.faiz_label = tk.Label(self.root,text='Faiz')
        self.faiz_label.pack()
        
        self.faiz = tk.Entry(self.root)
        self.faiz.pack(padx=10,pady=10)    
        
        self.vade_label = tk.Label(self.root,text='Sene')
        self.vade_label.pack()
        
        self.vade = tk.Entry(self.root)
        self.vade.pack(padx=10,pady=10)
        
        self.hesap_butonu = tk.Button(self.root,text='Hesapla',command=self.hesapla)
        self.hesap_butonu.pack(pady=5)
    
    
    
        self.root.mainloop()
    
    
    


myApp = InterestApp()
myApp.mainMenu()
