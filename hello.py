class thing:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Oi, {self.name}!")
	

earth = thing("world")
earth.greet()

