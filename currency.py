Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Iran():
    r=float(input("Enter Currency in pak = "))
    currency=r*275
    print("You have",currency,"Irani riyals")

def Saudia():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.024
    print("You have",currency,"Saudi Riyals")
    
    
def Qatar():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0237
    print("You have",currency,"Qatar Riyals")
       
  

def Turkey():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.055
    print("You have",currency,"Turkish Lira")     
    

def China():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0422
    print("You have",currency,"Chinese Yuan")       
    
def Canada():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0081
    print("You have",currency,"Canadian Dollars")       

def Iraq():
    r=float(input("Enter Currency in pak = "))
    currency=r*9.4876
    print("You have",currency,"Iraqi Dinars")          
    
def Australia():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.00843
    print("You have",currency,"Australian Dollars")          
        
def Russia():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.4866
    print("You have",currency,"Russian Rubles")          

def Dubai():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0239
    print("You have",currency,"Dirhams")          
                    
def Thailand():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.2041
    print("You have",currency,"Thai Bhats")          
            
def England():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.004707
    print("You have",currency,"Pounds")
    
def SouthAfrica():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0928
    print("You have",currency,"South African Rand Zars")
    
def Europe():
    r=float(input("Enter Currency in pak = "))
    currency=r*0.0054
    print("You have",currency,"Euros")        
 
def SriLanka():
    r=float(input("Enter Currency in pak = "))
    currency=r*1.2642
    print("You have",currency,"SriLankan Rupees")
    
    
 ###### MAIN PROGRAM #####
     
print("Welcome To Currency Exchange Agency")
print()
print("Up To Date Currency Exchanger in whole market")
print()
print("""We Convert Pak Rupees in to Following Currencies
      
      1.Iran           
      2.Saudia
      3.Qatar
      4.Turkey
      5.China
      6.Canada
      7.Iraq
      8.Australia
      9.Russia
      10.Dubai
      11.Thailand
      12.England
      13.SouthAfrica
      14.Europe
      15.SriLanka """)
      
      
print("Choose by typing Country Names ")
print()      

exchange=input("In which currency do you want to exhange = ")

if(exchange=="iran" or exchange=="Iran" or exchange==1):
    Iran()

elif(exchange=="saudia" or exchange=="Saudia" or exchange==2):
    Saudia()    

elif(exchange=="qatar" or exchange=="Qatar" or exchange==3):    
    Qatar()
    
elif(exchange=="turkey" or exchange=="Turkey" or exchange==4):
    Turkey()    

elif(exchange=="china" or exchange=="China" or exchange==5):
    China()            
    
elif(exchange=="canada" or exchange=="Canada" or exchange==6):
    Canada()    

elif(exchange=="iraq" or exchange=="Iraq" or exchange==7):
    Iraq()
    
elif(exchange=="australia" or exchange=="Australia" or exchange==8):
    Australia()    

elif(exchange=="russia" or exchange=="Russia" or exchange==9):
    Russia()            
  
elif(exchange=="dubai" or exchange=="Dubai" or exchange==10):
    Dubai()    

elif(exchange=="thailand" or exchange=="Thailand" or exchange==11):
    Thailand()
    
elif(exchange=="england" or exchange=="England" or exchange==12):
    England()    

elif(exchange=="southafrica" or exchange=="SouthAfrica" or exchange==13):
    SouthAfrica()            
  
elif(exchange=="europe" or exchange=="Europe" or exchange==14):
    Europe()    

elif(exchange=="srilanka" or exchange=="Srilanka" or exchange==15):
    SriLanka()