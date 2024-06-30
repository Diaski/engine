class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def register_scene(self, scene_name, scene_class):
        self.scenes[scene_name] = scene_class

    def load_scene(self, scene_name):
        if scene_name in self.scenes:
            scene_class = self.scenes[scene_name]
            self.current_scene = scene_class()
        else:
            print(f"Scene '{scene_name}' not found")

    def get_current_scene(self):
        return self.current_scene
