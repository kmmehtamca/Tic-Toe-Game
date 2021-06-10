
print(
    
"""
    Slicing 'Cheat Sheet'

    0    1    2    3    4    5
    +----+----+----+----+-----
    | p  |  i | z  | z  | a  |
    +----+----+----+----+-----
    -5   -4  -3    -2  -1    0 
"""
)
print("Enter the beginning and ending index for your slice of'Pizza'")
print("Pres  the enter key at 'Start' to exit,")
word = "pizza"
start1 = None
print(word[2:4])
print("Kapil Mehta")
while(start1 !="" ):
    start1 = input("Enter the starting point")
    if start1:
        start1 = int(start1)
        endpoint1= int(input("Enter the finish point"))
        print("\n")
        print(word[start1:endpoint1])

print('\\Enter the enter key to exit')
