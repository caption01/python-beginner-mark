class Car:
    """Represent a car object"""
    miles = 0

    def __init__(self, color, make, modal, miles=0):
        """Set initial detail of car"""
        self.color = color
        self.make = make
        self.modal = modal
        self.miles = miles

    def add_miles(self, miles):
        """Increase miles by given number."""
        self.miles += miles

    def display_miles(self):
        """Print the current miles values"""
        print(
            f'{self.make} {self.modal} ({self.color}) '
            f'has driven {self.miles} miles.'
        )


astra = Car('Red','Vauxhall', 'Astra')
astra.add_miles(100)
astra.add_miles(100)
astra.add_miles(100)

astra.display_miles()

prius = Car(make='Toyoya', color='Blue', modal='Prius', miles=100)
prius.add_miles(50)
prius.display_miles()