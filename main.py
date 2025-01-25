from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, RiseInTransition, FallOutTransition
from kivy.properties import StringProperty
from Particles import ParticlesEffect  # Importer les particules
from kivy.lang import Builder

import Dico
import logic  # Importera la logique des jeux

# Charger le fichier .kv
Builder.load_file('Game.kv')

# Écran principal du menu
class MenuScreen(Screen):
    pass

# Écran pour le jeu du pendu
class Pendu_SurvivalScreen(Screen):
    word = StringProperty("")       # Le mot à deviner
    locate = StringProperty("")     # Le mot masqué affiché (_ _ _)
    score = StringProperty("0")
    lives = StringProperty("0")
    # Le score du joueur

    def on_enter(self):
        # Initialise la logique du pendu lorsqu'on entre sur l'écran
        self.game = logic.PenduLogic(Dico.Words_list, 23)  # Nouvelle instance de la logique du pendu
        self.word = self.game.word      # Mot à deviner
        self.locate = self.game.get_display_word()
        self.lives = str(self.game.lives)
        self.ids.lives_label.text = f"Lives : {self.lives}"
        self.ids.mot_cache.text = self.locate
        self.ids.resultat_label.text = " "

    def game_play(self, letter):
        # Appelle la logique pour traiter la lettre
        result = self.game.survival_mode(letter)
        self.locate = self.game.get_display_word()
        self.score = str(self.game.Score)
        self.lives = str(self.game.lives)
        self.ids.score_label.text = f"Score : {self.score}"
        self.ids.lives_label.text = f"Lives : {self.lives}"


        self.ids.mot_cache.text = self.locate
        self.ids.letter_input.text = ""



class Pendu_ArcadeScreen(Screen):
    word = StringProperty("")  # Le mot à deviner
    locate = StringProperty("")  # Le mot masqué affiché (_ _ _)
    stage = StringProperty("1")
    lives = StringProperty("0")

    def on_enter(self):
        # Initialise la logique du pendu lorsqu'on entre sur l'écran
        self.game = logic.PenduLogic(Dico.Words_list, 6)  # Nouvelle instance de la logique du pendu
        self.word = self.game.word  # Mot à deviner
        self.locate = self.game.get_display_word()
        self.lives = str(self.game.lives)
        self.ids.lives_label.text = f"Lives : {self.lives}"
        self.ids.stage_label.text = f"Stage : {self.stage}"
        self.ids.mot_cache.text = self.locate
        self.ids.resultat_label.text = " "

    def game_play(self, letter):
        result = self.game.arcade_mode(letter)
        self.locate = self.game.get_display_word()
        self.stage = str(self.game.stage)
        self.lives = str(self.game.lives)
        self.ids.stage_label.text = f"Stage : {self.stage}"
        self.ids.lives_label.text = f"lives : {self.lives}"

        self.ids.mot_cache.text = self.locate


class PenduModeScreen(Screen):
    pass


# Écran pour le jeu du Scrabble
class ScrabbleScreen(Screen):
    word = StringProperty("")
    score = StringProperty("0")  # Ajout d'une propriété pour le score

    def on_enter(self):
        # Initialise la logique du Scrabble
        self.game = logic.ScrabbleLogic(Dico.Words_list)
        self.word = self.game.get_letters()
        self.score = str(self.game.Score)  # Met à jour le score
        self.ids.mot_cache.text = self.word
        self.ids.resultat_label.text = ""

    def game_play(self, Word):
        result = self.game.submit_word(Word)
        self.score = str(self.game.Score)  # Met à jour le score
        self.ids.resultat_label.text = result
        self.ids.score_label.text = f"Score : {self.score}"  # Met à jour l'affichage du score


# Gestionnaire des écrans
sm = ScreenManager(transition=SlideTransition(direction='left', duration=0.6))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Pendu_SurvivalScreen(name='pendu_survival'))
sm.add_widget(Pendu_ArcadeScreen(name='pendu_arcade'))
sm.add_widget(PenduModeScreen(name='pendu_mode'))
sm.add_widget(ScrabbleScreen(name='scrabble'))

class JeuApp(App):
    def build(self):
        return sm

    def go_to_Pendu(self):
        # Définir une transition spécifique avant de passer à l'écran "Pendu_arcade"
        self.root.transition = RiseInTransition(duration=0.7)
        self.root.current = 'pendu_mode'

    def go_to_Scrabble(self):
        # Définir une transition spécifique avant de passer à l'écran "Pendu_arcade"
        self.root.transition = RiseInTransition(duration=0.7)
        self.root.current = 'scrabble'

    def go_to_Pendu_arcade(self):
        # Définir une transition spécifique avant de passer à l'écran "Pendu_arcade"
        self.root.transition = FadeTransition(duration=1)
        self.root.current = 'pendu_arcade'

    def go_to_Pendu_survival(self):
        # Définir une transition spécifique avant de passer à l'écran "Pendu_arcade"
        self.root.transition = FadeTransition(duration=1)
        self.root.current = 'pendu_survival'

    def go_to_menu(self):
        # Revenir à une transition par défaut
        self.root.transition = FallOutTransition(duration=0.5)
        self.root.current = 'menu'

if __name__ == '__main__':
    JeuApp().run()
