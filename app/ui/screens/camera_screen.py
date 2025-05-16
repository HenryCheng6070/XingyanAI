from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from app.services.camera_service import CameraService

class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        
        # Create main layout
        layout = BoxLayout(orientation='vertical')
        
        # Initialize camera service
        self.camera_service = CameraService()
        layout.add_widget(self.camera_service)
        
        # Add back button
        back_button = Button(text='返回', size_hint_y=None, height='48dp')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def on_enter(self):
        # Make sure camera_service is initialized before accessing camera
        if hasattr(self.camera_service, 'camera'):
            self.camera_service.camera.play = True
    
    def on_leave(self):
        # Stop camera when leaving the screen
        if hasattr(self.camera_service, 'camera'):
            self.camera_service.camera.play = False
    
    def go_back(self, instance):
        self.manager.current = 'main'