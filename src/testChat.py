import numpy as np
from vispy import app, scene


class MyApp(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive', show=True)

        # Créer une scène 3D
        self.view = scene.SceneCanvas(keys='interactive', show=True)
        self.view.size = (800, 600)
        self.view.create_native()

        # Créer une vue 3D
        self.view_widget = self.view.central_widget.add_view()

        # Définir la couleur de fond de la vue en blanc
        self.view_widget.bgcolor = (1, 1, 1, 1)

        # Ajouter un cube à la scène
        self.cube = scene.visuals.Cube(
            size=1, color='red', parent=self.view_widget.scene)
        self.cube.transform = scene.transforms.STTransform(translate=(0, 0, 0))

        # Ajouter une caméra TurntableCamera à la vue
        self.cam = scene.cameras.TurntableCamera(
            parent=self.view_widget.scene, fov=60)
        self.view_widget.camera = self.cam

        # Définir une boucle de mise à jour
        self.timer = app.Timer(1.0 / 60.0, connect=self.on_timer)
        self.timer.start()

    def on_timer(self, event):
        self.update()

    def update(self):
        # Code de mise à jour à exécuter à chaque intervalle de temps dans la boucle
        pass


if __name__ == '__main__':
    my_app = MyApp()  # Créez une instance de MyApp
    app.run()  # Exécutez l'application VisPy en utilisant app.run()
