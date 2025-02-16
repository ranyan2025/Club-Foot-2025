from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date, datetime
from crud import inserer_inscrit, lire_inscrits, mettre_a_jour_inscrit, supprimer_inscrit, rechercher_inscrits, \
    inserer_compta, lire_compta

def calculer_age(date_naissance):
    naissance = datetime.strptime(date_naissance, "%d/%m/%Y")
    today = date.today()
    age = today.year - naissance.year - ((today.month, today.day) < (naissance.month, naissance.day))
    return age

def convertir_date_pour_mysql(date_naissance):
    return datetime.strptime(date_naissance, "%d/%m/%Y").strftime("%Y-%m-%d")

def convertir_date_pour_affichage(date_naissance_mysql):
    return datetime.strptime(date_naissance_mysql, "%Y-%m-%d").strftime("%d/%m/%Y")

def ajouter_inscrit():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    email = entry_email.get()
    photo = entry_photo.get()

    try:
        date_naissance_mysql = convertir_date_pour_mysql(date_naissance)
    except ValueError:
        messagebox.showerror("Erreur", "Date de naissance invalide. Utilisez le format jj/mm/aaaa.")
        return

    age = calculer_age(date_naissance)
    inserer_inscrit(nom, prenom, age, email, photo, date_naissance_mysql)
    messagebox.showinfo("Succès", "Inscrit ajouté avec succès")
    afficher_inscrits()

def afficher_inscrits():
    inscrits = lire_inscrits()
    for item in tree.get_children():
        tree.delete(item)
    for inscrit in inscrits:
        tree.insert("", "end", values=inscrit)

def afficher_tous_inscrits():
    afficher_inscrits()

def remplir_formulaire(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, "values")
    entry_id.delete(0, END)
    entry_id.insert(0, values[0])
    entry_nom.delete(0, END)
    entry_nom.insert(0, values[1])
    entry_prenom.delete(0, END)
    entry_prenom.insert(0, values[2])
    entry_email.delete(0, END)
    entry_email.insert(0, values[4])
    entry_photo.delete(0, END)
    entry_photo.insert(0, values[5])

    if len(values) >= 7 and values[6]:
        date_naissance = convertir_date_pour_affichage(values[6])
        entry_date_naissance.delete(0, END)
        entry_date_naissance.insert(0, date_naissance)

        age = calculer_age(date_naissance)
        entry_age.delete(0, END)
        entry_age.insert(0, str(age))
    else:
        entry_date_naissance.delete(0, END)
        entry_age.delete(0, END)
        entry_age.insert(0, "N/A")

    afficher_photo(values[5])

def afficher_photo(photo_path):
    try:
        img = Image.open(photo_path)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        canvas.delete("all")
        canvas.config(width=img.width, height=img.height)
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo
    except Exception as e:
        print(f"Erreur lors de l'affichage de la photo : {e}")

def choisir_photo():
    filename = filedialog.askopenfilename(title="Sélectionner une photo",
                                          filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if filename:
        entry_photo.delete(0, END)
        entry_photo.insert(0, filename)
        afficher_photo(filename)

def mettre_a_jour():
    id = entry_id.get()
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    email = entry_email.get()
    photo = entry_photo.get()

    try:
        date_naissance_mysql = convertir_date_pour_mysql(date_naissance)
    except ValueError:
        messagebox.showerror("Erreur", "Date de naissance invalide. Utilisez le format jj/mm/aaaa.")
        return

    age = calculer_age(date_naissance)
    mettre_a_jour_inscrit(id, nom, prenom, age, email, photo, date_naissance_mysql)
    messagebox.showinfo("Succès", "Inscrit mis à jour avec succès")
    afficher_inscrits()

def supprimer():
    id = entry_id.get()
    supprimer_inscrit(id)
    messagebox.showinfo("Succès", "Inscrit supprimé avec succès")
    afficher_inscrits()

def nouveau_inscrit():
    entry_id.delete(0, END)
    entry_nom.delete(0, END)
    entry_prenom.delete(0, END)
    entry_date_naissance.delete(0, END)
    entry_email.delete(0, END)
    entry_photo.delete(0, END)
    entry_age.delete(0, END)
    canvas.delete("all")

def rechercher():
    critere = entry_nom.get()  # Récupérer le nom depuis entry_nom
    if not critere:
        critere = entry_id.get()  # Si entry_nom est vide, récupérer l'ID depuis entry_id

    if critere:
        afficher_resultats_recherche(critere)
    else:
        messagebox.showinfo("Info", "Veuillez entrer un critère de recherche")

def afficher_resultats_recherche(critere):
    inscrits = rechercher_inscrits(critere)
    for item in tree.get_children():
        tree.delete(item)
    for inscrit in inscrits:
        tree.insert("", "end", values=inscrit)


app = Tk()
app.title("Gestion des inscrits du club de foot")
app.config(bg="green")

#app.state("zoomed")
#app.attributes('-zoomed', True)


label_titre = Label(app, text="GESTION DU CLUB FOOTBALL", font=("Helvetica", 24, "bold"))
label_titre.pack(pady=10)

frame_form = Frame(app)
frame_form.pack(pady=10)

Label(frame_form, text="ID", font=("Helvetica", 12, "italic", "bold")).grid(row=0, column=0)
entry_id = Entry(frame_form)
entry_id.grid(row=0, column=1)

Label(frame_form, text="Nom", font=("Helvetica", 12, "italic", "bold")).grid(row=1, column=0)
entry_nom = Entry(frame_form)
entry_nom.grid(row=1, column=1)

# Canvas for displaying the photo
canvas = Canvas(frame_form, width=100, height=100)
canvas.grid(row=1, column=2, rowspan=5, padx=10)

Label(frame_form, text="Prénom", font=("Helvetica", 12, "italic", "bold")).grid(row=2, column=0)
entry_prenom = Entry(frame_form)
entry_prenom.grid(row=2, column=1)

Label(frame_form, text="Date de naissance (jj/mm/aaaa)", font=("Helvetica", 12, "italic", "bold")).grid(row=3, column=0)
entry_date_naissance = Entry(frame_form)
entry_date_naissance.grid(row=3, column=1)

Label(frame_form, text="Âge", font=("Helvetica", 12, "italic", "bold")).grid(row=4, column=0)
entry_age = Entry(frame_form)
entry_age.grid(row=4, column=1)

Label(frame_form, text="Tel Parents", font=("Helvetica", 12, "italic", "bold")).grid(row=5, column=0)
entry_email = Entry(frame_form)
entry_email.grid(row=5, column=1)

Label(frame_form, text="Photo", font=("Helvetica", 12, "italic", "bold")).grid(row=6, column=0)
entry_photo = Entry(frame_form)
entry_photo.grid(row=6, column=1)
Button(frame_form, text="Choisir une photo", font=("Helvetica", 12, "italic", "bold"), command=choisir_photo).grid(row=6, column=2, padx=5)

frame_buttons = Frame(app)
frame_buttons.pack(pady=10)

btn_ajouter = Button(frame_buttons, text="Enregistrer", font=("Helvetica", 12, "italic", "bold"), command=ajouter_inscrit)
btn_ajouter.grid(row=0, column=1, padx=5)

btn_mettre_a_jour = Button(frame_buttons, text="Mettre à jour", font=("Helvetica", 12, "italic", "bold"), command=mettre_a_jour)
btn_mettre_a_jour.grid(row=0, column=5, padx=5)

btn_supprimer = Button(frame_buttons, text="Supprimer", font=("Helvetica", 12, "italic", "bold"), command=supprimer)
btn_supprimer.grid(row=0, column=2, padx=5)

btn_nouveau = Button(frame_buttons, text="Nouveau", font=("Helvetica", 12, "italic", "bold"), command=nouveau_inscrit)
btn_nouveau.grid(row=0, column=0, padx=5)

btn_afficher_tous = Button(frame_buttons, text="Afficher tous", font=("Helvetica", 12, "italic", "bold"), command=afficher_tous_inscrits)
btn_afficher_tous.grid(row=0, column=4, padx=5)

btn_rechercher = Button(frame_form, text="Rechercher par ID ou NOM", font=("Helvetica", 12, "italic", "bold"), command=rechercher)
btn_rechercher.grid(row=0, column=2, padx=5)

btn_rechercher = Button(frame_form, text="Nouvelle Rechercher", font=("Helvetica", 12, "italic", "bold"), command=nouveau_inscrit)
btn_rechercher.grid(row=0, column=3, padx=5)

btn_quitter = Button(frame_buttons, text="Quitter", font=("Helvetica", 12, "italic", "bold"), command=quit)
btn_quitter.grid(row=0, column=7, padx=5)


tree = ttk.Treeview(app, columns=("id", "nom", "prenom", "age", "email", "photo", "date_naissance"), show="headings")
tree.heading("id", text="ID")
tree.heading("nom", text="Nom")
tree.heading("prenom", text="Prénom")
tree.heading("age", text="Âge")
tree.heading("email", text="Email")
tree.heading("photo", text="Photo")
tree.heading("date_naissance", text="Date de naissance")
tree.pack(pady=10)
tree.bind("<ButtonRelease-1>", remplir_formulaire)

afficher_inscrits()

def ouvrir_compta(id, nom, prenom):
    global selected_inscrit_id
    selected_inscrit_id = id  # Stocker l'ID de l'inscrit sélectionné

    compta_window = Toplevel(app)
    compta_window.state("zoomed")

    compta_window.title("Gestion de la Comptabilité pour {} {}".format(nom, prenom))

    Label(compta_window, text="ID Inscrit :").grid(row=0, column=0)
    entry_id = Entry(compta_window)
    Label(compta_window, text=id).grid(row=0, column=1)

    Label(compta_window, text="Nom :").grid(row=1, column=0)
    entry_nom = Entry(compta_window)
    Label(compta_window, text=nom).grid(row=1, column=1)

    Label(compta_window, text="Prénom :").grid(row=2, column=0)
    entry_prenom = Entry(compta_window)
    Label(compta_window, text=prenom).grid(row=2, column=1)

    Label(compta_window, text="Mensualité :").grid(row=3, column=0, padx=10, pady=5)
    entry_mensualite = Entry(compta_window)
    entry_mensualite.grid(row=3, column=1, padx=10, pady=5)

    Label(compta_window, text="Date du paiement (jj/mm/aaaa) :").grid(row=4, column=0, padx=10, pady=5)
    entry_date_paiement = Entry(compta_window)
    entry_date_paiement.grid(row=4, column=1, padx=10, pady=5)

    Label(compta_window, text="Mois payé:").grid(row=5, column=0, padx=10, pady=5)
    mois_list = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    combo_mois_paye = ttk.Combobox(compta_window, values=mois_list)
    combo_mois_paye.grid(row=5, column=1, padx=10, pady=5)

    Label(compta_window, text="Moyen de paiement :").grid(row=6, column=0, padx=10, pady=5)
    moyen_paiement_var = StringVar()  # Variable pour stocker le moyen de paiement sélectionné
    combo_moyen_paiement = ttk.Combobox(compta_window, values=['espece', 'cheque', 'virement'])
    combo_moyen_paiement.grid(row=6, column=1, padx=10, pady=5)

    Label(compta_window, text="Retard de paiement :").grid(row=7, column=0, padx=10, pady=5)
    retard_paiement_var = IntVar()
    check_retard_paiement = ttk.Checkbutton(compta_window, variable=retard_paiement_var)
    check_retard_paiement.grid(row=7, column=1, padx=10, pady=5)

    Label(compta_window, text="Alerte :").grid(row=8, column=0, padx=10, pady=5)
    alerte_var = IntVar()
    check_alerte = ttk.Checkbutton(compta_window, variable=alerte_var)
    check_alerte.grid(row=8, column=1, padx=10, pady=5)

    # Bouton pour enregistrer les informations de comptabilité


    def enregistrer_compta():
        # Récupérer les valeurs des champs
        mensualite = entry_mensualite.get()
        date_paiement = entry_date_paiement.get()
        mois_paye = combo_mois_paye.get()
        moyen_paiement = combo_moyen_paiement.get()
        retard_paiement = check_retard_paiement.instate(['selected'])
        alerte = check_alerte.instate(['selected'])

        # Assurez-vous que l'id_inscrit est correctement passé à la fonction
        id_inscrit = selected_inscrit_id  # Utilisez la variable globale selected_inscrit_id

        # Insérer dans la table compta
        if mensualite and date_paiement and mois_paye and moyen_paiement:
            try:
                date_paiement_mysql = convertir_date_pour_mysql(date_paiement)
            except ValueError:
                messagebox.showerror("Erreur", "Date de paiement invalide. Utilisez le format jj/mm/aaaa.")
                return

            if inserer_compta(id_inscrit, nom, prenom, mensualite, date_paiement_mysql, mois_paye, moyen_paiement,
                              retard_paiement, alerte):
                messagebox.showinfo("Succès", "Données de comptabilité enregistrées avec succès.")
            else:
                messagebox.showerror("Erreur", "Échec de l'enregistrement des données de comptabilité.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")

    # Supprimez les arguments de la fonction enregistrer_compta pour éviter l'erreur de trop d'arguments

    # Bouton Enregistrer
    btn_enregistrer = Button(compta_window, text="Enregistrer", command=enregistrer_compta)
    btn_enregistrer.grid(row=9, column=0, columnspan=2, pady=10)

    btn_quitter = Button(compta_window, text="Quitter", command=quit)
    btn_quitter.grid(row=10, column=0, columnspan=2, pady=10)

    def afficher_compta():
        compta = lire_compta()
        for item in tree_compta.get_children():
            tree_compta.delete(item)
        for ligne in compta:
            tree_compta.insert("", "end", values=ligne)

    # Afficher la comptabilité existante dans un Treeview
    tree_compta = ttk.Treeview(compta_window, columns=("ID Inscrit", "Nom", "Prénom", "Mensualité", "Date de Paiement", "Mois Payé", "Moyen de Paiement",
    "Retard de Paiement", "Alerte"), show='headings')
    tree_compta.heading("ID Inscrit", text="ID Inscrit")
    tree_compta.heading("Nom", text="Nom")
    tree_compta.heading("Prénom", text="Prénom")
    tree_compta.heading("Mensualité", text="Mensualité")
    tree_compta.heading("Date de Paiement", text="Date de Paiement")
    tree_compta.heading("Mois Payé", text="Mois Payé")
    tree_compta.heading("Moyen de Paiement", text="Moyen de Paiement")
    tree_compta.heading("Retard de Paiement", text="Retard de Paiement")
    tree_compta.heading("Alerte", text="Alerte")

    tree_compta.grid(row=14, column=0, columnspan=6, pady=10)

    afficher_compta()

    def remplir_formulaire_compta(event):
        selected_item = tree_compta.selection()[0]
        values = tree_compta.item(selected_item, "values")
        entry_mensualite.delete(0, END)
        entry_mensualite.insert(0, values[4])
        entry_date_paiement.delete(0, END)
        entry_date_paiement.insert(0, values[5])
        combo_mois_paye.delete(0, END)
        combo_mois_paye.set(values[6])
        combo_moyen_paiement.set(values[7])
        if values[8]:
            check_retard_paiement.state(['selected'])
        else:
            check_retard_paiement.state(['!selected'])
        if values[9]:
            check_alerte.state(['selected'])
        else:
            check_alerte.state(['!selected'])

    # Lier la fonction à l'événement de clic sur une ligne dans ttk.Treeview pour la comptabilité
    tree_compta.bind("<ButtonRelease-1>", remplir_formulaire_compta)

    def supprimer():
        id_inscrit = entry_id.get()
        supprimer_inscrit(id_inscrit)
        messagebox.showinfo("Succès", "Inscrit supprimé avec succès")
        afficher_compta()

    btn_supprimer = Button(compta_window, text="Supprimer", command=supprimer)
    btn_supprimer.grid(row=0, column=2, padx=5)
    

# Fonction pour ouvrir la fenêtre de comptabilité avec les informations de l'inscrit sélectionné
def open_compta_window():
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")
        id_inscrit = values[0]
        nom = values[1]
        prenom = values[2]
        ouvrir_compta(id_inscrit, nom, prenom)
    else:
        messagebox.showinfo("Information", "Veuillez sélectionner un inscrit pour accéder à la comptabilité.")

# Button for Compta
btn_compta = Button(frame_buttons, text="Compta", font=("Helvetica", 12, "italic", "bold"), command=open_compta_window)
btn_compta.grid(row=0, column=6, padx=5)




app.mainloop()
