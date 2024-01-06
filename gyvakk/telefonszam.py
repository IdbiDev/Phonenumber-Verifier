from Exepctions import *
import re
import random

szolgaltatok = {"20": "Yettel", "30": "Telekom", "70": "Vodafone", "50": "Digi"}
regex = re.compile(r"^[0-9]+$")


class PhonenumberGenerator:
    def __init__(self, invalid=0, valid=10):
        self.uwu = self.makeRangedNumbers(invalid=invalid, valid=valid)
        f = open("telefonszamok.txt", "w+")
        [f.write(x.number + "\n") for x in self.uwu]

    def makeNumber(self):
        service = random.randint(1, 8)
        useplus = random.random()
        lenght = random.randint(1000000, 9999999)
        result = ""
        if useplus > 0.5:
            result += "+" + str(random.randint(34, 38))
        else:
            result += "0" + str(random.randint(5, 7))
        result += str(service) + "0" + str(lenght)

        return Phonenumber(result)

    def makeRangedNumbers(self, invalid=0, valid=10):
        ret = []
        invalid_counter = 0
        valid_counter = 0
        # Ez simán lehet while True loop, ha olyan szerencsés vagy :)
        while invalid > invalid_counter or valid > valid_counter:
            c_number = self.makeNumber()
            c_type = c_number.getService()

            if c_type == "Invalid" and invalid_counter < invalid:
                invalid_counter += 1
                ret.append(c_number)
            elif valid > valid_counter and not (c_type == "Invalid"):
                valid_counter += 1
                ret.append(c_number)

        return ret


class Phonenumber:
    def __init__(self, number: str):
        self.number = number
        self.szolgaltato = None
        self.trimmedNumber = None

    def __str__(self):
        return f"{self.number}: Szolgáltató: {self.getService()}"

    def classifyNumber(self):
        if not regex.match(self.number.replace("+", "")):
            raise InvalidPhoneNumber("A telefonszám nem tartalmazhat betűket,különleges karaktereket, kivéve a '+'-t")

        if len(self.number) == 12 and self.number.startswith("+36") or len(
                self.number) == 11 and self.number.startswith("06"):
            if len(self.number) == 12:
                self.trimmedNumber = self.number.replace("+36", "", 1)
            else:
                self.trimmedNumber = self.number.replace("06", "", 1)
            if (self.trimmedNumber[0:2]) in szolgaltatok.keys():
                self.szolgaltato = szolgaltatok[self.trimmedNumber[0:2]]
            else:
                raise InvalidPhoneService("Ez a szolgáltató nem létezik!")
        else:
            if not (self.number.startswith("+36") or self.number.startswith("06")):
                raise InvalidPhoneNumber("A telefonszám nem magyar, vagy ismeretlen!")
            raise InvalidPhoneNumber("A telefonszám hossza nem megfelelő")
        return self.szolgaltato

    def getService(self) -> str:
        try:
            return self.classifyNumber()
        except InvalidPhoneNumber as e:
            return "Invalid"
        except InvalidPhoneService as e:
            return "Invalid"


# Életem legértelmesebb functionja
def replaceStrWithNumber(string, number: str):
    ret = list(string)
    for k, v in enumerate(ret):
        try:
            ret[k] = number[k]
        except Exception:
            ret[k] = " "
    return "".join(ret)


SessionData = []
data = None
while True:
    userInput = input("Kérem a parancsot > ")
    if userInput.lower() == "txt":
        userInput = input("txt > ")
        if userInput.lower() == "random":
            data = PhonenumberGenerator(invalid=10, valid=50)
            for phones in data.uwu:
                print(f"{phones.number}: {phones.getService()}")
                SessionData.append(phones)
        elif userInput.lower() == "back":
            continue
        else:
            try:
                data = open(userInput)
                for phones in data:
                    num = Phonenumber(phones)
                    print(f"{num.number}: {num.getService()}")
                    SessionData.append(num)
            except FileNotFoundError:
                print("File nem található")
    elif userInput.lower() == "input":
        data = input("Ellenőrizni kívánt telefonszám:")
        p = Phonenumber(data)
        print(f"{p.number}: {p.classifyNumber()}")

    elif userInput.lower() == "exit":
        exit("Program bezárva!")
    elif userInput.lower() == "stats":

        countedElements = {"Yettel": 0, "Telekom": 0, "Vodafone": 0, "Digi": 0, "Invalid": 0}
        for phone in SessionData:
            print(phone)
            countedElements[phone.getService()] += 1
        print(
            f"\nÖsszegzés:\n| Yettel | Telekom | Vodafone | Digi | Ismeretlen |\n| {replaceStrWithNumber('Yettel', str(countedElements['Yettel']))} | {replaceStrWithNumber('Telekom', str(countedElements['Telekom']))} | {replaceStrWithNumber('Vodafone', str(countedElements['Vodafone']))} | {replaceStrWithNumber('Digi', str(countedElements['Digi']))} | {replaceStrWithNumber('Ismeretlen', str(countedElements['Invalid']))} |")
        print(
            f"Összesen {countedElements['Yettel'] + countedElements['Telekom'] + countedElements['Vodafone'] + countedElements['Digi']} db valós telefonszám van, {countedElements['Invalid']} db hibás!")
    elif userInput.lower() == "clear":
        SessionData.clear()
        print("Statisztikai memória törölve!")
    elif userInput.lower() == "export":
        with open("phonenumbers_export.txt", "x+") as f:
            for phone in SessionData:
                f.write(f"{phone.number},{phone.getService()}\n")
    else:
        print("Ismeretlen parancs")
