# Sample string for demonstration
text = "hello"

# 1. __add__ (Concatenate strings)
print(text.__add__(" world"))  # Output: 'hello world'

# 2. __class__ (Get the class of the object)
print(text.__class__)  # Output: <class 'str'>

# 3. __contains__ (Check if substring is present)
print(text.__contains__('he'))  # Output: True

# 4. __delattr__ (Delete an attribute, typically for custom objects)
class Example:
    def __init__(self):
        self.attr = 'value'
        
example = Example()
delattr(example, 'attr')  # This deletes 'attr'
# print(example.attr)  # Raises AttributeError

# 5. __dir__ (List all attributes of the object)
print(text.__dir__())  # Output: List of attributes and methods of str

# 6. __doc__ (Get the docstring of the object)
print(str.__doc__)  # Output: Documentation of the str class

# 7. __eq__ (Check equality)
print(text.__eq__("hello"))  # Output: True

# 8. __format__ (Format a string)
print("{:>10}".format(text))  # Output: '     hello'

# 9. __ge__ (Greater than or equal to)
print(text.__ge__("abc"))  # Output: True

# 10. __getattribute__ (Get attribute of the object)
print(text.__getattribute__('upper'))  # Output: <built-in method upper>

# 11. __getitem__ (Get item by index)
print(text.__getitem__(1))  # Output: 'e'

# 12. __getnewargs__ (Returns arguments for object creation in pickling)
print(text.__getnewargs__())  # Output: ('hello',)

# 13. __gt__ (Greater than comparison)
print(text.__gt__("abc"))  # Output: True

# 14. __hash__ (Returns the hash value of the object)
print(text.__hash__())  # Output: Hash value (varies)

# 15. __init__ (Constructor, initialized in class definition)
# Covered in custom classes, e.g., class Car above.

# 16. __init_subclass__ (Called when a class is subclassed)
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Subclass created: {cls.__name__}")

class Derived(Base):
    pass  # Output: Subclass created: Derived

# 17. __iter__ (Returns iterator)
iterator = text.__iter__()
print(next(iterator))  # Output: 'h'

# 18. __le__ (Less than or equal to comparison)
print(text.__le__("world"))  # Output: True

# 19. __len__ (Length of string)
print(text.__len__())  # Output: 5

# 20. __lt__ (Less than comparison)
print(text.__lt__("world"))  # Output: True

# 21. __mod__ (String interpolation using `%`)
print("I am %s" % text.__mod__(text))  # Output: 'I am hello'

# 22. __mul__ (String repetition)
print(text.__mul__(3))  # Output: 'hellohellohello'

# 23. __ne__ (Not equal comparison)
print(text.__ne__("world"))  # Output: True

# 24. __new__ (Creates a new instance of a class)
# Typically used in custom classes.

# 25. __reduce__ (Used for pickling)
# Typically used in pickling, see pickle module.

# 26. __reduce_ex__ (Extension of __reduce__ for pickling)
# Related to serialization, see pickle module.

# 27. __repr__ (String representation of object)
print(text.__repr__())  # Output: "'hello'"

# 28. __rmod__ (Reverse mod, `%` operator)
print("%s" % text.__rmod__(text))  # Output: 'hello'

# 29. __rmul__ (Reverse multiply for strings)
print(text.__rmul__(2))  # Output: 'hellohello'

# 30. __setattr__ (Set attribute value)
# Typically used in custom objects, e.g., setattr(object, name, value).

# 31. __sizeof__ (Returns the size of the object)
print(text.__sizeof__())  # Output: Size in bytes

# 32. __str__ (String representation)
print(text.__str__())  # Output: 'hello'

# 33. __subclasshook__ (Customizes issubclass behavior)
# Typically used with abstract base classes.

### String Methods:
# 34. capitalize
print(text.capitalize())  # Output: 'Hello'

# 35. casefold
print(text.casefold())  # Output: 'hello' (lowercase)

# 36. center
print(text.center(10, "-"))  # Output: '--hello---'

# 37. count
print(text.count("l"))  # Output: 2

# 38. encode
print(text.encode())  # Output: b'hello' (in bytes)

# 39. endswith
print(text.endswith("o"))  # Output: True

# 40. expandtabs
tab_text = "hello\tworld"
print(tab_text.expandtabs(4))  # Output: 'hello   world'

# 41. find
print(text.find("l"))  # Output: 2

# 42. format
print("Hello, {}".format("world"))  # Output: 'Hello, world'

# 43. format_map
print("{name}".format_map({'name': 'world'}))  # Output: 'world'

# 44. index
print(text.index("l"))  # Output: 2

# 45. isalnum
print(text.isalnum())  # Output: False

# 46. isalpha
print(text.isalpha())  # Output: True

# 47. isascii
print(text.isascii())  # Output: True

# 48. isdecimal
print("123".isdecimal())  # Output: True

# 49. isdigit
print("123".isdigit())  # Output: True

# 50. isidentifier
print("var_1".isidentifier())  # Output: True

# 51. islower
print(text.islower())  # Output: True

# 52. isnumeric
print("123".isnumeric())  # Output: True

# 53. isprintable
print(text.isprintable())  # Output: True

# 54. isspace
print("   ".isspace())  # Output: True

# 55. istitle
print("Hello World".istitle())  # Output: True

# 56. isupper
print(text.isupper())  # Output: False

# 57. join
print(",".join(["a", "b", "c"]))  # Output: 'a,b,c'

# 58. ljust
print(text.ljust(10, '-'))  # Output: 'hello-----'

# 59. lower
print(text.lower())  # Output: 'hello'

# 60. lstrip
print("   hello".lstrip())  # Output: 'hello'

# 61. maketrans
trans = str.maketrans("h", "H")
print(text.translate(trans))  # Output: 'Hello'

# 62. partition
print(text.partition("l"))  # Output: ('he', 'l', 'lo')

# 63. removeprefix
print("Mr. John".removeprefix("Mr. "))  # Output: 'John'

# 64. removesuffix
print("hello.py".removesuffix(".py"))  # Output: 'hello'

# 65. replace
print(text.replace("l", "L"))  # Output: 'heLLo'

# 66. rfind
print(text.rfind("l"))  # Output: 3

# 67. rindex
print(text.rindex("l"))  # Output: 3

# 68. rjust
print(text.rjust(10, '-'))  # Output: '-----hello'

# 69. rpartition
print(text.rpartition("l"))  # Output: ('hel', 'l', 'o')

# 70. rsplit
print(text.rsplit("l"))  # Output: ['he', '', 'o']

# 71. rstrip
print("hello   ".rstrip())  # Output: 'hello'

# 72. split
print(text.split("l"))  # Output: ['he', '', 'o']

# 73. splitlines
print("hello\nworld".splitlines())  # Output: ['hello', 'world']

# 74. startswith
print(text.startswith("he"))  # Output: True

# 75. strip
print("  hello  ".strip())  # Output: 'hello'

# 76. swapcase
print(text.swapcase())  # Output: 'HELLO'

# 77. title
print("hello world".title())  # Output: 'Hello World'

# 78. translate
print(text.translate(trans))  # Output:

