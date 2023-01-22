class Czlowiek:
    def __init__(self,imie_zadane,plec): #init
         print(f"Powstaje human o imieniu {imie_zadane}")
         self.imie=imie_zadane
         self.plec=plec 
     def przedstaw_sie(self):
         print("hej, jestem", self.imie, "i jestem", self.plec, "i jestem gatunku", self.gatunek) 

adam=Czlowiek("Adam","M")
ewa=Czlowiek("Ewa","K")
