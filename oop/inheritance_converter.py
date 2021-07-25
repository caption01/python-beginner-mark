class TempMixin:
    """Convert temperature from metric to imperial (and reverse)"""

    def f_to_c(self, f):
        """Convert imperial to metric"""
        return (f - 32) / 1.8

    def c_to_f(self, c):
        """Comvert metric to imperial"""
        return (c * 1.8) + 32


class DistanceMixin:
    """Convert distance from metric to imperial (and reverse)"""

    def m_to_km(self, miles):
        """Convert miles to KM"""
        return miles * 1.60934

    def km_to_m(self, km):
        """Convert km to miles"""
        return km * 0.6213712
    
class DigitalStorageMixin:
    """Comvert digital storage values"""

    def gb_to_mb(self, gb):
        """Convert gb to mb"""
        return gb * 1000
    
    def mb_to_gb(self, mb):
        """Convert mb to gb"""
        return mb / 1000

class Weather(TempMixin, DistanceMixin):
    """Detail about the weather."""

    def __init__(self, celsius, kmph):
        """Initial data."""
        self._celsius = celsius
        self._kmph = kmph

    def display(self, metric=True):
        """Displayw weather values"""
        if metric:
            temp = self._celsius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celsius)
            wind = self.km_to_m(self._kmph)
        
        print(f'Temp: {temp}, Wind speed: {wind}')
        print('-------- End of Weather -------')

london = Weather(12, 7)
london.display(False)

class HardDrive(TempMixin, DigitalStorageMixin):
    """Computer HardDrive"""

    def __init__(self, space, celcius):
        """Initial data."""
        self._space = space
        self._celcius = celcius
    
    def status(self, metric=True):
        """Display drive status."""
        if metric:
            temp = self._celcius
        else:
            temp = self.c_to_f(self._celcius)
        space = self.mb_to_gb(self._space)

        print(f'Space: {space} gb, Temp: {temp}')
        print('------- End ------')

hd = HardDrive(80000, 22)
hd.status(False)