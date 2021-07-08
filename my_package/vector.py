class Vector:
    def __init__(self, args):
        if isinstance(args, int):
            self._coords = [0] * args
        else:
            self._coords = args


        # if arg is an int(dimension)
        #if isinstance(args[0], int):
        #self._coords = [0 for i in range(0, *args)]
        #print (_coords)
        #for x in *args:
        #    self._coords.append(x)

    def __len__(self):
        return len(self._coords)

        # return the dimension of the vector

    def __getitem__(self, j):
        return(self._coords[j])# return the jth coordinate of the vector

    def __setitem__(self, j, val):
        self._coords[j] = val
        # set the jth coordinate of vector to val

    def __add__(self, other):
        if len(self._coords) != len(other._coords):
            print("ADDITION OF DIFFERENT DIMENSION VECTORS NOT POSSIBLE")
        else:
            z = []
            for i in range(len(self)):
                z.append(self._coords[i] + other._coords[i])
            return Vector(z)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self._coords)):
                if self._coords[i] != other._coords[i]:
                    return False
        return True
        # return True if vector has same coordinates as other

    def __ne__(self, other):
        return not self.__eq__(other)
                # return True if vector differs from other

    def __str__(self):
        s = '<'
        for i in self._coords:
            s += str(i) + ', '
        s = s[:-2]
        s += '>'
        return s
        # return the string representation of a vector within <>

    def __sub__(self, other):
        if len(self._coords) != len(other._coords):
            print("SUBTRACTION OF DIFFERENT DIMENSION VECTORS NOT POSSIBLE")
        else:
            z = []
            for i in range(len(self)):
                z.append(self._coords[i] - other._coords[i])
            return Vector(z)
        # Soln for Qs. 2

    def __neg__(self):
        z = []
        for i in range(len(self._coords)):
            z.append(-self._coords[i])
        return Vector(z)
        # Soln for Qs. 3

    def __rmul__(self, value):
        z = []
        for i in range(len(self._coords)):
            z.append(self._coords[i]*value)
        return Vector(z)
        #return (self * value)

    def __mul__(self, other):
        z=0
        if isinstance(other, int):
            return self.__rmul__(other)
        if len(self._coords) != len(other._coords):
            print("MULTIPLICATION OF DIFFERENT DIMENSION VECTORS NOT POSSIBLE")
        else:
            for i in range(len(self)):
                z += self._coords[i]*other._coords[i]
            return z
        # Soln for Qs. 4, 5 and 6

def main():
    v1 = Vector(5)
    v2 = Vector ([7])
    v3 = Vector([1,2,3,4,5])
    v5 = Vector([8,3,-1,-3,1])
    v4 = Vector([9,5,2,1,6])
    v6 = Vector([1,1,1,1,1])
    print(v4-v5)
    print(-v5)
    print(v4+v6)
    print(v1*v3)
    print(4*v6)
    # Add suitable print statements to display the results
    # of the different question segments


if __name__ == '__main__':
    main()
