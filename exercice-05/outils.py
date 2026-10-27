def convertir_note(texte):
    #aller chercher ce qui doit etre remplacer et remplacer 
    texte = texte.replace(",", ".")
    try:
        return float(texte)
    except ValueError:
        return None


def moyenne(valeurs):
    return sum(valeurs)/len(valeurs)


def mention(note):
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "passable"
    elif note < 14:
        return " assez-bien"
    elif note < 16:
        return " Bien"
    else:
        return "tres bien"