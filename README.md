# CS201 PROGRAMMING ASSIGNMENT #3  
60  POINTS   (10pts design, 50pts final)  
DESIGN DUE: 10/12/16  
FINAL DUE: 10/19/16  

## PROBLEM 
Create a program that will calculate various sports statistics for the user, based on the user’s choice of statistic. 

## PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you practice with

1. input & output
2. decision making
3. function design and implementation
4. error checking

## REQUIREMENTS ANALYSIS
The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what your program needs to do. Your program will give the user the option of calculating statistics relevant to three sports. You must do the calculations for the following sports in your program: 

* Quarterback rating in American football  
  * The quarterback rating determines how good a quarterback is in passing (throwing) a football. A perfect passer rating in the NFL is considered to be a 158.3.  
  * QB rating = 100 * [5(completions/attempts – 0.3) + 0.25(passing-yards/attempts-3) + 20(touchdown-passes/attempts) + 2.375 – (25 * interceptions/attempts)]/6  
  * Note that attempts means the number of passing attempts made, and is the same number used throughout the equation.  
  * You will want to tell the user whether or not the quarterback is a perfect passer.  
  
* Strength factor for the USA Fencing Team
  * The strength factor (SSF) determines how strong a team is, based on the number of people who have qualified for the national team. No matter what the below equation calculates, the result cannot be higher than 2.0.
  * SSF = [N/10 + 7(Sr8) + 6(Sr16) + 5(Sr32) + 4(Sr64) + 3(Jr16) + 2(Sr100)]/100, where 
    * N = Number of Competitors 
    * Sr8 = No. of fencers ranked 1-8 in the World Cup standings 
    * Sr16 = No. of fencers ranked 9-16 in the World Cup standings 
    * Sr32 = No. of fencers ranked 17-32 in the World Cup standings 
    * Sr64 = No. of fencers ranked 33-64 in the World Cup standings 
    * Sr100 = No. of fencers ranked 65-100 in the World Cup standings 
    * Jr16 = No. of fencers ranked 1-16 in the Junior World Cup standings 
  
* Calculate the final score for a gymnast on any apparatus. 
  * Assume there are 6 scores (we’re simplifying slightly from the real world). One score is on difficulty. The other 5 scores are on execution. All scores are between 0 and 10. Of the execution scores, the highest and lowest are dropped. The final score is acquired by adding the difficulty score to the average of the execution scores.

In your program, you must do some basic error checking: check if you are going to divide by zero when relevant, and don’t do the calculation if that’s the case; and before typecasting input to an int, check that it is only digits, and don’t typecast or do the calculation otherwise. In any case where an error is detected, output that it was an error, and don’t continue the calculation – you can output a zero for the result of the calculation.

## DESIGN
The second stage is to design your solution based on the requirements:

1. Determine the tasks being accomplished in your program. Each of these should be a function.
2. Remember that the user is only going to do ONE of the sports statistics calculations, although your program can do all three of them. They choose which one to do.
3. Write an algorithm for each function. This algorithm includes parameters, calculations, and returned values. In general your function will NOT output anything, except perhaps error messages when invalid input is given; your main program should do all of the output of results. Results from functions should be returned.
4. Make the main part of your program be in a “main” function. The main function never takes parameters, and does not return anything. The main function will call most of your other functions.
5. Double check that you included all of the requirements.

*NOTE:* There are no aspects of this program that you can google how to solve. The only appropriate googling will be if you want to understand a sport or its calculations better. You MUST write your own code to find the min/max for gymnastics.

You may find it helpful the first time to start on your algorithm first, and then break it up into functions later. But you need to have it written in terms of functions for the design submission. 

**DESIGN SUBMISSION: 10/12/16**

Submit to GitHub: the algorithm for your program in designInitial.txt.

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.


## PROGRAMMING REQUIREMENTS
After your design is complete and correct, it’s time to start programming and then testing:

* Fix design issues: If there were issues with your design, either not meeting requirements or in the format, fix that before you start writing your code.
* Implementation: Write your program following the requirements and based on your design.
  * Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
  * Follow good use of functions
  * Remember to define functions before they are used (so if function A calls function B, you need to define function B first in your program)
  * Remember to state the purpose of the program
* Testing: Make sure it works correctly; give it sample input, and check that the output is correct.
  * Create a partial flowchart for your program. You only need to show the details for 1 sport’s calculations. For the other 2 sports, just draw a box and state “calculations for X” where X is replaced with the name of the sport. 
  * Label the control paths in your flowchart. For each control path related to the sport your flowchart, list a test case.
  * Test your program using the test cases. You ALSO need to make sure you test your other sport calculations even though they aren’t part of your flowchart. If it doesn’t give the expected output, find the error and fix it. You are expected to turn in a fully functioning program without errors.

## ASSIGNMENT REMINDERS
Follow the programming assignment requirements document for comments, formatting, etc.

Recall that you may not do someone else’s work, or have someone else do your work. Sharing of solutions is an honor code violation. This includes someone who is not in the class, including a tutor, writing any or all of your algorithm or code or dictating to you how to do it. As everyone in the class is solving the same problem, no code may change hands. See the syllabus for details or ask the professor if you are unsure.

## EXTRA CREDIT (only if everything else works)
If you choose to do extra credit, it must be submitted in a separate file with “extraCredit” in the file name. 

Each of the following extra credit options will earn you extra credit. You can do either or both of them:
1.	Add error checking to the gymnastics calculation so that the calculation is only done if the score is between 0 and 10.
2.	Design a function that allows the user to keep trying to input an int when an int was asked for, until they do so. Use this function wherever you checked for an int in the original program.

## REFLECTION
Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult, how were functions useful?  This should be no more than a page.

## FINAL SUBMISSION   
* To GitHub:
  * Your .py file
  * Your extra credit .py file if you did the extra credit (make sure “extraCredit” is in the filename)
  * Your reflection of the programming assignment in reflection.txt
  * Your final algorithm, including the changes you made based on the design feedback in designFinal.txt
  * Your test cases based on your flowchart in testcases.txt. You should have at least 1 test case per control path, using boundary values (see notes #7).
* Hardcopy in class:
  * A flowchart of your program as described above, with control paths labeled
  * A printout of your .py file

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.
