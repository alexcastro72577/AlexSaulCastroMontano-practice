class Calculator:
    def add(self, val1, val2):
        return val1 + val2

    def valid_age(self, value):
        return 0 < value < 100

    def max(self, numbers):
        max=numbers[0]
        for number in numbers:
            if number > max:
                max = number
        return max

    def isVocal(self, letter):
        if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            answer = "vocal"
            return answer
        if letter=="1" or letter=="2" or letter=="3" or letter=="4" or letter=="5" \
                or letter=="6" or letter=="7" or letter=="8" or letter=="9" or letter=="0":
            answer = "number"
            return answer
        else:
            answer = "consonant"
            return answer

    def inversa(self, message):
        answer=""
        for letra in message:
            answer = letra + answer
        return answer

    def palindromo(self, message):
        answer = ""
        for letra in message:
            answer = letra + answer
        return message == answer

    def change(self, numbers):
        max = numbers[0]
        min = numbers[0]
        for number in numbers:
            if number > max:
                max = number
        for number in numbers:
            if number < min:
                min = number
        prom = sum(numbers) / len(numbers)
        return max, min, prom

    def country(self, countries):
        max = 0
        answer = ""
        for country in countries:
            num= len(country)
            if num > max:
                max=num
                answer=country
        return answer

    def binary(self, number):
        binario = ''
        while number // 2 != 0:
            binario = str(number % 2) + binario
            number = number // 2
            answer=str(number) + binario
        return int(answer)

    def countChar(self, message):
        count = 0
        for i in message:
            count = count + 1
        return count
