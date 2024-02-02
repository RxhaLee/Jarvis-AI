#jervis 		: Beta 
#created by 	: Maharaj Teertha Deb
#linked IN 		: https://www.linkedin.com/in/maharaj-teertha-deb/
#released on 	: September-21-2023

'''
	Changes on Beta 0.2.1 
		* User can Type and Speak to command Jarvis
		* Opens some application using "Open Application function"
		* Very good at searching youtube Videos

	Changes on Beta 0.4.9
		* Able to Play Music
		* Issue on sending emails
		* GPT integration (Trial Mode)

	Changes on Beta 0.4.91
		* Better Weather using web scrapping.
		* Some features are still in development.
		* ChatGPT is Uniavailable in this version as it requires premium subscription.
		* Google Bard is being introduced.

	Changes on Beta 0.4.92
		* Modules are on different files so easy to debug.
		* Playing song from youtube is perfect now.
		* It can now tell a joke.
		* Next version will be dedicated on Google Bard or User Based design.

	Changes on 1.00:
		* Personalized Assistant.
		* GPT 3.5 : powered.
		* Improved Search Engine.
		* More Features.
'''


# The code script that imports various libraries and modules to perform different tasks.
import datetime
import wikipedia
import os
import webbrowser
import smtplib
from bs4 import BeautifulSoup
import requests
import urllib.parse
from googlesearch import search
import Joke
from tryGPT import ask_gpt


from weather import find_weather_element
from Speak import speak
from TakeCommand import takeCommand
from OpenApplication import open_application
from GoogleSearch import googleSearch
from tryYoutube import playMusicFromYouTube
from WeatherVisual import Gen_report
import User

boss = None

def User_Set_UP():
	'''
		This function creates the user object with all necessary information for interaction, such as name, email address
		This function creates the user object for personalization of responses, takes user's name and
		asks if they want to continue with previous data (if any) or create new one.

		Since : 1.00
	'''
	global boss
	boss = User.return_user()
	if(boss == None):
		print("Welcome to Jarvis AI Assistant! I will be your personal assistant. Before you continue, let's setup your personal assistant at first. \nIt is a one time setup and next time you will just click and run it.")
		speak("Welcome to Jarvis AI Assistant! I will be your personal assistant. Before you continue, let's setup your personal assistant at first. It is a one time setup and next time you will just click and run it.")
		speak("So let's get started.")
		boss = User.User()
	
	User.save_user_to_file(boss)

def wish_User():
	"""
		The function `wish_User()` greets the user based on the current time and introduces itself as a
		personal assistant.

		updated : 1.00 : personalized wish
	"""
	hour = int(datetime.datetime.now().hour)
	
	if boss.is_birthday_today():
		age = datetime.datetime.now().year - boss.birth_date.year
		print(f"{boss.pronunciation},  Happy Birthday! You are {age} years old today.")
		speak(f"Happy {age} th Birthday")
	
	if hour>=0 and hour<12:
		speak("Good Morning Sir !")
	
	elif hour>=12 and hour<18:
		speak("Good Afternoon Sir !")
	
	else:
		speak("Good Evening Sir !")

	speak("I am your personal assistant, Jarvis. Please tell me how may I help you?")






def sendEmail(to , content):
	
	"""
	!!! THIS FUNCTION IS NOT DONE YET.....
	The function `sendEmail` sends an email to the specified recipient with the given content.
	
	:param to: The "to" parameter is the email address of the recipient to whom you want to send the
	email. It should be a string containing the email address
	:param content: The content parameter is the body of the email that you want to send. It can be a
	string containing the message you want to send to the recipient
	"""
	server = smtplib.SMTP("smtb.gmail.com" , 587)
	server.ehlo()
	server.starttls()
	server.login('yourEmail@gmail.com' , '*****')
	server.sendmail("d_mahar@concordia.ca" , to , content)
	server.close()


######################################################################################################################### Main Function Follows :::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::;;;;


if __name__ == "__main__":

	User_Set_UP()
	
	user_wants_to_type = True ### Check this
	wish_User()
	
	print("If you want to command me by typing , speak : I want to type")
	speak("Just to let you know that, you can command me by typing. If you want to command by typing, speak so")

	while (True):

		if(user_wants_to_type) : 
			speak("Enter your command: ")
			query = input("\nEnter your command : ")
			query = query.lower()
		
		else : 
			query = takeCommand().lower()


		# The code block is checking if the word "wikipedia" is present in the user's query. If
		# it is, the code removes the word "wikipedia" from the query and uses the `wikipedia` library to
		# search for a summary of the remaining query on Wikipedia. It retrieves the summary of the query
		# and stores it in the `results` variable. The `sentences` parameter specifies the number of
		# sentences to include in the summary, in this case, it is set to 2. The code then prints the
		# results and speaks it using the `speak` function.
		if ("wikipedia" in query):
			speak("Searching Wikipedia...")
			query = query.replace("wikipedia" , "")
			# The line `results = wikipedia.summary(query , sentences = 2)` is using the `wikipedia` library to
			# search for a summary of the query on Wikipedia. It retrieves the summary of the query and stores
			# it in the `results` variable. The `sentences` parameter specifies the number of sentences to
			# include in the summary. In this case, it is set to 2, so the summary will contain 2 sentences.
			# then it prints the result and speaks it.
			results = wikipedia.summary(query , sentences = 2)
			print(results)
			speak(f"According to Wikipedia,{results}")
		

		# The code is checking if the query contains the words "play" and "from youtube". If it does,
		# it extracts the music query by removing the words "play" and "from youtube" from the query and
		# then calls the function `playMusicFromYouTube` with the extracted music query as an argument.
		elif "play" in query and "from youtube" in query:
			music_query = query.replace("play", "").replace("from youtube", "").strip()
			playMusicFromYouTube(music_query)
			

		# The code block elif ("open youtube" in query): is checking if the
		# user's query contains the phrase "open youtube". If it does, it opens the YouTube website in the
		# default web browser using the `webbrowser.open()` function. This allows the user to easily access
		# the YouTube website by simply saying "open youtube" to the personal assistant.
		elif ("open youtube" in query):
			try:
				webbrowser.open("https://www.youtube.com")
				print("Youtube opened via your default browser")
				speak("Do you want me to play anymusic?")
				query = takeCommand.lower()
				if "yes" in query:
					speak("ask me the song to play: ")
					query = takeCommand().lower()
					music_query = query.replace("play", "").replace("from youtube", "").strip()
					playMusicFromYouTube(music_query)
				elif "play" in query and "from youtube" in query:
					music_query = query.replace("play", "").replace("from youtube", "").strip()
					playMusicFromYouTube(music_query)
				else:
					speak("Aborting playing music and Waiting on the next command...")
					print("Aborting playing music.")

			except Exception as e:
					print("An error occurred:", e)
					speak("An error occured while opening youtube from your browser.")

		# The code block is checking if the user's query contains the phrase "open
		# google". If it does, it opens the Google website in the default web browser using the
		# `webbrowser.open()` function. This allows the user to easily access the Google website by simply
		# saying "open google" to the personal assistant.
		elif ("open google" in query):
			webbrowser.open("https://www.google.com")
			print("Google opened via your default browser")

		# The code block checking if the user's query contains the phrase "open
		# facebook". If it does, it opens the Facebook website in the default web browser using the
		# `webbrowser.open()` function. This allows the user to easily access the Facebook website by simply
		# saying "open facebook" to the personal assistant.
		elif ("open facebook" in query):
			webbrowser.open("https://www.facebook.com")
			print("Facebook opened via your default browser")

		# The code block is checking if the user's query contains the phrase "open gmail".
		# If it does, it opens the Gmail website in the default web browser using the `webbrowser.open()`
		# function. This allows the user to easily access the Gmail website by simply saying "open gmail" to
		# the personal assistant.
		elif ("open gmail" in query):
			webbrowser.open("https://www.gmail.com")
			print("Gmail opened via your default browser")
		
		# The code block is checking if
		# the user's query contains the phrase "open linkedin". If it does, it opens the LinkedIn website in
		# the default web browser using the `webbrowser.open()` function. This allows the user to easily
		# access the LinkedIn website by simply saying "open linkedin" to the personal assistant.
		elif ("open linkedin" in query):
			webbrowser.open("https://www.linkedin.com")
			print("LinkedIN opened via your default browser")
		
		# The code block is checking if
		# the user's query contains the phrase "open chatgpt". If it does, it opens the ChatGPT website
		# (chat.openai.com) in the default web browser using the `webbrowser.open()` function. This allows
		# the user to easily access the ChatGPT website by simply saying "open chatgpt" to the personal
		# assistant.
		elif ("open chat gpt" in query or "open gpt" in query):
			webbrowser.open("https://www.chat.openai.com")
			print("ChatGPT opened via your default browser")

		# This code handles the functionality of playing music. It allows the user to specify a music directory and plays songs from that directory.
		# Updated on : <0.2.2>
		# Functionality:
		# - Checks if the specified music directory exists and creates it if it doesn't.
		# - Checks if a music directory path is already assigned in a file and reads it.
		# - If the music directory path is not assigned, prompts the user to enter it and saves it in the file.
		# - Lists the songs in the music directory and plays the first song.
		# - Provides appropriate messages for scenarios where no songs are found or if there are errors in the process.+
		
		elif "play" in query and ("music" in query or "song" in query):
			'''
				Updated on : <1.00>
				Functionality:
					- Checks if user has already a music directory
					- if not , asks uers to enter it
					- if the directory is valid, saves it, otherwise asks to make this directory
					- either cases it saves update to user file.
					- Finally tries to play music from the directory.
			'''
			if(boss.check_music_directory):
				music_dir = boss.get_music_directory()

			else:
				music_dir = input("Please enter your music directory full-path: ")

			if not os.path.exists(music_dir):
				speak("That is an invalid Path. Do you want me to make this path?")
				choise = input ("That is an invalid Path. Do you want me to make this path? (Yes / No) : ")

				if choise[0] == "y" or choise[0] == "Y":
					os.makedirs(music_dir)
					print("Directory made. Now you can paste your songs in that directory.")
					speak("Directory made. Now you can paste your songs in that directory.")
					boss.set_music_directory(music_dir)
					User.save_user_to_file(boss)					

				else:
					print("Operation aborted to play musics")
					speak("Operation aborted to play musics")
					continue
			
			else:
				boss.set_music_directory(music_dir)
				User.save_user_to_file(boss)

			try:
				songs = os.listdir(music_dir)
				if len(songs) == 0:
					speak("No songs found in the music directory.")
					print("No songs found in the music directory.")
				else:
					speak("Playing songs.")
					print("Playing Songs: ", songs)
					os.startfile(os.path.join(music_dir, songs[0]))
			except Exception as e:
				print("Error:", e)
				speak(f"Sorry {boss.pronunciation}, I couldn't play music.")

		
		# The code block `elif ("the time" in query)` is checking if the user's query contains the phrase
		# "the time". If it does, it retrieves the current time using the
		# `datetime.datetime.now().strftime("%H:%M:%S")` function and stores it in the `strTime` variable.
		# It then prints the current time and speaks it using the `speak` function. This allows the personal
		# assistant to provide the user with the current time when asked.
		elif ("the time" in query) :
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print("The current time is: " , strTime)
			speak(f"The time is, {strTime}")

	
		# The code is checking if the query contains the phrase "open code" or "open visual studio
		# code". If either of these phrases is present, it will call the function "open_application" and
		# pass the argument "Visual Studio Code.exe".
		elif (("open code" in query) or ("open visual studio code" in query)):
			open_application("Visual Studio Code.exe")
			
		# The code is checking if the string "open notepad in query" is present. If it is, it will
		# open the Notepad application.
		elif "open notepad" in query:
			open_application("notepad.exe")

		elif "open chrome" in query:
			open_application("chrome.exe")

		# The code block `elif ("email to me" in query)` is checking if the user's query contains the phrase
		# "email to me". If it does, it prompts the user to provide the content of the email by saying "What
		# should I write?". It then uses the `takeCommand()` function to convert the user's speech input
		# into text and stores it in the `content` variable. After that, it speaks the message "The email
		# has been sent". If there is an error during the process of sending the email, it prints the error
		# message and speaks "Sorry, I was not able to send the email due to [error message]".
		elif ("email" in query):
			try:
				speak("What should i write ?")
				content = input("Write content here: ")
				speak("The content that were written: ")
				print(content)
				speak(content)
				ask_Confirmation = input("Should I send it? (yes/no): ")
				speak("Should I send it?")
				if("e" in ask_Confirmation and "s" in ask_Confirmation):
					speak("Enter the email address to be sent: ")
					receiverEmailAddress = input("enter receivers email: ")
					speak("What is the subject is the email: ")
					subject = takeCommand()
					speak("Trying to send the email")
					send_email_with_selenium(receiverEmailAddress , subject , content)
				else:
					speak("You aborted the operation")
					print("You aborted the operation")
			except Exception as e:
				print("Error :" , e)
				speak("Sorry , I was not able to send the email. due to ")
		
		
		elif ("google" in query):
			# The code is checking if the word "google" is present in the variable "query". If it is, it
			# removes the word "google" from the query and strips any leading or trailing whitespace. It then
			# calls a function called "googleSearch" with the modified search query as an argument.
			search_query = query.replace("google" , "").strip()
			googleSearch(search_query)
		
		
		elif "weather" in query and "in" in query :
			'''
				This code presents weather visuals.

				Since : <1.00>

				# The code is checking if the word "weather" and the word "in" are present in the query. If
				# both words are present, it will extract the city name from the query and pass it to the function
				# `Gen_report()` to generate a weather report for that city.
			'''
			
			try:
				cityName = query.split("in")[1].strip()
				Gen_report(cityName)
				speak("Weather visuals on your screen")
				
			except Exception as e:
				print("An error occurred while processing your request.")
				print("Error: " , e)
				speak("There was an error processing your request.")

		# The code snippet that handles a query related to weather. It first checks
		# if the word "weather" is present in the query. If it is, it extracts the search query by removing
		# the phrase "what is" and any leading or trailing spaces.
		elif "weather" in query or ("temperature" in query and "now" in query):
			
			try:
				temp = find_weather_element()
				print( temp + " degree Celcious")
				speak("The Temerature is :" + temp + " celcious")
			except Exception as e:
				print("Error:", e)
	

		elif "what is" in query or "search" in query:
			search_query = query.replace("what is", "").strip()
			# First, try searching on Wikipedia
			try:
				wikipedia_results = wikipedia.summary(search_query , sentences = 3)
				try:
					print(wikipedia_results)
					speak("According to Wikipedia,")
					speak(wikipedia_results)
				except Exception as e:
					print("Error while searching in wikipedia. Error : " , e)
				# If not found on Wikipedia, search on Google
			except Exception as e:
				googleSearch(search_query)


		# The above code is a Python code snippet that handles a query asking "who is" a certain person.
		## Since : 0.4.92
		elif "who is" in query:
			person_to_search = query.replace("who is", "").strip()

			# Attempt to find information on Wikipedia
			try:
				wikipedia_results = wikipedia.summary(person_to_search, sentences=3)
				print(wikipedia_results)
				speak(f"According to Wikipedia, {wikipedia_results}")
			
			# If not found on Wikipedia, search on Google
			except wikipedia.exceptions.DisambiguationError as e:
				print(f"DisambiguationError: {e}")
				speak(f"Searching for {person_to_search} on Google.")
				
				# You can implement your Google search logic here
				googleSearch(person_to_search)
			
			except Exception as e:
				print(f"Error while searching for {person_to_search} on Wikipedia: {e}")
				speak(f"Sorry, I couldn't find information about {person_to_search} on Wikipedia.")
				speak(f"Please ensure that {person_to_search} is on Wikipedia for accurate results.")

		# The above code is checking if the string "Joke" is present in the variable "query". If it is, it
		# calls the function "tellJoke()" to tell a joke.
		# Since : 0.4.92 
		elif "joke" in query:
			# Extracting the topic from the query
			split_query = query.split("joke", 1)  # Split the query at the word "joke"
			
			if len(split_query) > 1 and split_query[1].strip():  # Check if there's content after "joke"
				topic = split_query[1].strip().split()  # Extract the topic after "joke"
				if len(topic) > 1:
					print("Topic:", topic[1])
					Joke.tell_joke(topic[1])
				else:
					Joke.tell_joke(topic[0])  # If there's only one word after "joke", treat it as the topic
			else:
				Joke.tell_joke()  # No specific topic mentioned, tell a random joke


		# The code checks if the string "thank you" is
		# present in the variable "query". If it is, then it calls the function "speak" with the message
		# "You are welcome. I am designed to help you by all means any time."
		elif("thank you" in query):
			speak("You are welcome. I am designed to help you by all means any time.")
		
		# The above code is checking if the string "how do you work?" is present in the variable "query". If
		# it is, then it will execute the code inside the if statement, which includes speaking a response.
		elif("how do you work?" in query):
			speak("let that be a secret , but you can explore me")
			print(":)")
		
		# The code snippet that handles a query containing the word "where". It
		# performs search query on google and speaks the result.
		elif "where" in query:
			search_query = query.replace("where", "").strip()
			encoded_query = urllib.parse.quote(search_query)
			search_url = f"https://www.google.com/search?q=where+{encoded_query}"
			try:
				webbrowser.open(search_url)
				speak("Here is the result:")
				try:
					response = requests.get(search_url)
					soup = BeautifulSoup(response.text, "html.parser")
					# Find and extract the main search result description
					search_result = soup.find(class_="BBwThe")
					print(search_result.get_text())
					if search_result:
						speak(search_result.get_text())
					else:
						speak("I'm sorry, I couldn't find the information you requested.")
					
				except Exception as e:
					print("Error:", e)
					speak("Sorry, I could not find what you were looking for. Please try again later.")
					
			except Exception as e:
				print("Error:", e)
				speak("Sorry, I couldn't open the website.")

		
		
		# The code is checking if the string "who made you" is present in the variable "query". If it
		# is, it will print a message and a link to the LinkedIn profile of Mr. Maharaj Teertha Deb.
		elif "who made you" in query:
			speak("Mr. Maharaj Teertha Deb made me. visit his linkedIN profile typed below")
			print("https://www.linkedin.com/in/maharaj-teertha-deb/")

		# The cod is checking if the words "quite" or "exit" are present in the variable "query". If
		# either of these words is present, it will execute the code inside the if statement. In this case,
		# it will call the "speak" function to say "Thank you for using me. Talk to you later. Bye" and then
		# exit the program with a status code of 0.
		elif ("quite" in query or "exit" in query):
			speak("Thank you for using me. Talk to you later. Bye")
			print("Thank you.")
			break

		# The code is checking if the string "i" and "type" are present in the variable "query". If
		# both conditions are true, it sets the variable "user_wants_to_type" to True and speaks a message
		# informing the user that they will be typing to command the program.
		elif ("i" in query and "type" in query):
			user_wants_to_type = True
			speak("You will be typing to command me now. If you want to speak instead, write I want to speak")

		# The code is checking if the string "i" is present in the variable "query" and if the string
		# "speak" is present in the variable "query". If both conditions are true, it sets the variable
		# "user_wants_to_type" to False and calls the function "speak" with the argument "You can command me
		# by saying anything. And you know how to type to command me".
		elif ("i" in query and "speak" in query):
			user_wants_to_type = False
			speak("You can command me by saying anything. And you know how to type to command me")

		else:
			'''
				since : 1.00
				functionality:
					- checks user's gpt api
					- if they have it,  generates response based on user's input from gpt.
			'''
			if boss.gpt_api != None:
				try:
					ask_gpt(query , boss.gpt_api)
				
				except Exception as e:

					if ("insufficient_quota" in str(e)):
						print("Your Api key is out expired now. You need to get a new api key. I am opening the webbrowser you can get a new api key")
						speak("Your Api key is out expired now. You need to get a new api key. I am opening the webbrowser you can get a new api key")
						boss.set_gpt_api(None)
						print("Try the command again.")
						speak("Try the command again.")
						User.save_user_to_file(boss)

					elif ("invalid_api_key" in str(e)):
						print("Gpt says that is an invalid api key.")
						speak("Opps!  It seems like your GPT API Key is not valid.")
						boss.set_gpt_api(None)
						print("Try the command again.")
						speak("Try the command again.")
						User.save_user_to_file(boss)

					else:
						print("I tried GPT, but failed to response due to :" , e)
						speak("I tried GPT, but failed to response")
			
			else:
				print("Sorry , I don't know this command, also you did not setup your gpt api, so i can't search on gpt.")
				speak("Sorry , I don't know this command, also you did not setup your gpt api, so i can't search on gpt.")