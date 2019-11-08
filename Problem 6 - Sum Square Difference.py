def sum_of_squares(n):
    sum_squares = (n*(n+1)*(2*n+1))/6
    print(sum_squares)
    return sum_squares


def square_of_sum(n):
    nat_sum = sum(range(1, n+1))
    square_sum = nat_sum * nat_sum
    print(square_sum)
    return square_sum


goal = int(input())

number = square_of_sum(goal) - sum_of_squares(goal)

print(number)
