def extract_sublists(numbers):
    sublists = []
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] > numbers[j]:
                if i < j:
                    sublists.append(numbers[i+1:j])
                elif i > j:
                    sublists.append(numbers[j+1:i])
    return sublists

# Example usage
numbers = [20, 50, 60, 30]
sublists = extract_sublists(numbers)
print(sublists)
