from ObservableObjects import *
from varname import *

# STAGE 0 - DEFINE TEST CLASSES
# INSTANCE OF CLASS 'A' WILL TRIGGER PROPERTY CHANGED EVENT EVERY TIME ITS ATTRIBUTE CHANGES
# INSTANCE OF CLASS 'B' WILL SUBSCRIBE TO THE CHANGES OF CLASS 'A' ATTRIBUTE AND RECEIVE NEW VALUES


class A(ObservableObject):
    def __init__(self):
        # Attribute 'a' will have property changed events triggered every time its value changes
        self.a = 1


class B(ObserverObject):
    def __init__(self):
        # Attribute 'b_1' will receive value from attribute 'A.a', every time 'A.a' triggers property changed event
        self.b_1 = 1
        # 'b_2' will also receive value from 'A.a', but not directly (with the use of 'setStrValue' method)
        self.b_2 = '1'

    def setStrValue(self, value):
        self.b_2 = str(value)


if __name__ == '__main__':
    # Initialize class instances
    A_instance = A()
    B_instance = B()

    # STAGE 1 - SUBSCRIBE TO DESIRED VARIABLE FROM ANOTHER OBJECT
    # Subscription for 'B' class' 'b_1' attribute is made directly. The 'setter_method_name' and 'getter_method_name'
    # are 'None' which means the 'setattr' and 'getattr' functions are used.
    B_instance.subscribeToVariable(dst_property_name=nameof(B_instance.b_1), setter_method_name=None,
                                   src_obj=A_instance, src_property_name=nameof(A_instance.a), getter_method_name=None)
    # Subscription for 'B' class' 'b_2' attribute is made indirectly. The 'setter_method_name' is not 'None'. The setter
    # method specified is a property of class, not the attribute, so the 'dst_property_name' is None in this case.
    B_instance.subscribeToVariable(dst_property_name=None, setter_method_name=nameof(B_instance.setStrValue),
                                   src_obj=A_instance, src_property_name=nameof(A_instance.a), getter_method_name=None)

    # Now the 'B_instance' object will automatically receive updates for its attributes based on the subscriptions made
    # - every time the 'A_instance' object triggers property changed event for its subscribed attribute

    # DO SOME TESTS:
    for _ in range(9):
        # Print all relevant attributes
        print('a: ' + str(A_instance.a) + ' | b_1: ' + str(B_instance.b_1) + ' | b_2: ' + B_instance.b_2)
        # Change registered attribute value
        A_instance.a += 1
        # STAGE 2 - TRIGGER PROPERTY CHANGED EVENT
        A_instance.publishPropertyChanges(nameof(A_instance.a))

    """
    The output: 
    a: 1 | b_1: 1 | b_2: 1
    a: 2 | b_1: 2 | b_2: 2
    a: 3 | b_1: 3 | b_2: 3
    a: 4 | b_1: 4 | b_2: 4
    a: 5 | b_1: 5 | b_2: 5
    a: 6 | b_1: 6 | b_2: 6
    a: 7 | b_1: 7 | b_2: 7
    a: 8 | b_1: 8 | b_2: 8
    a: 9 | b_1: 9 | b_2: 9
    """