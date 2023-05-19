#Make a program of displaying questions to user like KBC
#Use list datatype to store questions and their right answer
#Display the final amount the person is taking home after playing game

l1=["How Many subcontinents are there ","Pakistan is located in which reigon ","what is capital of Pakistan "]
l2=["Seven","Asia","Islamabad"]
score = 0

n = int(input("Are you ready to start? Type 1  "))
if n == 1:
  while (True):
    x = input(l1[0])
    if x.capitalize() == l2[0]:
      score = score + 1
      print("\nRight Answer !\tScore:", score, "\n")
    else:
      print("\nBetter luck next time\nScore:", score, "\n")
      break

    x = input(l1[1])
    if x.capitalize() == l2[1]:
      score = score + 1
      print("\nRight Answer !\tScore", score, "\n")
    else:
      print("\nBetter luck next time\nScore:", score, "\n")
      break

    x = input(l1[2])
    if x.capitalize() == l2[2]:
      score = score + 1
      print("\nRight Answer !\tScore", score)
    else:
      print("\nBetter luck next time\nScore:", score, "\n")
      break
    if (score == 3):
      print("\nCongrats !!! You have won with Score ", score)
      break

else:
  print("\nThanks for showing interest")

if n == 1 and score != 3:
  print("\nYou have completed the session with score:", score,
        "\n\nThanks for Participating")