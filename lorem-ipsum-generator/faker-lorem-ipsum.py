from faker import Faker
import time

# definir ici les 2 parametres
out_file_name = 'lorem_ipsum_10k_lines.txt'
nb_lines = 10000

def generate_large_lorem_ipsum(file_path, line_count):
    fake = Faker('fr_FR')  # Pour générer en français
    start_time = time.time()
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for _ in range(line_count):
            # Écrit une ligne de Lorem Ipsum dans le fichier.
            # Faker génère un paragraphe à chaque appel de la méthode .paragraph()
            file.write(fake.paragraph() + '\n')
    
    end_time = time.time()
    print(f"File generated in {end_time - start_time:.2f} seconds")

# Appel de la fonction
generate_large_lorem_ipsum(out_file_name, nb_lines)

