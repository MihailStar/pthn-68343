# 1
def generate_letter(
    mail: str,
    name: str,
    date: str,
    time: str,
    place: str,
    teacher: str = "Тимур Гуев",
    number: int = 17,
) -> str:
    return f"""To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}.
Экзамен будет проводить {teacher} в кабинете {number}.
Желаем удачи на экзамене!"""


# 2
def pretty_print(data: list[object], side: str = "-", delimiter: str = "|") -> None:
    data_string = (
        f"{delimiter} "
        + f" {delimiter} ".join(str(item) for item in data)
        + f" {delimiter}"
    )
    line = " " + side * (len(data_string) - 2) + " "

    print(line, "\n", data_string, "\n", line)
