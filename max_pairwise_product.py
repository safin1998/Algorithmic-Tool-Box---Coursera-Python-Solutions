# python3


''' def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
'''

def max_product(numbers):
    biggest=0
    for i in numbers:
        if biggest < i:
            biggest=i
    numbers.remove(biggest)
    
    s_biggest=0
    for i in numbers:
        if s_biggest < i:
            s_biggest=i
    product=biggest * s_biggest

    return product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_product(input_numbers))
    
