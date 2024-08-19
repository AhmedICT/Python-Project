import pywhatkit
whatsapp_number = input("Enter the Whatsapp Number like +8801XXXXXXXXX:")
write_message = input ("Write your Text in here:")
t_hour = int(input("Give the time in 24 hours:"))
t_mit = int(input("Give the time in mint:"))
pywhatkit.sendwhatmsg(whatsapp_number, write_message,t_hour,t_mit)