import tkinter as tk
from pynput import keyboard
from mouse_controller import MouseController

class App:
    def __init__(self, master):
        self.master = master
        self.controller = MouseController()
        self.master.title("Mouse Mover")

        # Метки для отображения точек и статуса
        self.point1_label = tk.Label(master, text="Point 1: not set")
        self.point1_label.pack()
        self.point2_label = tk.Label(master, text="Point 2: not set")
        self.point2_label.pack()

        # Поле для ввода длительности движения
        self.duration_label = tk.Label(master, text="Duration (seconds):")
        self.duration_label.pack()
        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()
        self.duration_entry.insert(0, "1")  # Значение по умолчанию

        self.status_label = tk.Label(master, text="Status: stopped")
        self.status_label.pack()

        # Запуск слушателя клавиш
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.f1:
                self.set_point1()
            elif key == keyboard.Key.f2:
                self.set_point2()
            elif key == keyboard.Key.f5:
                self.toggle_moving()
        except AttributeError:
            pass

    def set_point1(self):
        self.controller.set_point1()
        if self.controller.point1:
            self.point1_label.config(text=f"Point 1: {self.controller.point1}")

    def set_point2(self):
        self.controller.set_point2()
        if self.controller.point2:
            self.point2_label.config(text=f"Point 2: {self.controller.point2}")

    def toggle_moving(self):
        if self.controller.running:
            self.controller.stop_moving()
            self.status_label.config(text="Status: stopped")
        else:
            try:
                self.controller.duration = float(self.duration_entry.get())
            except ValueError:
                self.controller.duration = 1.0  # Если введено некорректное значение, используем 1.0
            self.controller.start_moving()
            self.status_label.config(text="Status: moving")