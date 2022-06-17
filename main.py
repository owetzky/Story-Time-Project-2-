# project requirements: 
# create a three choice story for the user 
# the user must choose one story path
# after the story path is selected, the story must prompt the user to solve a riddle or puzzle
# story must have one multiple choice and one free response
# story must utilize Control Flow and contain at least one 'if' statement 
# user muse enter the correct answer to complete the story 
# code must contain comments or it will not be graded 
# Lincoln must choose between pursuing three high school choices; art (Basquiat High School - mom), science (Stem High School - dad) or law (Cochran High School - grandfather)

# multiple choice question with three story path 
print("**Lincoln's High School Ultimatum**")
print()
print("Lincoln is your typical 8th grader. He likes watching YouTube, playing sports and hanging out with his buddies. While finshing out his 8th grade school year, Lincoln's parents gave him an ultimatum regarding the high school he'll attend next school year. 'Choose a high school or we will choose one for you!'")
print()
print("Selecting a high school was no ordinary choice for Lincoln; his mom, dad and grandfather were all notable alumni of their high school's and were all trying to sway Lincoln towards their alma mater. Lincoln's mom was an admired painter and attended Basquiat High School, while his dad was an esteemed chemist and attended Stem High School. Lincoln's grandfather was a revered lawyer and attended Cochran High School. Lincoln rests quietly on his bed, pondering what each high school experience would be like...")
print()

# first question, choose which storline 
print("Can you help Lincoln make his high school selection?")
print()
print("a. Basquiat High School ~ 'artistic luminary in the making!'")
print("b. Stem High School ~ 'future Priestley Medal winner!'")
print("c. Cochran High School ~ 'looming torts aficionado!'")
print()
highSchoolChoice = input("Choose one of the following from above (a, b or c): ")
print()

# devlop high school choice "a" with if statements and riddle/puzzle question
if(highSchoolChoice == "a"):
  print("Lincoln imagines attending orientation with his parents at Basquiat High School. Lincoln's mother introduces him to her favorite teacher, Mr. Vivid. He quickly probes Lincoln with a question, 'What year was Jean-Michel Basquiat born? If you are to attend this high school you must memorize this question!'")
  print()

# solve question correctly to be admitted to BHS
  basquiatQuestion = input("Please enter the correct birth year: ")
  print()

  # convert free response into an integer, only accept the correct answer of 1960
  basquiatQuestion = int(basquiatQuestion)
  if(int(basquiatQuestion == 1960)):
    print(f"Lincoln, I see you know your stuff. Welcome to Basquiat High School!")
    print()
    print("Mom you are right, I am headed to Basquiat High School!")
  if(not(int(basquiatQuestion == 1960))):
    print(f"Lincoln, you have a bit more studying to do. Sorry we cannot admit you to Basquiat High School!")

# devlop high school choice "b" with if statements and riddle/puzzle question
if(highSchoolChoice == "b"):
  print("Lincoln imagines attending Stem High School for the first day. His dad warned him of the 9th grade chemistry teacher named, Mr. Beaker. As Lincoln walks into class, Mr. Beaker has a multiple choice question on the whiteboard, it read as follows:")
  print()
  print("What is the most abundant element (by mass) forming the planet Earth?")
  print()
  print("a. oxygen")
  print("b. iron")
  print("c. carbon")
  print()

  # solve question correctly to wow Mr. Beaker, only accept "b" as the correct answer
  stemQuestion = input("Choose one of the following from above (a, b or c): ")
  print()
  if(stemQuestion == "b"):
    print("Lincoln I see you are a natural, your father must be proud!")
    print()
    print("Dad you are right, I am headed to Stem High School!")
  if(not(stemQuestion) == "b"):
    print("Lincoln, maybe you should do a tad bit more studying! You do know you father is a pretty well-known chemist, right?!")

# devlop high school choice "c" with if statements and riddle/puzzle question
if(highSchoolChoice == "c"):
  print("Lincoln recollects back to a conversation he had with his grandfather. His grandfather went on in chilling detail describing a high school teacher named, Mr. Judgeship. Not only did Mr. Judgeship yell and spit when he talked, he would randomly quizzed all of his students throughout the class period on unrelated law subject matters. Lincoln's grandfather vividly details Mr. Judgeship asking him, 'how many years does a patent protection last?'")
  print()
  print("a. 10 years")
  print("b. 20 years")
  print("c. 30 years")
  print()

  # solve question correctly, only accept "b" as the correct answer
  cochranQuestion = input("Choose one of the following from above (a, b or c): ")
  print()
  if(cochranQuestion == "b"):
    print(f"Lincoln's grandfather was awed at Mr. Judgeship's silence. He then marveled at his next words, perfect answer! See me after class, I have a legal clerk internship I'd like to recommend you for! Lincoln's grandfather graciously exalted, 'That internship launched my law career!'")
    print()
    print("Grandfather you are right, I am headed to Cochran High School!")
  if(not(cochranQuestion == "b")):
    print(f"Sorry sir incorrect answer! Maybe you should study more, if you answered correctly I would have recommended you for a legal clerk internship!")
  

