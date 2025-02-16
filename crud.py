
from db import connect_to_db
#from mysql.connector import Error


def inserer_inscrit(nom, prenom, age, email, photo, date_naissance):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO inscrits (nom, prenom, age, email, photo, date_naissance) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nom, prenom, age, email, photo, date_naissance)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def lire_inscrits():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM inscrits"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def mettre_a_jour_inscrit(id, nom, prenom, age, email, photo, date_naissance):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE inscrits SET nom = %s, prenom = %s, age = %s, email = %s, photo = %s, date_naissance = %s WHERE id = %s"
    values = (nom, prenom, age, email, photo, date_naissance, id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def supprimer_inscrit(id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM inscrits WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()


def rechercher_inscrits(critere):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM inscrits WHERE id = %s OR nom LIKE %s"
    cursor.execute(query, (critere, f"%{critere}%"))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def inserer_compta(id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte):

        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO compta (id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()




"""def inserer_compta(id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte):
    try:
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            query = INSERT INTO compta (id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            data = (id_inscrit, nom, prenom, mensualite, date_paiement, mois_paye, moyen_paiement, retard_paiement, alerte)
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False
    except Error as e:
        print(e)
        return False"""


def lire_compta():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM compta"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result