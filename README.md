# Clash of Letters en Python

**Clash of Letters** est une application de jeu développée en Python. Elle propose deux jeux classiques :  
- Le **jeu du Pendu**  
- Le **jeu de Scrabble**

---

## Comment utiliser l'application

1. Executer la commande : `pip install kivy`
2. Exécutez le script : `main.py`
3. Une fois l'application lancée, cliquez sur le bouton correspondant au jeu auquel vous souhaitez jouer.

---

## Tutoriels

### 1. Le jeu du Pendu
Le jeu du Pendu dispose de deux modes : **Arcade** et **Survival**.

#### Mode Arcade
- Vous progressez étage par étage.
- À chaque étage, vous disposez de **six (6) essais** pour deviner le mot complet.
- Si vous devinez le mot correctement, vous passez automatiquement à l’étage suivant, et vos essais sont réinitialisés à **six (6)**.
- Si vous échouez à deviner le mot après les six essais, vous perdez et êtes ramené au **premier étage**.

#### Mode Survival
- Vous commencez avec **vingt-trois (23) vies**.
- Votre objectif est de deviner un maximum de mots avant d’épuiser vos vies.
- Chaque mot trouvé augmente votre **score** en fonction du nombre de lettres composant le mot.

---

### 2. Le jeu de Scrabble
Dans ce jeu, un long mot composé de plusieurs lettres vous est présenté.  
Votre objectif est de découvrir les **trois mots** qui ont été combinés pour former ce long mot.  

- **Mot trouvé parmi les trois :**  
  Si le mot trouvé fait partie des trois mots utilisés, votre score augmente du nombre de lettres formant ce mot.  

- **Mot trouvé mais différent :**  
  Si le mot trouvé n'est pas l'un des trois mots d'origine mais existe dans le dictionnaire, votre score augmente de **la moitié** du nombre de lettres composant ce mot.

---

## Améliorations possibles

Voici quelques idées pour améliorer l'application à l'avenir :
- Ajouter un tutoriel interactif intégré dans l'application.  
- Ajouter des effets sonores pour enrichir l'expérience utilisateur.  
- Agrandir le dictionnaire de mots pour plus de diversité.  
- Permettre de jouer dans plusieurs langues.  
- Ajouter un tableau des meilleurs scores pour encourager la compétition.
