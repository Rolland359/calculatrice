# -*- coding : "utf-8" -*-
from tkinter import *
from tkinter import messagebox

class Calculatrice:
    """simple calculatrice avec tkinter """


    def __init__(self):
        
        self.fenetre = Tk()
        self.fenetre.title("calculatrice")
        self.evaluation = StringVar()
        self.champ = Entry(self.fenetre, textvariable=self.evaluation, borderwidth=2)
        self.champ.bind('<Return>', self.bouton_evaluer_bind)

        #création des bouton :
        self.bouton_1 = Button(self.fenetre, text="1", width=5, height=3, command=lambda : self.bouton_click("1") )
        self.bouton_2 = Button(self.fenetre, text="2", width=5, height=3,command=lambda : self.bouton_click("2") )
        self.bouton_3 = Button(self.fenetre, text="3", width=5, height=3,command=lambda : self.bouton_click("3") )

        self.bouton_4 = Button(self.fenetre, text="4", width=5, height=3,command=lambda : self.bouton_click("4") )
        self.bouton_5 = Button(self.fenetre, text="5", width=5, height=3,command=lambda : self.bouton_click("5") )
        self.bouton_6 = Button(self.fenetre, text="6", width=5, height=3,command=lambda : self.bouton_click("6") )

        self.bouton_7 = Button(self.fenetre, text="7", width=5, height=3,command=lambda : self.bouton_click("7") )
        self.bouton_8 = Button(self.fenetre, text="8", width=5, height=3,command=lambda : self.bouton_click("8") )
        self.bouton_9 = Button(self.fenetre, text="9", width=5, height=3,command=lambda : self.bouton_click("9") )

        self.bouton_add = Button(self.fenetre, text="+", width=5, height=7,command=lambda : self.bouton_click("+") )
        self.bouton_min = Button(self.fenetre, text="-", width=5, height=3,command=lambda : self.bouton_click("-") )
        self.bouton_prod = Button(self.fenetre, text="*", width=5, height=3,command=lambda : self.bouton_click("*") )
        self.bouton_div = Button(self.fenetre, text="/", width=5, height=3,command=lambda : self.bouton_click("/") )

        self.bouton_equ = Button(self.fenetre, text="=", width=5, height=6,command=self.bouton_evaluer )
        self.bouton_zero = Button(self.fenetre, text="0", width=12, height=2,command=lambda : self.bouton_click("0") )
        self.bouton_virg = Button(self.fenetre, text=".", width=5, height=2,command=lambda : self.bouton_click(",") )

        self.bouton_del = Button(self.fenetre, text="DEL", width=5, height=3,command=self.bouton_netoye )


        # mapper les boutons :
        self.bouton_1.grid(padx=2, pady=2, row=4, column=0)
        self.bouton_2.grid(padx=2, pady=2, row=4, column=1)
        self.bouton_3.grid(padx=2, pady=2, row=4, column=2)

        self.bouton_4.grid(padx=2, pady=2, row=3, column=0)
        self.bouton_5.grid(padx=2, pady=2, row=3, column=1)
        self.bouton_6.grid(padx=2, pady=2, row=3, column=2)

        self.bouton_7.grid(padx=2, pady=2, row=2, column=0)
        self.bouton_8.grid(padx=2, pady=2, row=2, column=1)
        self.bouton_9.grid(padx=2, pady=2, row=2, column=2)

        self.bouton_min.grid(padx=2, pady=2, row=1, column=1)
        self.bouton_prod.grid(padx=2, pady=2, row=1, column=2)
        self.bouton_div.grid(padx=2, pady=2, row=1, column=3)

        self.bouton_add.grid(padx=2, pady=2, row=2, column=3,rowspan=2)
        self.bouton_equ.grid(padx=2, pady=2, row=4, column=3, rowspan=2)
        self.bouton_zero.grid(padx=2, pady=2, row=5, column=0,columnspan=2)
        self.bouton_virg.grid(padx=2, pady=2, row=5, column=2)

        self.bouton_del.grid(padx=2, pady=2, row=1, column=0)
        self.champ.grid(padx=2,pady=2,row=0,column=0,columnspan=4)


        self.fenetre.mainloop()
        
    def bouton_click(self, texte):
        self.evaluation.set(self.evaluation.get()+str(texte))

    def bouton_netoye(self):
        self.champ.delete(0, END)
        # messagebox.showinfo("Delete", "vous avez nettoyer l'entre")
    
    def bouton_evaluer(self):
        expression = self.evaluation.get()
        try :
            self.evaluation.set(f"{expression} = {eval(expression)}")
        
        except ZeroDivisionError:
            messagebox.showwarning("Attention", "Ne peut pas diviser par zéro")
        except NameError:
            messagebox.showerror("Erreur","Veuillez entrer des chiffres valides...")        
        except SyntaxError:
            messagebox.showerror("Erreur","Veuillez entrer des chiffres valides...")
        # messagebox.showinfo("titre",f"resultat: {eval(self.champ.get())}")
    
    def bouton_evaluer_bind(self, event):
        try:
            self.evaluation.set(f"{self.evaluation.get()} = {eval(self.champ.get())}")
        except ZeroDivisionError:
            messagebox.showwarning("Attention", "Ne peut pas diviser par zéro")
        except NameError:
            messagebox.showerror("Erreur","Veuillez entrer des chiffres valides...")
        except SyntaxError:
            messagebox.showerror("Erreur","Veuillez entrer des chiffres valides...")

if __name__ == '__main__':
    Calculatrice()