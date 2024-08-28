import tkinter as tk
from tkinter import filedialog, messagebox

class InspectionForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inspection de l'éclairage et du vitrage")
        self.geometry("600x800")  # Fixe une taille initiale

        # Création du cadre principal avec barre de défilement
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bouton pour afficher/masquer la section Capot
        self.capot_button = tk.Button(self.scrollable_frame, text="Capot", command=self.toggle_capot_section)
        self.capot_button.pack(fill="x", padx=10, pady=5)

        # Section Capot (initialement masquée)
        self.capot_frame = tk.LabelFrame(self.scrollable_frame, text="Capot")
        self.capot_visible = False

        self.corrosion_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Corrosion ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.corrosion_var, value="OUI", command=self.toggle_corrosion).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.corrosion_var, value="NON", command=self.toggle_corrosion).pack(anchor="w")

        self.multiple_corrosion_var = tk.StringVar(value="NON")
        self.photo_corrosion_button = tk.Button(self.capot_frame, text="Prenez une photo de la trace de corrosion", command=self.upload_corrosion_photo, state="disabled")
        self.photo_corrosion_button.pack(anchor="w")
        tk.Label(self.capot_frame, text="Y a t’il plusieurs traces de corrosion ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.multiple_corrosion_var, value="OUI", command=self.toggle_multiple_corrosion).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.multiple_corrosion_var, value="NON", command=self.toggle_multiple_corrosion).pack(anchor="w")
        
        self.photo_second_corrosion_button = tk.Button(self.capot_frame, text="Prenez une photo de la deuxième trace de corrosion", command=self.upload_second_corrosion_photo, state="disabled")
        self.photo_second_corrosion_button.pack(anchor="w")

        self.rayure_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Rayure ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.rayure_var, value="OUI", command=self.toggle_rayure).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.rayure_var, value="NON", command=self.toggle_rayure).pack(anchor="w")

        self.multiple_rayure_var = tk.StringVar(value="NON")
        self.photo_rayure_button = tk.Button(self.capot_frame, text="Prenez une photo de la rayure", command=self.upload_rayure_photo, state="disabled")
        self.photo_rayure_button.pack(anchor="w")
        tk.Label(self.capot_frame, text="Y a t’il plusieurs rayures ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.multiple_rayure_var, value="OUI", command=self.toggle_multiple_rayure).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.multiple_rayure_var, value="NON", command=self.toggle_multiple_rayure).pack(anchor="w")
        
        self.photo_second_rayure_button = tk.Button(self.capot_frame, text="Prenez une photo de la deuxième rayure", command=self.upload_second_rayure_photo, state="disabled")
        self.photo_second_rayure_button.pack(anchor="w")

        self.impact_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Impact ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.impact_var, value="OUI", command=self.toggle_impact).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.impact_var, value="NON", command=self.toggle_impact).pack(anchor="w")

        self.multiple_impact_var = tk.StringVar(value="NON")
        self.photo_impact_button = tk.Button(self.capot_frame, text="Prenez une photo de l'impact", command=self.upload_impact_photo, state="disabled")
        self.photo_impact_button.pack(anchor="w")
        tk.Label(self.capot_frame, text="Y a t’il plusieurs impacts ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.multiple_impact_var, value="OUI", command=self.toggle_multiple_impact).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.multiple_impact_var, value="NON", command=self.toggle_multiple_impact).pack(anchor="w")
        
        self.photo_second_impact_button = tk.Button(self.capot_frame, text="Prenez une photo du deuxième impact", command=self.upload_second_impact_photo, state="disabled")
        self.photo_second_impact_button.pack(anchor="w")

        self.defaut_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Défaut de peinture ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.defaut_var, value="OUI", command=self.toggle_defaut).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.defaut_var, value="NON", command=self.toggle_defaut).pack(anchor="w")

        self.multiple_defaut_var = tk.StringVar(value="NON")
        self.photo_defaut_button = tk.Button(self.capot_frame, text="Prenez une photo du défaut de peinture", command=self.upload_defaut_photo, state="disabled")
        self.photo_defaut_button.pack(anchor="w")
        tk.Label(self.capot_frame, text="Y a t’il plusieurs défauts de peinture ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.multiple_defaut_var, value="OUI", command=self.toggle_multiple_defaut).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.multiple_defaut_var, value="NON", command=self.toggle_multiple_defaut).pack(anchor="w")
        
        self.photo_second_defaut_button = tk.Button(self.capot_frame, text="Prenez une photo du deuxième défaut de peinture", command=self.upload_second_defaut_photo, state="disabled")
        self.photo_second_defaut_button.pack(anchor="w")

        self.alignment_defect_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Défaut d’alignement du capot ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.alignment_defect_var, value="OUI", command=self.toggle_alignment_defect).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.alignment_defect_var, value="NON", command=self.toggle_alignment_defect).pack(anchor="w")

        self.photo_alignment_defect_button = tk.Button(self.capot_frame, text="Prenez une photo du défaut d'alignement", command=self.upload_alignment_defect_photo, state="disabled")
        self.photo_alignment_defect_button.pack(anchor="w")

        self.other_defect_var = tk.StringVar(value="NON")
        tk.Label(self.capot_frame, text="Autre défaut ?").pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="OUI", variable=self.other_defect_var, value="OUI", command=self.toggle_other_defect).pack(anchor="w")
        tk.Radiobutton(self.capot_frame, text="NON", variable=self.other_defect_var, value="NON", command=self.toggle_other_defect).pack(anchor="w")

        self.other_defect_description = tk.Entry(self.capot_frame, width=50, state="disabled")
        self.other_defect_description.pack(anchor="w")
        self.photo_other_defect_button = tk.Button(self.capot_frame, text="Prenez une photo du défaut supplémentaire", command=self.upload_other_defect_photo, state="disabled")
        self.photo_other_defect_button.pack(anchor="w")

        tk.Label(self.capot_frame, text="Évaluez l’état visuel général du capot de 1 à 5 ?").pack(anchor="w")
        self.capot_condition = tk.Scale(self.capot_frame, from_=1, to=5, orient=tk.HORIZONTAL)
        self.capot_condition.pack(anchor="w")

        self.photo_capot_complete_button = tk.Button(self.capot_frame, text="Prenez une photo du capot complet", command=self.upload_capot_complete_photo)
        self.photo_capot_complete_button.pack(anchor="w")

                # Bouton pour afficher/masquer la section Parechoc
        self.parechoc_button = tk.Button(self.scrollable_frame, text="Parechoc", command=self.toggle_parechoc_section)
        self.parechoc_button.pack(fill="x", padx=10, pady=5)

        # Section Parechoc (initialement masquée)
        self.parechoc_frame = tk.LabelFrame(self.scrollable_frame, text="Parechoc")
        self.parechoc_visible = False

        self.parechoc_corrosion_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Corrosion ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_corrosion_var, value="OUI", command=self.toggle_parechoc_corrosion).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_corrosion_var, value="NON", command=self.toggle_parechoc_corrosion).pack(anchor="w")

        self.parechoc_photo_corrosion_button = tk.Button(self.parechoc_frame, text="Prenez une photo de la trace de corrosion", command=self.upload_parechoc_corrosion_photo, state="disabled")
        self.parechoc_photo_corrosion_button.pack(anchor="w")

        self.parechoc_multiple_corrosion_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Y a-t-il plusieurs traces de corrosion ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_multiple_corrosion_var, value="OUI", command=self.toggle_parechoc_multiple_corrosion).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_multiple_corrosion_var, value="NON", command=self.toggle_parechoc_multiple_corrosion).pack(anchor="w")

        self.parechoc_photo_second_corrosion_button = tk.Button(self.parechoc_frame, text="Prenez une photo de la deuxième trace de corrosion", command=self.upload_parechoc_second_corrosion_photo, state="disabled")
        self.parechoc_photo_second_corrosion_button.pack(anchor="w")

        self.parechoc_rayure_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Rayure ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_rayure_var, value="OUI", command=self.toggle_parechoc_rayure).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_rayure_var, value="NON", command=self.toggle_parechoc_rayure).pack(anchor="w")

        self.parechoc_photo_rayure_button = tk.Button(self.parechoc_frame, text="Prenez une photo de la rayure", command=self.upload_parechoc_rayure_photo, state="disabled")
        self.parechoc_photo_rayure_button.pack(anchor="w")

        self.parechoc_multiple_rayure_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Y a-t-il plusieurs rayures ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_multiple_rayure_var, value="OUI", command=self.toggle_parechoc_multiple_rayure).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_multiple_rayure_var, value="NON", command=self.toggle_parechoc_multiple_rayure).pack(anchor="w")

        self.parechoc_photo_second_rayure_button = tk.Button(self.parechoc_frame, text="Prenez une photo de la deuxième rayure", command=self.upload_parechoc_second_rayure_photo, state="disabled")
        self.parechoc_photo_second_rayure_button.pack(anchor="w")

        self.parechoc_impact_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Impact ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_impact_var, value="OUI", command=self.toggle_parechoc_impact).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_impact_var, value="NON", command=self.toggle_parechoc_impact).pack(anchor="w")

        self.parechoc_photo_impact_button = tk.Button(self.parechoc_frame, text="Prenez une photo de l'impact", command=self.upload_parechoc_impact_photo, state="disabled")
        self.parechoc_photo_impact_button.pack(anchor="w")
        
        self.parechoc_multiple_impact_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Y a-t-il plusieurs impacts ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_multiple_impact_var, value="OUI", command=self.toggle_parechoc_multiple_impact).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_multiple_impact_var, value="NON", command=self.toggle_parechoc_multiple_impact).pack(anchor="w")
        
        self.parechoc_photo_second_impact_button = tk.Button(self.parechoc_frame, text="Prenez une photo du deuxième impact", command=self.upload_parechoc_second_impact_photo, state="disabled")
        self.parechoc_photo_second_impact_button.pack(anchor="w")

        self.parechoc_defaut_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Défaut de peinture ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_defaut_var, value="OUI", command=self.toggle_parechoc_defaut).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_defaut_var, value="NON", command=self.toggle_parechoc_defaut).pack(anchor="w")

        self.parechoc_photo_defaut_button = tk.Button(self.parechoc_frame, text="Prenez une photo du défaut de peinture", command=self.upload_parechoc_defaut_photo, state="disabled")
        self.parechoc_photo_defaut_button.pack(anchor="w")

        self.parechoc_multiple_defaut_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Y a-t-il plusieurs défauts de peinture ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_multiple_defaut_var, value="OUI", command=self.toggle_parechoc_multiple_defaut).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_multiple_defaut_var, value="NON", command=self.toggle_parechoc_multiple_defaut).pack(anchor="w")

        self.parechoc_photo_second_defaut_button = tk.Button(self.parechoc_frame, text="Prenez une photo du deuxième défaut de peinture", command=self.upload_parechoc_second_defaut_photo, state="disabled")
        self.parechoc_photo_second_defaut_button.pack(anchor="w")

        self.parechoc_alignment_defect_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Défaut d’alignement du parechoc ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_alignment_defect_var, value="OUI", command=self.toggle_parechoc_alignment_defect).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_alignment_defect_var, value="NON", command=self.toggle_parechoc_alignment_defect).pack(anchor="w")

        self.parechoc_photo_alignment_defect_button = tk.Button(self.parechoc_frame, text="Prenez une photo du défaut d'alignement", command=self.upload_parechoc_alignment_defect_photo, state="disabled")
        self.parechoc_photo_alignment_defect_button.pack(anchor="w")

        self.parechoc_other_defect_var = tk.StringVar(value="NON")
        tk.Label(self.parechoc_frame, text="Autre défaut ?").pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="OUI", variable=self.parechoc_other_defect_var, value="OUI", command=self.toggle_parechoc_other_defect).pack(anchor="w")
        tk.Radiobutton(self.parechoc_frame, text="NON", variable=self.parechoc_other_defect_var, value="NON", command=self.toggle_parechoc_other_defect).pack(anchor="w")

        self.parechoc_other_defect_description = tk.Entry(self.parechoc_frame, width=50, state="disabled")
        self.parechoc_other_defect_description.pack(anchor="w")

        self.parechoc_photo_other_defect_button = tk.Button(self.parechoc_frame, text="Prenez une photo du défaut supplémentaire", command=self.upload_parechoc_other_defect_photo, state="disabled")
        self.parechoc_photo_other_defect_button.pack(anchor="w")

        tk.Label(self.parechoc_frame, text="Évaluez l’état visuel général du parechoc de 1 à 5 ?").pack(anchor="w")
        self.parechoc_condition = tk.Scale(self.parechoc_frame, from_=1, to=5, orient=tk.HORIZONTAL)
        self.parechoc_condition.pack(anchor="w")

        self.parechoc_photo_complete_button = tk.Button(self.parechoc_frame, text="Prenez une photo du parechoc complet", command=self.upload_parechoc_complete_photo)
        self.parechoc_photo_complete_button.pack(anchor="w")


        # Bouton de soumission
        self.submit_button = tk.Button(self.scrollable_frame, text="Soumettre", command=self.submit)
        self.submit_button.pack(pady=10)

    # Méthodes pour afficher/masquer les sections

    def toggle_capot_section(self):
        if self.capot_visible:
            self.capot_frame.pack_forget()
        else:
            self.capot_frame.pack(fill="both", expand="yes", padx=10, pady=10, after=self.capot_button)
        self.capot_visible = not self.capot_visible

    def toggle_parechoc_section(self):
        if self.parechoc_visible:
            self.parechoc_frame.pack_forget()
        else:
            self.parechoc_frame.pack(fill="both", expand="yes", padx=10, pady=10, after=self.parechoc_button)
        self.parechoc_visible = not self.parechoc_visible

    # Les autres méthodes restent inchangées

    def toggle_corrosion(self):
        if self.corrosion_var.get() == "OUI":
            self.photo_corrosion_button.config(state="normal")
        else:
            self.photo_corrosion_button.config(state="disabled")

    def toggle_multiple_corrosion(self):
        if self.multiple_corrosion_var.get() == "OUI":
            self.photo_second_corrosion_button.config(state="normal")
        else:
            self.photo_second_corrosion_button.config(state="disabled")

    def toggle_rayure(self):
        if self.rayure_var.get() == "OUI":
            self.photo_rayure_button.config(state="normal")
        else:
            self.photo_rayure_button.config(state="disabled")

    def toggle_multiple_rayure(self):
        if self.multiple_rayure_var.get() == "OUI":
            self.photo_second_rayure_button.config(state="normal")
        else:
            self.photo_second_rayure_button.config(state="disabled")

    def toggle_impact(self):
        if self.impact_var.get() == "OUI":
            self.photo_impact_button.config(state="normal")
        else:
            self.photo_impact_button.config(state="disabled")

    def toggle_multiple_impact(self):
        if self.multiple_impact_var.get() == "OUI":
            self.photo_second_impact_button.config(state="normal")
        else:
            self.photo_second_impact_button.config(state="disabled")

    def toggle_defaut(self):
        if self.defaut_var.get() == "OUI":
            self.photo_defaut_button.config(state="normal")
        else:
            self.photo_defaut_button.config(state="disabled")

    def toggle_multiple_defaut(self):
        if self.multiple_defaut_var.get() == "OUI":
            self.photo_second_defaut_button.config(state="normal")
        else:
            self.photo_second_defaut_button.config(state="disabled")

    def toggle_alignment_defect(self):
        if self.alignment_defect_var.get() == "OUI":
            self.photo_alignment_defect_button.config(state="normal")
        else:
            self.photo_alignment_defect_button.config(state="disabled")

    def toggle_other_defect(self):
        if self.other_defect_var.get() == "OUI":
            self.other_defect_description.config(state="normal")
            self.photo_other_defect_button.config(state="normal")
        else:
            self.other_defect_description.config(state="disabled")
            self.photo_other_defect_button.config(state="disabled")

    def upload_corrosion_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_second_corrosion_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_rayure_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_second_rayure_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_impact_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_second_impact_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_defaut_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_second_defaut_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_alignment_defect_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_other_defect_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_capot_complete_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    
    def toggle_parechoc_corrosion(self):
        if self.parechoc_corrosion_var.get() == "OUI":
            self.parechoc_photo_corrosion_button.config(state="normal")
        else:
            self.parechoc_photo_corrosion_button.config(state="disabled")

    def toggle_parechoc_multiple_corrosion(self):
        if self.parechoc_multiple_corrosion_var.get() == "OUI":
            self.parechoc_photo_second_corrosion_button.config(state="normal")
        else:
            self.parechoc_photo_second_corrosion_button.config(state="disabled")

    def toggle_parechoc_rayure(self):
        if self.parechoc_rayure_var.get() == "OUI":
            self.parechoc_photo_rayure_button.config(state="normal")
        else:
            self.parechoc_photo_rayure_button.config(state="disabled")

    def toggle_parechoc_multiple_rayure(self):
        if self.parechoc_multiple_rayure_var.get() == "OUI":
            self.parechoc_photo_second_rayure_button.config(state="normal")
        else:
            self.parechoc_photo_second_rayure_button.config(state="disabled")

    def toggle_parechoc_impact(self):
        if self.parechoc_impact_var.get() == "OUI":
            self.parechoc_photo_impact_button.config(state="normal")
        else:
            self.parechoc_photo_impact_button.config(state="disabled")

    def toggle_parechoc_multiple_impact(self):
        if self.parechoc_multiple_impact_var.get() == "OUI":
            self.parechoc_photo_second_impact_button.config(state="normal")
        else:
            self.parechoc_photo_second_impact_button.config(state="disabled")

    def toggle_parechoc_defaut(self):
        if self.parechoc_defaut_var.get() == "OUI":
            self.parechoc_photo_defaut_button.config(state="normal")
        else:
            self.parechoc_photo_defaut_button.config(state="disabled")

    def toggle_parechoc_multiple_defaut(self):
        if self.parechoc_multiple_defaut_var.get() == "OUI":
            self.parechoc_photo_second_defaut_button.config(state="normal")
        else:
            self.parechoc_photo_second_defaut_button.config(state="disabled")

    def toggle_parechoc_alignment_defect(self):
        if self.parechoc_alignment_defect_var.get() == "OUI":
            self.parechoc_photo_alignment_defect_button.config(state="normal")
        else:
            self.parechoc_photo_alignment_defect_button.config(state="disabled")

    def toggle_parechoc_other_defect(self):
        if self.parechoc_other_defect_var.get() == "OUI":
            self.parechoc_other_defect_description.config(state="normal")
            self.parechoc_photo_other_defect_button.config(state="normal")
        else:
            self.parechoc_other_defect_description.config(state="disabled")
            self.parechoc_photo_other_defect_button.config(state="disabled")

    def upload_parechoc_corrosion_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_second_corrosion_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_rayure_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_second_rayure_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_impact_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_second_impact_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_defaut_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_second_defaut_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_alignment_defect_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_other_defect_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")

    def upload_parechoc_complete_photo(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file:
            messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file}")


    def submit(self):
        response = messagebox.askyesno("Confirmation", "Voulez-vous vraiment soumettre le formulaire ?")
        if response:
            messagebox.showinfo("Soumission", "Formulaire soumis avec succès !")
        else:
            messagebox.showinfo("Annulation", "Soumission annulée.")

if __name__ == "__main__":
    app = InspectionForm()
    app.mainloop()
