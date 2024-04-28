def main():
	time = input("What time is it? ")
	time = convert(time)
	
	#breakfast between 7:00 and 8:00
	if time >= 7 and time <= 8:
		print('breakfast time')
	#lunch between 12:00 and 13:00
	elif time >= 12 and time <= 13:
		print('lunch time')
	#dinner between 18:00 and 19:00
	elif time >= 18 and time <= 19:
		print('dinner time')


def convert(time):
	hours, minutes = time.split(":")
	hours, minutes = int(hours), int(minutes)
	time = hours + minutes / 60
	return time


if __name__ == "__main__":
    main()