# python_observable_objects
Publisher/Observer pattern for python objects to synchronize data in the background with the use of event-driven callbacks mechanism.

# modules created:
Useful modules to implement background data synchronization between objects:
- Utilities.py - contains definition of 'PropertyChangedEventHandler' class used to manage the event-driven callbacks mechanism
- ObservableObjects.py - contains definitions of 'ObservableObject' and 'ObserverObject' classes used to create objects that can easily register attributes for publishing their values' changes and subscribe to those changes (for receiving value updates automatically). 'Utilities.py' is a dependency for 'ObservableObjects.py'.

# modules containing examples of usage:
Simple presentation of solution:
- testing.py - simple data synchronization setup between 2 instances of classes that inherit from 'ObservableObject' and 'ObserverObject' class
-----------------------------------------------------------------------------------------------------------------------------------------------
Framework for creating PyQt5 GUI python applications in a model similar to C# MVVM (Model, View, ViewModel):
- DataModels.py - contains definition of object(s) that receive raw data unprepared for visualization
- ViewModels.py - contains definition of object(s) that store (lists of) 'DataModels' object(s) and perform necessary data transformations to prepare it to visualization. These transformations are often done by 'getter'/'setter' custom functions assigned to python properties - exposed attributes that act like an interface for interacting with internal variables - e.g. from data models stored. 
- Views.py - contains definition of PyQt5 GUI objects. Data to be displayed with the use of these objects comes from view models object(s).

In this case, Views.py contains also a few lines of execution code to present some solution - in-background synchronization between plain attributes (e.g. strings) and PyQt5 objects (e.g. QLabels). When the value of the string attribute of view model object changes, a property changed event is triggered and the new value is automatically set to the QLabel.
Also there is a solution for one consistent way of providing values FROM input GUI objects (like QLineEdits) TO plain variables - using PyQt5 signal slots. 
The two above are done using Utilities.py and ObservableObjects.py modules.

