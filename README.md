# Python Tasks
_Woman In AI Course_

### 1. Define the Function
Create the apply_operation function with the following signature:

```python
def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.
    
    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]
