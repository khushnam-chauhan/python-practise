class MCA:
    def speak(self):
        return "moye moye "
    
class dj(MCA):
    def speak(self):
        return "Inki pinky ponky"
    
class sonali(MCA):
    def speak(self):
        return "mahesh dallle"


song=MCA()
DJ=dj()
so=sonali()

print(song.speak())
print(DJ.speak())
print(so.speak())