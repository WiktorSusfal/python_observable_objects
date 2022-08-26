from ObservableObjects import *
from varname import *

# STAGE 0 - DEFINE TEST CLASSES
# INSTANCE OF CLASS 'A' WILL TRIGGER PROPERTY CHANGED EVENT EVERY TIME ITS ATTRIBUTE CHANGES
# INSTANCE OF CLASS 'B' WILL SUBSCRIBE TO THE CHANGES OF CLASS 'A' ATTRIBUTE AND RECEIVE NEW VALUES


class A(ObservableObject):
    def __init__(self):
        # Attribute 'a' will be registered as a publisher for property changed events
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

    # STAGE 1 - REGISTER VARIABLE THAT NEEDS TO BE OBSERVED
    A_instance.registerProperty(nameof(A_instance.a))

    # STAGE 2 - SUBSCRIBE TO DESIRED VARIABLE FROM ANOTHER OBJECT
    # Subscription for 'B' class' 'b_1' attribute is made directly. The 'setter_method_name' and 'getter_method_name'
    # are 'None' which means the 'setattr' and 'getattr' functions are used.
    B_instance.subscribeToVariable(dst_property_name=nameof(B_instance.b_1), setter_method_name=None,
                                   src_obj=A_instance, src_property_name=nameof(A_instance.a), getter_method_name=None)
    # Subscription for 'B' class' 'b_2' attribute is made indirectly. The 'setter_method_name' is not 'None'. The setter
    # method specified is a property of class, not the attribute, so the 'dst_property_name' is None in this case.
    B_instance.subscribeToVariable(dst_property_name=None, setter_method_name=nameof(B_instance.setStrValue),
                                   src_obj=A_instance, src_property_name=nameof(A_instance.a), getter_method_name=None)

    # Now the 'B_instance' object will automatically receive updates for its attributes based on the subscriptions made
    # - every time the 'A_instance' object triggers property changed event for its registered attribute

    # DO SOME TESTS:
    for _ in range(9):
        # Print all relevant attributes
        print('Aa.a: ' + str(A_instance.a) + ' | Bb.b: ' + str(B_instance.b_1) + ' | Bb.c: ' + B_instance.b_2)
        # Change registered attribute value
        A_instance.a += 1
        # STAGE 3 - TRIGGER PROPERTY CHANGED EVENT
        A_instance.publishPropertyChanges(nameof(A_instance.a))
