import pyautogui
import time
import threading

class MouseController:
    def __init__(self):
        self.point1 = None
        self.point2 = None
        self.duration = 1.0  # Длительность движения по умолчанию (в секундах)
        self.running = False
        self.thread = None

    def set_point1(self):
        self.point1 = pyautogui.position()

    def set_point2(self):
        self.point2 = pyautogui.position()

    def move_cursor(self):
        if self.point1 is None or self.point2 is None:
            return
        while self.running:
            pyautogui.moveTo(self.point2, duration=self.duration)
            time.sleep(0.1)  # Небольшая пауза между движениями
            pyautogui.moveTo(self.point1, duration=self.duration)
            time.sleep(0.1)

    def start_moving(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self.move_cursor)
        self.thread.start()

    def stop_moving(self):
        self.running = False
        if self.thread:
            self.thread.join()