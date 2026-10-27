from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes = []      
ignorees = 0    

for texte in notes_brutes:        
    note = convertir_note(texte)  
    if note is None:              
        ignorees = ignorees + 1   
    else:                         
        notes.append(note)       

moy = moyenne(notes)              
print(f"Notes ignorées : {ignorees}")
print(f"Moyenne : {moy:.2f}")
print(f"Mention : {mention(moy)}")