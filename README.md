# Compléxité algorithmique

La complexité de cet algorithme est exponentielle O(2^la_profondeur_de_calcul).
Dans notre exemple la recherche se termine après 3 coups. Elle est donc de O(2^3).


# Algorithme LZ77 - Compression sans perte

L'algorithme LZ77 utilise une méthode appelée **"compression par fenêtre glissante"**. Cette technique repose sur l'utilisation d'une zone mémoire de recherche qui se déplace au fur et à mesure de l'analyse des données. Cette approche permet d'éviter les trous et optimise l'encodage.

L'algorithme est composé de deux parties principales :

- **Le dictionnaire** (à gauche) : Contient les motifs déjà rencontrés.
- **Le tampon** (à droite) : La partie de lecture où le motif à encoder est recherché.

## Principe de l'Encodage

Prenons un exemple simple avec la phrase suivante : **"Hello friends, hello world"**.

L'algorithme va d'abord rechercher un motif déjà présent dans le dictionnaire. Lorsqu'un motif est trouvé, au lieu de réécrire le motif, LZ77 encode sa position dans le dictionnaire (la distance) et sa taille. Cela permet de compresser la donnée en évitant les répétitions inutiles.

### Exemple :

Le texte **"Hello friends"** pourrait être compressé en une notation du type **(15, 6)**, ce qui signifie que le motif **"Hello"** a été trouvé à une distance de 15 caractères et a une taille de 6 caractères. Cela permet de réduire la taille du fichier en stockant seulement l'information nécessaire à la reconstruction de la donnée.

## Fonctionnement détaillé

1. **Fenêtre de Recherche et Tampon** : La recherche se fait dans une fenêtre de taille fixe. Le tampon représente une partie des données non encore encodées, et le dictionnaire représente les motifs déjà vus.
   
2. **Codage par Triplet** : L'algorithme génère des triplets composés de :
   - **Distance** : La distance entre le tampon et le motif trouvé dans le dictionnaire.
   - **Longueur** : La taille du motif trouvé.
   - **Caractère suivant** : Le caractère qui suit immédiatement le motif trouvé.

3. **Encodage** : À chaque itération, l'algorithme recherche un motif. S'il est trouvé, il encode la distance et la taille du motif, sinon, il encode le caractère comme étant une nouvelle donnée.

## Compression

L'algorithme peut, dans certains cas, ne pas être très efficace pour les petites données. Par exemple, lorsque les données sont déjà très compressées, la version compressée peut être plus grande que l'originale. Cependant, sur des textes plus volumineux, comme **"Les Misérables"**, la compression peut être significative.

### Exemple de Compression :
- Un fichier de **710 Ko** peut être compressé à **420 Ko**, soit une compression de **40%**.

## Décompression

La décompression fonctionne en inversant le processus d'encodage. On commence par initialiser un dictionnaire de recherche et un tampon. À chaque triplet (distance, longueur, caractère), on reconstruit le texte en ajoutant le motif trouvé et le caractère suivant.

### Pseudo-code de la décompression :

1. Initialisation du dictionnaire et de la donnée compressée.
2. Parcours de la donnée compressée pour récupérer les triplets.
3. Si un motif est trouvé, ajouter la portion correspondante du dictionnaire au texte.
4. Ajouter les nouveaux caractères au dictionnaire.

## Représentation Binaire

Le dictionnaire de recherche est souvent codé sur **12 bits**, ce qui permet de gérer jusqu'à **4095 caractères**, et le tampon de recherche utilise **4 bits** pour gérer jusqu'à **15 caractères**. Cela permet de compresser les données efficacement tout en optimisant l'espace mémoire.

## Source Youtube

Huffman : compresser avec un arbre
https://www.youtube.com/watch?v=915H9d5U7_E

La compression de fichier, c'est simple, en fait
https://www.youtube.com/watch?v=Z4sYZrKuL_E

Understanding the LZ77 compression algorithm - Presentation
https://www.youtube.com/watch?v=-V48ZygMUtg

## Un projet de jeux d'échec est également en cours de finition

https://github.com/Fluffy918/ProjetALgoEchec


# 🙇 Auteurs

Projets WEB1 en groupe

- **Brendan Pidoux**
- **Ethan Pandor**
- **Benmouhoub Soufiane**
- **Romain Roth**

