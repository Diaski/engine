from .example_scene import ExampleScene

def register_scenes(scene_manager):
    scene_manager.register_scene("example", ExampleScene)
