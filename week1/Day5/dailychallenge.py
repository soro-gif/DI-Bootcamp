import math
from functools import wraps


def circle_factory(func):
    """
    Decorator that allows creating a Circle from either radius or diameter.
    Usage: @circle_factory on __init__ allows passing either 'radius=' or 'diameter='
    """
    @wraps(func)
    def wrapper(self, radius=None, diameter=None):
        if radius is not None:
            func(self, radius)
        elif diameter is not None:
            func(self, diameter / 2)
        else:
            raise ValueError("Either 'radius' or 'diameter' must be specified")
    return wrapper


class Circle:
    """A class representing a geometric circle with various operations."""
    
    def __init__(self, radius=None, diameter=None):
        """
        Initialize a Circle with either radius or diameter.
        
        Args:
            radius (float): The radius of the circle
            diameter (float): The diameter of the circle (will be converted to radius)
        
        Raises:
            ValueError: If neither radius nor diameter is provided
        """
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either 'radius' or 'diameter' must be specified")
    
    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self.radius * 2
    
    @property
    def area(self):
        """Compute and return the area of the circle."""
        return math.pi * self.radius ** 2
    
    def __str__(self):
        """
        Dunder method for human-readable string representation.
        Returns a formatted string with circle attributes.
        """
        return (f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, "
                f"area={self.area:.2f})")
    
    def __repr__(self):
        """
        Dunder method for official string representation.
        Returns a string that could recreate the object.
        """
        return f"Circle(radius={self.radius})"
    
    def __add__(self, other):
        """
        Dunder method to add two circles.
        Returns a new circle with radius equal to the sum of both radii.
        
        Args:
            other (Circle): Another Circle instance
        
        Returns:
            Circle: A new Circle with combined radius
        """
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot add Circle and {type(other).__name__}")
        
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)
    
    def __gt__(self, other):
        """
        Dunder method to compare if this circle is greater than another.
        Compares based on radius.
        
        Args:
            other (Circle): Another Circle instance
        
        Returns:
            bool: True if this circle's radius is greater
        """
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot compare Circle and {type(other).__name__}")
        
        return self.radius > other.radius
    
    def __lt__(self, other):
        """
        Dunder method to compare if this circle is less than another.
        Compares based on radius.
        
        Args:
            other (Circle): Another Circle instance
        
        Returns:
            bool: True if this circle's radius is smaller
        """
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot compare Circle and {type(other).__name__}")
        
        return self.radius < other.radius
    
    def __eq__(self, other):
        """
        Dunder method to check equality between two circles.
        Circles are equal if they have the same radius (within floating point precision).
        
        Args:
            other (Circle): Another Circle instance
        
        Returns:
            bool: True if circles have equal radius
        """
        if not isinstance(other, Circle):
            return False
        
        return math.isclose(self.radius, other.radius, rel_tol=1e-9)
    
    def __le__(self, other):
        """Dunder method for less than or equal comparison."""
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot compare Circle and {type(other).__name__}")
        return self.radius <= other.radius
    
    def __ge__(self, other):
        """Dunder method for greater than or equal comparison."""
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot compare Circle and {type(other).__name__}")
        return self.radius >= other.radius
    
    def __ne__(self, other):
        """Dunder method for not equal comparison."""
        return not self.__eq__(other)



# Test Suite


if __name__ == "__main__":
   
    print("CIRCLE CLASS - OOP & DUNDER METHODS DEMONSTRATION")
    
    
    # Create circles using radius
    print("\n1. Creating circles with radius:")
    c1 = Circle(radius=5)
    c2 = Circle(radius=3)
    c3 = Circle(radius=5)
    
    print(f"   c1: {c1}")
    print(f"   c2: {c2}")
    print(f"   c3: {c3}")
    
    # Create circles using diameter
    print("\n2. Creating circles with diameter:")
    c4 = Circle(diameter=20)  # radius = 10
    print(f"   Circle with diameter 20: {c4}")
    
    # Query radius and diameter
    print("\n3. Querying radius and diameter:")
    print(f"   c1 radius: {c1.radius}, diameter: {c1.diameter}")
    print(f"   c4 radius: {c4.radius}, diameter: {c4.diameter}")
    
    # Area computation
    print("\n4. Computing area:")
    print(f"   Area of c1 (radius=5): {c1.area:.4f}")
    print(f"   Area of c2 (radius=3): {c2.area:.4f}")
    
    # String representation (__str__ and __repr__)
    print("\n5. String representations:")
    print(f"   __str__: {str(c1)}")
    print(f"   __repr__: {repr(c1)}")
    
    # Addition of circles (__add__)
    print("\n6. Adding circles (__add__):")
    c_sum = c1 + c2
    print(f"   c1 + c2 = {c_sum}")
    print(f"   (radius {c1.radius} + radius {c2.radius} = radius {c_sum.radius})")
    
    # Comparison - greater than (__gt__)
    print("\n7. Comparing circles - greater than (__gt__):")
    print(f"   c1 > c2: {c1 > c2} (radius {c1.radius} > {c2.radius})")
    print(f"   c2 > c1: {c2 > c1} (radius {c2.radius} > {c1.radius})")
    
    # Comparison - less than (__lt__)
    print("\n8. Comparing circles - less than (__lt__):")
    print(f"   c2 < c1: {c2 < c1} (radius {c2.radius} < {c1.radius})")
    print(f"   c1 < c4: {c1 < c4} (radius {c1.radius} < {c4.radius})")
    
    # Equality comparison (__eq__)
    print("\n9. Equality comparison (__eq__):")
    print(f"   c1 == c3: {c1 == c3} (both have radius {c1.radius})")
    print(f"   c1 == c2: {c1 == c2} (radius {c1.radius} != {c2.radius})")
    print(f"   c1 != c2: {c1 != c2}")
    
    # Sorting circles (__lt__)
    print("\n10. Sorting circles:")
    circles = [c4, c1, c2, Circle(radius=7), Circle(radius=2)]
    print(f"    Original: {[c.radius for c in circles]}")
    sorted_circles = sorted(circles)
    print(f"    Sorted:   {[c.radius for c in sorted_circles]}")
    print("    Details:")
    for i, circle in enumerate(sorted_circles, 1):
        print(f"      {i}. {circle}")
    
    # All comparison methods
    print("\n11. All comparison methods:")
    print(f"    c1 <= c4: {c1 <= c4}")
    print(f"    c1 >= c3: {c1 >= c3}")
    print(f"    c2 <= c1: {c2 <= c1}")
    
  
  

