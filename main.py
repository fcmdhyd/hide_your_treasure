# 🚨 Don't change the code below 👇
row1 = ["💩","💩","💩"]
row2 = ["💩","💩","💩"]
row3 = ["💩","💩","💩"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure?\n")

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

post = list(position)

col = int(position[0])
row = int(position[1])

cola = col - 1
rowa = row - 1

if cola==0 and rowa==0:
  row1.insert(0,"☠️")
  row1.pop()
if cola==1 and rowa==0:
  row1.insert(1,"☠️")
  row1.pop()
if cola==2 and rowa==0:
  row1.insert(2,"☠️")
  row1.pop()


if cola==0 and rowa==1:
  row2.insert(0,"☠️")
  row2.pop()
if cola==1 and rowa==1:
  row2.insert(1,"☠️")
  row2.pop()
if cola==2 and rowa==1:
  row2.insert(2,"☠️")
  row2.pop()

if cola==0 and rowa==2:
  row3.insert(0,"☠️")
  row3.pop()
if cola==1 and rowa==2:
  row3.insert(1,"☠️")
  row3.pop()
if cola==2 and rowa==2:
  row3.insert(2,"☠️")
  row3.pop()

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")