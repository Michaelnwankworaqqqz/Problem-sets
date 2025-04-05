class Jar:
    # __init__ should initialize a cookie jar with the given capacity,
    #  which represents the maximum number of cookies that can fit in the cookie jar.
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size


    # __str__ should return a str with 🍪, where n is the number of cookies in the cookie jar.
    # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    def __str__(self):
        return f"{'🍪' * self.size}"


    #deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
    # though, deposit should instead raise a ValueError.
    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Addition of cookies to cookie jar exceeds cookie jar capacity")
        elif n > self.capacity:
            raise ValueError("New additional cookies exceeds cookie jar capacity")
        else:
            self.size += n


    # Withdraw should remove n cookies from the cookie jar. Nom nom nom.
    # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There aren't that many cookies in the cookie jar")
        else:
            self.size -= n

    #capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity


    # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("ValueError")
        self._capacity = capacity

    # Size should return the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size



def main():
    # Initialize class object
    jar = Jar(12, 0)


    # Prompt user for input
    deposition = int(input("number of 🍪 you want to deposit: "))
    withdrawal = int(input("number of 🍪 you want to withdraw: "))


    # Call deposit and withdraw methods via try and use except to raise ValueError
    try:
        jar.deposit(deposition)
        jar.withdraw(withdrawal)
    except ValueError as e:
        print(e)


    # Output
    print(jar)

if __name__ == "__main__":
    main()
