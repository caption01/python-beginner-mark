class User():
    """Represent a user of the store"""

    def __init__(self, name, password):
        """Initialize data for user"""
        self._name = name
        self._password = password
        self._logged_in = False

    def login(self, password):
        """Check password and log user in"""
        if password == self._password:
            self._logged_in = True
        else:
            print(f'Incorrect password')
    
    def show_status(self):
        """Print the status of the user"""
        if self._logged_in:
            print(f'{self._name} is logged in')
        else:
            print(f'{self._name} is NOT logged in')

customer = User(
    name='Bruce',
    password='super123'
)

customer.login('xxxxxx')
customer.show_status()

customer.login('super123')
customer.show_status()

class Admin(User):
    """Administator of the store"""

    def __init__(self, name, password, staff_id):
        """Initialise data for a store admin"""
        super().__init__(name, password)
        self._staff_id = staff_id

    def add_product(self, name):
        """Add a new product to the inventory"""
        if self._logged_in:
            print(f'{self._name} ({self._staff_id}) added product: {name}.')
        else:
            print(f'Login to add product.')

staff = Admin(
    name='Mark',
    password='puppy123',
    staff_id=1234
)

staff.add_product('coffee')
staff.login('puppy123')
staff.add_product('Coffee')