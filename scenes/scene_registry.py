from scenes.example_scene import ExampleScene

def register_scenes(scene_manager, event_handler):
    scene_manager.register_scene("example", lambda: ExampleScene(event_handler))
