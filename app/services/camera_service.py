from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create camera component
        self.camera = Camera(play=True)
        self.add_widget(self.camera)
        
        # Create capture button
        self.capture_button = Button(text='拍照', size_hint_y=None, height='48dp')
        self.capture_button.bind(on_press=self.capture)
        self.add_widget(self.capture_button)
    
    def capture(self, instance):
        # Take photo and save
        image_name = f"resources/capture_{int(time.time())}.png"
        self.camera.export_to_png(image_name)
        print(f"已保存照片: {image_name}")
        return image_name
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time  # Add this import for the timestamp in capture method

class CameraService(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraService, self).__init__(**kwargs)
        self.orientation = 'vertical'