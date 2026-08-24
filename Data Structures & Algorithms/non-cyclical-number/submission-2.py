class Solution:
    def isHappy(self, n: int) -> bool:

        digit = 0  #variable to store digit, rewritten every iteration
        sum_squares = 0  #variable to store sum of squares, rewritten for every new calc
        squares = set()

        while n != 0:

            sum_squares = 0

            while n > 0:
                digit = n % 10
                sum_squares += digit ** 2
                n = n // 10

            if sum_squares in squares:
                return False

            squares.add(sum_squares)

            if sum_squares == 1:
                return True

            n = sum_squares

            
                
                
        

        