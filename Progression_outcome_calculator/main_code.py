#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.


#Date:21/11/2023
#--------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------Part 1---------------------------------------------------------------------------

from graphics import *
from datetime import datetime  #for part 3 to name text files


#variable initialization
pass_credits=0
defer_credits=0
fail_credits=0
total_credits=0
progression_results=[]  #list of the results predicted
credit_collection=[]   #list of the credits entered for each student(strored in a tuple)


#Defining the function to check if input value is valid and within the range
def read_credit(user_message):
       #Looping through until the user enters a valid integer within the range
       while True:
           #exception handling to catch the error if it is out of range or if a non-integer is entered
           try: 
               credit_value=int(input(user_message))
               if credit_value in range(0,121,20): #checking if it is in the range 
                    return credit_value
               else:
                    #raising an exception to print an error  
                    raise Exception("Out of range") #reference to raise an exception: Data, R. (2023) Raise an exception, Python raise an exception. Available at: https://www.w3schools.com/python/gloss_python_raise.asp (Accessed: 25 November 2023). 
           except ValueError:
               print("Integer required")
               print()
           except Exception as e:
               print(e)
               print()
#Defining a function to ask the user if they want to enter another set of data
def read_ask(indicator):
       while True:  #looping through until user wants to quit
          ask_user=input("Would you like to enter another set of data(q to quit,y to continue): ")
          ask_user=ask_user.lower()  #converting it to lowercase so that even if the user enters an uppercase it will automatically turn to lowercase
          if ask_user=="q": #if user wants to quit
              indicator=True  #breaking out of the loop
              break
          elif ask_user=="y": #if user wants to continue 
              break
          else:
              print("Enter either 'q' or 'y'") #if user enters anything other than "q" or "y"
              print()
       return indicator

#Defining a function to assess the result of an individual student
def get_progression_outcome(p_credit,d_credit,f_credit):
       if p_credit==120: #if the pass_credits is 120 then the student can progress
              return "Progress"
       elif p_credit==100:  #if the pass_credits is 100 then the result is progress(module trailer)
              return "Progress (module trailer)"
       elif p_credit<100:  #pass_credits less than 100
              if f_credit>=80:  #if pass_credits is below 80 and fail_credits is above or equal to 80 then the result is exclude
                     return "Exclude"
              else:  #fail_credits less than 80
                     return "Module  retriever"


#Defining a function to style the text in the histogram which is repetitively used
def style_text(message):
       message.setTextColor("gray36")
       message.setSize(22)
       message.setStyle("bold")
       message.setFace("helvetica")
       

#Defining a function to build a histogram
def draw_histogram(outcome_list):
       #reference to build a histogram: from lecture notes{Graphics Reference(graphics.py v5)}
       #reference for colours: Data, R. (2023) X11 Colors, Colors - X11. Available at: https://www.w3schools.com/colors/colors_x11.asp (Accessed: 26 November 2023). 
       histogram=GraphWin("Histogram",800,600)  #open a window object,"Histogram" with size and title
       histogram.setBackground("lightyellow2")

       #Main heading
       heading=Text(Point(140,30),"Histogram Results")
       style_text(heading)  #calling the function to style heading
       heading.draw(histogram)  #rendering the heading to the window

       #drawing a line to build the graph bars above it
       graph_line=Line(Point(60,500),Point(740,500))
       graph_line.draw(histogram)  #rendering the line to the window

       #gathering the total of each outcome from the outcome_list
       progress_val=0  #variable for the Progress count
       trailer_val=0   #variable for the Progress(module trailer) count
       retriever_val=0  #variable for the Module Retriever count
       exclude_val=0  #variable for the Exclude count
       for val in outcome_list:
              if val=="Progress":
                     progress_val+=1
              elif val=="Progress (module trailer)":
                     trailer_val+=1
              elif val=="Module  retriever":
                     retriever_val+=1
              elif val=="Exclude":
                     exclude_val+=1

       #accumulating the total of each result in a list so that it can be looped to draw each rectangle       
       result_values=[progress_val,trailer_val,retriever_val,exclude_val]

       #drawing the bars for each result
       res=0  #index of outcome_list 
       i=0  #index of the colour list
       x=0  #base change for each bar
       tot_outcome=0   #variable to caluculate the total number of results
       for num in result_values:
              rec_height=500-(num*8)#by substracting the value obtained by, multiplying the result value  with a specific number(according to scaling) from the base height of the rectangle we can obtain the height of the rectangle
              bar=Rectangle(Point(90+x,500),Point(230+x,rec_height))
              #reference for colours: Data, R. (2023) X11 Colors, Colors - X11. Available at: https://www.w3schools.com/colors/colors_x11.asp (Accessed: 26 November 2023).
              colour=["mediumspringgreen","yellow2","sienna1","tomato2"] #colour list
              bar.setFill(colour[i])  #filling the rectangle with a color in the colour list
              bar.draw(histogram)  #rendering the rectangle to the window
              text_val=Text(Point(160+x,rec_height-15),num)
              style_text(text_val)  #calling the function to style text_val
              text_val.draw(histogram)  #rendering the result value to the window
              bar_names=["Progress","Trailer","Retriever","Excluded"]
              res_name=Text(Point(160+x,520),bar_names[res])
              style_text(res_name)  #calling the function to style res_name
              res_name.draw(histogram)  #rendering result name to the window
              i+=1 #increasing the index of the colour list for the next bar
              x+=160 #changing the base point to draw the next bar
              res+=1  #increasing the index of the bar_names list to name the next bar
              tot_outcome+=num  #adding the  each result value

       #Displaying the total outcomes on the histogram
       total=Text(Point(150,550),str(tot_outcome)+" "+"outcomes in total")
       style_text(total)  #calling the function to style total
       total.draw(histogram)


       histogram.getMouse()  #pause for click in window
       histogram.close()  #closes the on-screen window







#----------------------------------MAIN-------------------------------------------


#Printing the introduction
print("--------------------------PROGRESSION OUTCOME PREDICTOR-----------------------------")
print()
print("------------------------------------------------------------------------------------")
print("Enter the pass, defer and fail credits of a student and get the progression outcome")
print()
print("The acceptable range of credits is  --->  0,20,40,60,80,100,120")
print()
print("-----------------------------------------------------------------")
print()

#Taking inputs for the credits at pass, defer and fail of a student
flag=False  #introducing a flag variable
while not flag: #loop continues as long as flag is False, breaks when the flag is true(not flag evaluates to true)
       #calling the function to get and check the input
       pass_credits=read_credit("Please enter the credits at pass: ")
       defer_credits=read_credit("Please enter the credits at defer: ")
       fail_credits=read_credit("Please enter the credits at fail: ")
       #calculating the total credits
       total_credits=pass_credits + defer_credits + fail_credits
       if total_credits!=120:  #checking if the total of all the credits is equal to 120, if not asking again
              print("Total incorrect")
              print()
              continue  #using continue we can stop this iteration and start the next iteration
       elif total_credits==120:
              credit_collection.append((pass_credits,defer_credits,fail_credits))  #collecting each set of data to display as a list for part 2 and also used in part 3 to save in a text file
              outcome=get_progression_outcome(pass_credits,defer_credits,fail_credits)  #calling the function to get outcome
              progression_results.append(outcome)  #appending the results to a list 
       print(outcome)  
       print()
       user_answer=read_ask(flag) #calling the function to get the user decision to continue or to quit
       print()
       #If the flag variable is True, then it will break out of the inner loop in the read_ask function and also break out of the outer loop
       if user_answer==True: #reference to break out of 2 loops:  Abba, I.V. (2022) Break in python – nested for loop break if condition met example, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/break-in-python-nested-for-loop-break-if-condition-met-example/ (Accessed: 29 November 2023). 
              break 

print()
print()
#Drawing a histogram to display the results graphically
print("You can view the histogram of the results. Please click the mouse on any part of the window to close the histogram view")
print()
draw_histogram(progression_results)










#-----------------------------------------------------------------------Part 2---------------------------------------------------------------------------



#Printing the respective progression outcome and the list of collected data
print("--------------------------------PROGRESSION OUTCOME DATA LIST---------------------------------------")
print()
print("----------------------------------------------------------------------------------------------------")
print()
name=0  #index variable of the list progression_results
for array in credit_collection:
       stu_credits=str(array)[1:-1]  #Reference to remove the parentheses of the tuple when printing(string slicing): Jeremiah, O. (2023) Slicing and indexing in python – explained with examples, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/ (Accessed: 29 November 2023). 
       print(progression_results[name],"-",stu_credits)  
       if name<(len(progression_results)-1):  #increasing the index value only if the item on the list is less than last index value on the list
              name+=1  #increasing the index value
       else:
              break  #if not breaking out from the loop

print()
print()


#-----------------------------------------------------------------------Part 3---------------------------------------------------------------------------


#storing data in a text file and printing it
print("-----------------------------------PROGRESSION DATA FROM TEXT FILE-------------------------------------")
print()
print("-------------------------------------------------------------------------------------------------------")
print()
data=0  #index value for progression_results list
current_time=datetime.now().strftime("%I-%M-%S")  #Reference to use current time to uniquely identify a text file with the stored progression data: Data, R. (2023) Python datetime, Python Dates. Available at: https://www.w3schools.com/python/python_datetime.asp (Accessed: 29 November 2023). 
#Reference to write and read text file: Lecture notes(Using Python to write/read text files)
with open("progress_data_"+current_time+".txt","w+") as fo:  #file will be properly closed after operation within the indentation are completed
       for credit in credit_collection:  #looping through each element of the credit_collection list
              stu_credits=str(credit)[1:-1]  #Reference to remove the parentheses of the tuple when printing(string slicing): Jeremiah, O. (2023) Slicing and indexing in python – explained with examples, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/ (Accessed: 29 November 2023). 
              fo.write("{} - {}\n".format(progression_results[data],stu_credits))  #writing the progression data to the text file
              if data<(len(progression_results)-1):  #increasing the index value only if the item on the list is less than last index value on the list
                     data+=1  #increasing the index value
              else:
                     break  #if not breaking out from the loop
       fo.seek(0,0)  #Reference to go back to the start of the file: Fagbuyiro, D. (2023) File handling in python – how to create, read, and write to a file, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/file-handling-in-python/ (Accessed: 29 November 2023). 
       print(fo.read())  #reading the text file and printing the content

print()
print()
       





#-----------------------------------------------------------------------Part 4---------------------------------------------------------------------------

#updating the result in a dictionary and appending to a list to print the data
#Reference to lecture notes - as dictionaries store unique key-value pairs it can't be repeated therefore multiple dictionaries are created and appended to a list and then printed
print("-----------------------------------PROGRESSION DATA FROM DICTIONARY-------------------------------------")
print()
print("-------------------------------------------------------------------------------------------------------")
print()
prediction=0  #variable for index values of progression_results list
dict_result={}  #dictionary to store each entry
dict_collection=[]  #list to append each dictionary
for value in credit_collection:  #looping through the credit_collection list until all data are recorded
       stu_credits=str(value)[1:-1]  #Reference to remove the parentheses of the tuple when printing(string slicing): Jeremiah, O. (2023) Slicing and indexing in python – explained with examples, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/ (Accessed: 29 November 2023). 
       dict_result={progression_results[prediction]:stu_credits}  #adding the key-value pair
       dict_collection.append(dict_result)  #appending each dictionary
       if prediction<(len(progression_results)-1):  #increasing the index value only if the item on the list is less than last index value on the list
              prediction+=1  #increasing the index value
       else:
              break  #if not breaking out from the loop

for info in dict_collection:  #looping through until all the stored data are printed
       print(str(info)[1:-1])  #Reference to remove the parentheses of the tuple when printing(string slicing): Jeremiah, O. (2023) Slicing and indexing in python – explained with examples, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/ (Accessed: 29 November 2023). 


print()
print()

