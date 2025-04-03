def fizz_buzz(n):
    answer = []
    for i in range(1, n+1):
        if i % 15 == 0:  # Optimized check for divisibility by both 3 and 5
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

# Example usage
n = 15
print(fizz_buzz(n))
# Output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']