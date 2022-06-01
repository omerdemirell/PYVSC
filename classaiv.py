class IpCam:
    
    CCTV ="IpCam"
    
    def __init__(self, genus, aspect ):
        
        self.genus = genus
        self.aspect = aspect
        

Camera1 = IpCam("thermal", "white")
Camera2 = IpCam("laser", "black")


print("\nCamera1 detailes:")
print("\nCamera1 is a ", Camera1.CCTV) 
print("Genus", Camera1.genus)
print("Color", Camera1.aspect)  

print("\nCamera2 detailes:")
print("\nCamera2 is a", Camera2.CCTV)
print("Genus", Camera2.genus)
print("Color", Camera2.aspect)    

print("\nAccessing class variable using class name")
print(IpCam.CCTV)
