def check_temperature(temp_str: str) -> None:
	try:
		converted_str = int(temp_str)
		if converted_str >= 0 and converted_str <= 40:
			print(f"Temperature {converted_str}°C is perfect for plants!\n")
		elif converted_str > 40:
			print(f"Error: {converted_str}°C is too hot for plants (max 40°C)\n")
		elif converted_str < 0:
			print(f"Error: {converted_str}°C is too cold for plants (min 0°C)")
	except ValueError:
		print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
	print("=== Garden Temperature Checker ===\n")
	print(f"Testing temperature: 25")
	check_temperature("25")
	print(f"Testing temperature: abc")
	check_temperature("abc")
	print(f"Testing temperature: 100")
	check_temperature("100")
	print(f"Testing temperature: -50")
	check_temperature("-50")
test_temperature_input() 