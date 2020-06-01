def main():
    score = 0
    questionno = 0
    file = open("answers.txt", "r")
    sentences = []
    for line in file:
        line = line.strip()
        sentences.append(line)
    file.close()
    print("Welcome to Fill in the Blanks")
    print("You will be shown some questions")
    print("Each word guessed correctly will grant 1 point")

    for line in sentences:
        bracket1 = line.find("<")
        bracket2 = line.find(">")
        answer = line[bracket1+1:bracket2]
        question = line.replace("<"+answer+">", "_"*len(answer))
        print(question)
        questionno = questionno + 1
        userinp = input("Fill in the blanks: ").lower()
        if userinp == answer:
            score = score + 1
            print("Correct")
            print("You have", score, "points")
            qinput = input("Would you like to continue (Y/N)?").lower()
            if questionno >= len(sentences) and qinput == "y":
                print("We don't have any more questions for you, Thank you for playing!")
                break
           
            elif qinput == "n":
                print("Your final score is", score, "Thank you for playing!")
                break
            elif qinput != "y":
                print("That is an invalid choice")
        else:
            print("That's incorrect")
            

        
        
        

    





















if __name__ == "__main__":
    main()
