import datetime

name = input("What is your name ? ").strip()
age = input("How old are you ? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("WHat is your favourite hobby? ").strip()

intro_message = (
    f"Heyy! I'm {name}, {age} yrs young, vibin' in {city} 🌆.\n"
    f"By day I’m a {profession} 💼, but catch me {hobby} when I’m off the clock 😎.\n"
    f"Let’s vibe – cool to meet ya! ✌️\n"

)


current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"


border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)