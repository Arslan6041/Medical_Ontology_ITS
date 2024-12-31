#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Functions to handle user input and display results
def submit_person_data():
    age = person_age_entry.get()
    gender = person_gender_combo.get()
    history = medical_history_entry.get()
    genetic_risk = genetic_disposition_entry.get()
    symptoms = current_symptoms_entry.get()
    diagnosis = diagnosed_with_entry.get()
    treatment = treatment_entry.get()
    
    if not age.isdigit():
        messagebox.showerror("Input Error", "Age must be an integer!")
        return
    
    result = (
        f"**Person Data**\n"
        f"Age: {age}\nGender: {gender}\nMedical History: {history}\n"
        f"Genetic Disposition: {genetic_risk}\nCurrent Symptoms: {symptoms}\n"
        f"Diagnosis: {diagnosis}\nTreatment: {treatment}"
    )
    messagebox.showinfo("Person Data Submitted", result)

def submit_symptom_data():
    severity = symptom_severity_entry.get()
    onset = onset_date_entry.get()
    duration = duration_entry.get()
    chronic = chronic_var.get()
    body_part = affected_body_part_entry.get()
    indicates = indicates_disease_entry.get()

    try:
        severity_float = float(severity)
        if not (1 <= severity_float <= 10):
            raise ValueError
        duration_days = int(duration)
    except ValueError:
        messagebox.showerror("Input Error", "Severity must be between 1-10, duration must be an integer.")
        return

    result = (
        f"**Symptom Data**\n"
        f"Severity: {severity}\nOnset Date: {onset}\nDuration: {duration_days} days\n"
        f"Chronic: {'Yes' if chronic else 'No'}\nAffected Body Part: {body_part}\n"
        f"Indicates Disease: {indicates}"
    )
    messagebox.showinfo("Symptom Data Submitted", result)

def quit_program():
    root.destroy()

# Main GUI Window
root = tk.Tk()
root.title("Medical Ontology Interface")
root.geometry("700x600")

# Notebook for Tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# =========================== TAB 1: Person ===========================
tab_person = ttk.Frame(notebook)
notebook.add(tab_person, text="Person")

# Widgets for Person
tk.Label(tab_person, text="Enter Person Details", font=("Arial", 14)).pack(pady=10)

tk.Label(tab_person, text="Age:").pack()
person_age_entry = tk.Entry(tab_person)
person_age_entry.pack()

tk.Label(tab_person, text="Gender:").pack()
person_gender_combo = ttk.Combobox(tab_person, values=["Male", "Female", "Other"])
person_gender_combo.pack()

tk.Label(tab_person, text="Medical History:").pack()
medical_history_entry = tk.Entry(tab_person)
medical_history_entry.pack()

tk.Label(tab_person, text="Genetic Disposition:").pack()
genetic_disposition_entry = tk.Entry(tab_person)
genetic_disposition_entry.pack()

tk.Label(tab_person, text="Current Symptoms:").pack()
current_symptoms_entry = tk.Entry(tab_person)
current_symptoms_entry.pack()

tk.Label(tab_person, text="Diagnosed With:").pack()
diagnosed_with_entry = tk.Entry(tab_person)
diagnosed_with_entry.pack()

tk.Label(tab_person, text="Linked Treatment:").pack()
treatment_entry = tk.Entry(tab_person)
treatment_entry.pack()

tk.Button(tab_person, text="Submit Person Data", command=submit_person_data).pack(pady=10)

# =========================== TAB 2: Symptom ===========================
tab_symptom = ttk.Frame(notebook)
notebook.add(tab_symptom, text="Symptom")

tk.Label(tab_symptom, text="Enter Symptom Details", font=("Arial", 14)).pack(pady=10)

tk.Label(tab_symptom, text="Severity (1-10):").pack()
symptom_severity_entry = tk.Entry(tab_symptom)
symptom_severity_entry.pack()

tk.Label(tab_symptom, text="Onset Date (YYYY-MM-DD):").pack()
onset_date_entry = tk.Entry(tab_symptom)
onset_date_entry.pack()

tk.Label(tab_symptom, text="Duration (in days):").pack()
duration_entry = tk.Entry(tab_symptom)
duration_entry.pack()

chronic_var = tk.BooleanVar()
tk.Checkbutton(tab_symptom, text="Is Chronic?", variable=chronic_var).pack()

tk.Label(tab_symptom, text="Affected Body Part:").pack()
affected_body_part_entry = tk.Entry(tab_symptom)
affected_body_part_entry.pack()

tk.Label(tab_symptom, text="Indicates Disease:").pack()
indicates_disease_entry = tk.Entry(tab_symptom)
indicates_disease_entry.pack()

tk.Button(tab_symptom, text="Submit Symptom Data", command=submit_symptom_data).pack(pady=10)

# =========================== TAB 3: Exit ===========================
tab_exit = ttk.Frame(notebook)
notebook.add(tab_exit, text="Exit")

tk.Label(tab_exit, text="Exit the Application", font=("Arial", 14)).pack(pady=50)
tk.Button(tab_exit, text="Quit", command=quit_program).pack()

# Run the GUI
root.mainloop()


# In[14]:


import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Function to validate and display input data for each tab
def submit_person_data():
    try:
        age = int(person_age_entry.get())
        gender = person_gender_combo.get()
        history = person_history_entry.get()
        genetics = person_genetics_entry.get()
        symptoms = person_symptoms_entry.get()
        diagnosis = person_diagnosis_entry.get()
        treatment = person_treatment_entry.get()
        
        if not gender:
            raise ValueError("Gender cannot be empty")
        
        result = (f"**Person Data Submitted**\n"
                  f"Age: {age}\nGender: {gender}\nMedical History: {history}\n"
                  f"Genetic Disposition: {genetics}\nCurrent Symptoms: {symptoms}\n"
                  f"Diagnosis: {diagnosis}\nLinked Treatment: {treatment}")
        messagebox.showinfo("Person Data", result)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {str(e)}")

def submit_symptom_data():
    try:
        severity = float(symptom_severity_entry.get())
        if not (1 <= severity <= 10):
            raise ValueError("Severity must be between 1 and 10.")
        onset = symptom_onset_entry.get()
        datetime.datetime.strptime(onset, "%Y-%m-%d")
        duration = int(symptom_duration_entry.get())
        chronic = "Yes" if chronic_var.get() else "No"
        body_part = symptom_body_part_entry.get()
        disease = symptom_disease_entry.get()
        
        result = (f"**Symptom Data Submitted**\n"
                  f"Severity: {severity}\nOnset Date: {onset}\nDuration: {duration} days\n"
                  f"Chronic: {chronic}\nAffected Body Part: {body_part}\nIndicates Disease: {disease}")
        messagebox.showinfo("Symptom Data", result)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {str(e)}")

def submit_disease_data():
    name = disease_name_entry.get()
    risk = disease_risk_entry.get()
    contagiousness = contagious_entry.get()
    body_part = disease_body_part_entry.get()
    symptom = disease_symptom_entry.get()
    treatment = disease_treatment_entry.get()
    result = (f"**Disease Data Submitted**\n"
              f"Disease: {name}\nRisk Factor: {risk}\nContagiousness: {contagiousness}\n"
              f"Affected Body Part: {body_part}\nLinked Symptom: {symptom}\nTreatment: {treatment}")
    messagebox.showinfo("Disease Data", result)

def quit_app():
    root.destroy()

# Root window
root = tk.Tk()
root.title("Advanced Medical Ontology Interface")
root.geometry("800x700")

# Tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# ========================= Tab 1: Person =========================
tab_person = ttk.Frame(notebook)
notebook.add(tab_person, text="Person")

tk.Label(tab_person, text="Person Details", font=("Arial", 14)).pack(pady=10)
person_age_entry = ttk.Entry(tab_person)
person_gender_combo = ttk.Combobox(tab_person, values=["Male", "Female", "Other"])
person_history_entry = ttk.Entry(tab_person)
person_genetics_entry = ttk.Entry(tab_person)
person_symptoms_entry = ttk.Entry(tab_person)
person_diagnosis_entry = ttk.Entry(tab_person)
person_treatment_entry = ttk.Entry(tab_person)

tk.Label(tab_person, text="Age:").pack()
person_age_entry.pack()
tk.Label(tab_person, text="Gender:").pack()
person_gender_combo.pack()
tk.Label(tab_person, text="Medical History:").pack()
person_history_entry.pack()
tk.Label(tab_person, text="Genetic Disposition:").pack()
person_genetics_entry.pack()
tk.Label(tab_person, text="Current Symptoms:").pack()
person_symptoms_entry.pack()
tk.Label(tab_person, text="Diagnosed With:").pack()
person_diagnosis_entry.pack()
tk.Label(tab_person, text="Linked Treatment:").pack()
person_treatment_entry.pack()

tk.Button(tab_person, text="Submit Person Data", command=submit_person_data).pack(pady=10)

# ========================= Tab 2: Symptom =========================
tab_symptom = ttk.Frame(notebook)
notebook.add(tab_symptom, text="Symptom")

tk.Label(tab_symptom, text="Symptom Details", font=("Arial", 14)).pack(pady=10)
symptom_severity_entry = ttk.Entry(tab_symptom)
symptom_onset_entry = ttk.Entry(tab_symptom)
symptom_duration_entry = ttk.Entry(tab_symptom)
chronic_var = tk.BooleanVar()
symptom_body_part_entry = ttk.Entry(tab_symptom)
symptom_disease_entry = ttk.Entry(tab_symptom)

tk.Label(tab_symptom, text="Severity (1-10):").pack()
symptom_severity_entry.pack()
tk.Label(tab_symptom, text="Onset Date (YYYY-MM-DD):").pack()
symptom_onset_entry.pack()
tk.Label(tab_symptom, text="Duration (Days):").pack()
symptom_duration_entry.pack()
tk.Checkbutton(tab_symptom, text="Is Chronic?", variable=chronic_var).pack()
tk.Label(tab_symptom, text="Affected Body Part:").pack()
symptom_body_part_entry.pack()
tk.Label(tab_symptom, text="Indicates Disease:").pack()
symptom_disease_entry.pack()

tk.Button(tab_symptom, text="Submit Symptom Data", command=submit_symptom_data).pack(pady=10)

# ========================= Tab 3: Disease =========================
tab_disease = ttk.Frame(notebook)
notebook.add(tab_disease, text="Disease")

tk.Label(tab_disease, text="Disease Details", font=("Arial", 14)).pack(pady=10)
disease_name_entry = ttk.Entry(tab_disease)
disease_risk_entry = ttk.Entry(tab_disease)
contagious_entry = ttk.Entry(tab_disease)
disease_body_part_entry = ttk.Entry(tab_disease)
disease_symptom_entry = ttk.Entry(tab_disease)
disease_treatment_entry = ttk.Entry(tab_disease)

tk.Label(tab_disease, text="Disease Name:").pack()
disease_name_entry.pack()
tk.Label(tab_disease, text="Risk Factor:").pack()
disease_risk_entry.pack()
tk.Label(tab_disease, text="Contagiousness Score:").pack()
contagious_entry.pack()
tk.Label(tab_disease, text="Affected Body Part:").pack()
disease_body_part_entry.pack()
tk.Label(tab_disease, text="Related Symptom:").pack()
disease_symptom_entry.pack()
tk.Label(tab_disease, text="Treatment Protocol:").pack()
disease_treatment_entry.pack()

tk.Button(tab_disease, text="Submit Disease Data", command=submit_disease_data).pack(pady=10)

# ========================= Exit Button =========================
tk.Button(root, text="Quit", command=quit_app, bg="red", fg="white").pack(pady=20)

# Run Application
root.mainloop()


# In[15]:


import tkinter as tk
from tkinter import ttk, messagebox

# Function Definitions
def submit_person():
    age = person_age_entry.get()
    gender = person_gender_combo.get()
    history = medical_history_entry.get()
    genetics = genetic_disposition_entry.get()
    symptoms = current_symptoms_entry.get()
    diagnosis = diagnosed_with_entry.get()
    treatment = linked_treatment_entry.get()

    if not age.isdigit():
        messagebox.showerror("Input Error", "Age must be an integer.")
        return
    
    result = (
        f"**Person Data Submitted**\n"
        f"Age: {age}\nGender: {gender}\nMedical History: {history}\n"
        f"Genetic Disposition: {genetics}\nCurrent Symptoms: {symptoms}\n"
        f"Diagnosis: {diagnosis}\nLinked Treatment: {treatment}"
    )
    messagebox.showinfo("Person Data", result)

def submit_symptom():
    severity = symptom_severity_entry.get()
    duration = symptom_duration_entry.get()
    chronic = chronic_var.get()
    body_part = body_part_entry.get()
    disease = indicates_disease_entry.get()

    if not severity.replace('.', '', 1).isdigit() or not duration.isdigit():
        messagebox.showerror("Input Error", "Severity must be a float and duration must be an integer.")
        return
    
    result = (
        f"**Symptom Data Submitted**\n"
        f"Severity: {severity}\nDuration: {duration} days\nChronic: {'Yes' if chronic else 'No'}\n"
        f"Affected Body Part: {body_part}\nIndicates Disease: {disease}"
    )
    messagebox.showinfo("Symptom Data", result)

# GUI Setup
root = tk.Tk()
root.title("Medical Ontology System")
root.geometry("800x600")

# Title Label
tk.Label(root, text="Medical Ontology System", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Enter Details for Person, Symptoms, and Disease", font=("Arial", 12)).pack()

# Frames for Sections
person_frame = tk.LabelFrame(root, text="Person Details", font=("Arial", 12, "bold"))
person_frame.pack(fill="both", padx=10, pady=10)

symptom_frame = tk.LabelFrame(root, text="Symptom Details", font=("Arial", 12, "bold"))
symptom_frame.pack(fill="both", padx=10, pady=10)

# ==================== Person Section ====================
tk.Label(person_frame, text="Age:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
person_age_entry = tk.Entry(person_frame)
person_age_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Gender:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
person_gender_combo = ttk.Combobox(person_frame, values=["Male", "Female", "Other"])
person_gender_combo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Medical History:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
medical_history_entry = tk.Entry(person_frame)
medical_history_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Genetic Disposition:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
genetic_disposition_entry = tk.Entry(person_frame)
genetic_disposition_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Current Symptoms:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
current_symptoms_entry = tk.Entry(person_frame)
current_symptoms_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Diagnosed With:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
diagnosed_with_entry = tk.Entry(person_frame)
diagnosed_with_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(person_frame, text="Linked Treatment:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
linked_treatment_entry = tk.Entry(person_frame)
linked_treatment_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Button(person_frame, text="Submit Person Data", command=submit_person, bg="lightblue").grid(
    row=7, column=0, columnspan=2, pady=10
)

# ==================== Symptom Section ====================
tk.Label(symptom_frame, text="Severity (1-10):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
symptom_severity_entry = tk.Entry(symptom_frame)
symptom_severity_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(symptom_frame, text="Duration (in days):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
symptom_duration_entry = tk.Entry(symptom_frame)
symptom_duration_entry.grid(row=1, column=1, padx=5, pady=5)

chronic_var = tk.BooleanVar()
tk.Checkbutton(symptom_frame, text="Is Chronic?", variable=chronic_var).grid(row=2, column=0, columnspan=2)

tk.Label(symptom_frame, text="Affected Body Part:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
body_part_entry = tk.Entry(symptom_frame)
body_part_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(symptom_frame, text="Indicates Disease:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
indicates_disease_entry = tk.Entry(symptom_frame)
indicates_disease_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Button(symptom_frame, text="Submit Symptom Data", command=submit_symptom, bg="lightgreen").grid(
    row=5, column=0, columnspan=2, pady=10
)

# Run the Application
root.mainloop()


# In[16]:


from owlready2 import *
import tkinter as tk
from tkinter import ttk, messagebox

# Load the ontology RDF file
onto = get_ontology("medical.rdf").load()

# ======================= Dynamic Class Extraction =======================
classes = list(onto.classes())
data_properties = list(onto.data_properties())
object_properties = list(onto.object_properties())

# Dictionary to store user inputs dynamically
user_data = {}

# Function to submit form data for a selected class
def submit_data(class_name):
    global user_data
    result = f"Data for {class_name}:\n"
    for prop in user_data[class_name]:
        value = user_data[class_name][prop].get()
        result += f"{prop}: {value}\n"
    messagebox.showinfo("Submission Successful", result)

# Function to create input fields dynamically for a selected class
def build_form(frame, selected_class):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=f"Class: {selected_class}", font=("Arial", 14, "bold")).pack(pady=5)
    
    user_data[selected_class] = {}  # Initialize empty dictionary for class inputs

    for prop in data_properties:
        if selected_class in [cls.name for cls in prop.domain]:
            # Create an input field for each data property
            tk.Label(frame, text=f"{prop.name}:").pack(anchor="w")
            entry = ttk.Entry(frame)
            entry.pack(fill="x", pady=2)
            user_data[selected_class][prop.name] = entry

    tk.Button(frame, text="Submit", command=lambda: submit_data(selected_class)).pack(pady=10)

# ======================= GUI Setup =======================
root = tk.Tk()
root.title("Medical Ontology Interface")
root.geometry("800x600")

# Title
tk.Label(root, text="Medical Ontology Interface", font=("Arial", 18, "bold")).pack(pady=10)

# Dropdown for Class Selection
class_label = tk.Label(root, text="Select a Class:")
class_label.pack()
selected_class = tk.StringVar()
class_dropdown = ttk.Combobox(root, textvariable=selected_class, values=[cls.name for cls in classes])
class_dropdown.pack()

# Frame for Input Form
form_frame = tk.Frame(root, bd=2, relief="ridge")
form_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Build Form Button
tk.Button(root, text="Build Form", command=lambda: build_form(form_frame, selected_class.get())).pack(pady=10)

# Exit Button
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white").pack(pady=5)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




