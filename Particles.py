from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.uix.label import Label
import random

class ParticlesEffect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particles = []
        Clock.schedule_interval(self.update_particles, 2 / 30)

    def add_particle(self):
        # Générer une lettre aléatoire
        letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # Position, couleur et durée de vie aléatoires
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        lifetime = random.uniform(1, 3)
        color = (random.random(), random.random(), random.random(), 1)

        # Créer un Label pour afficher la lettre
        label = Label(text=letter, font_size=90, color=color)
        label.pos = (x, y)
        self.add_widget(label)

        # Ajouter la particule à la liste
        self.particles.append({'label': label, 'lifetime': lifetime})

    def update_particles(self, dt):
        for particle in self.particles[:]:
            particle['lifetime'] -= dt
            if particle['lifetime'] <= 0:
                # Supprimer la lettre du widget et de la liste
                self.remove_widget(particle['label'])
                self.particles.remove(particle)


        # Ajouter de nouvelles lettres si le nombre total est faible
        if len(self.particles) < 20:
            self.add_particle()
