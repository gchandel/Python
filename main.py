#Python is a high level (human readable) (Layer of Low Level Language which is machine code post compilation by compiler), 
#interpreted programming language (there is no compiler so no need to compiler, interpretor will convert into byte code (low level) 
# which will further run on hardware, it will run line by line) 
# known for its dynamic typing (dyanamic typed language),  here Python Interpretor find its datatype so this is called dynamic typing
# simplicity (clean code, easy readibility)
# versatility (can be used by many places as by DE, DA, DS, Developer etc.).
print("Programming is easy")

#variable - one who can change itself. RAM - Stores Variable and it has Memory Address. Value is stored in binary format. As Hard Disk can'nt 
#match with the speed of CPU so RAM is introduced
length = 100
breadth = 100
print(length,breadth)
print(id(length),id(breadth)) #to check address of length and it stored value binary format
# Here values are same so address will be same, here both pointing to same object/address
length = 100
breadth = 200
print(length,breadth)
print(id(length),id(breadth)) #value is different so address is also different

#Variable naming convention
# a-z, A-Z, _, Number but not at start, case sensitive, Don't use keyword i.e. break, pass, if etc.
st1_length = 100
St1_length = 200
print(st1_length,St1_length)
print(id(length),id(breadth))

#Data Type - Integer, Float, String, Boolean
#Integer - +ve, -ve whole no.
#Float - Decimal
#String - Character ("Name"/'Name')
#Boolean - True/False (case sensitive)

length_of_land = 100 #int indicates statically typed language i.e C, C++ etc. 
#Here Python Interpretor find its datatype so this is called dynamic typed language
bricks_cost_per_piece = 10.5
labour_mistry_1 = 'Jagmohan' 
is_home = True

print(length_of_land,bricks_cost_per_piece,labour_mistry_1,is_home)

print(type(length_of_land),type(bricks_cost_per_piece),type(labour_mistry_1),type(is_home))