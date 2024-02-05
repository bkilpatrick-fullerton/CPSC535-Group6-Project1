# CPSC535-Group6-Project1
## Group Project: Algorithm Efficiency Analyzer Tool
### Due Date: Feb 8th 11:59pm

### Roles
- Algo - Neema (and Asad?)
- Gui - Mrunal 
- Data visualization - Akshay 
- Documentation - Adam
- Project coordinator - Brandon

### Algo - Neema (and Asad?)
- **Version 1 Due Date:** Saturday Feb 3rd
- **Module Name(s):** SortingAlgos.py
- **Librarys needed:** none (only standard libraries)
- **Funtion/Class Definitions:** NOTE: CURRENT FILE NEEDS TO BE FILLED OUT WITH ACTUAL ALGO IMPLEMENTATIONS (currently just uses the list sort() function the time.sleep() function to simulate)
   - **Name:** Function: (algoname)_sort (Ex "bubble_sort")
   - **Description:** sorts the input array list in-place
   - **Input:** param1 "arr" = a List of unsorted integers
   - **Output:** none
- 
   - **Name:** Function: quick_select 
   - **Description:** finds and returns the "k"th element
   - **Input:** param1 "arr" = a List of unsorted integers
                param2 "kth" = an integer (between 0 and len(arr) - 1)
   - **Output:** integer kth element of the "arr"

### Visualizaion - Akshay
- **Version 1 Due Date:** Saturday Feb 3rd
- **Module Name(s):** GraphViz.py
- **Librarys needed:** must have matplotlib.pyplot, numpy installed
- **Funtion/Class Definitions:** 
   - **Name:** Class: BarGraph()
   - **Description:** wraps the pyplot.plt class which displays a bar graph based on two list arrays (x/y data)
   - **Properties:** .data = a Dict or for {(str)_algoname : (double) _time} (time is in milliseconds)
                     .x_label/.y_label/.title = text labels for the x-axis, y-axis and graph title repecitively
   - **Methods:** .show_graph() = call this method after setting the above properties to show the bargraph

### GUI - Mrunal
- **Version 1 Due Date:** Saturday Feb 3rd
- **Module Name(s):** AlgorithmAnalyzer
- **Librarys needed:** must have tkinter installed
- **Notes on using the Gui:** click the "generate" button to generate a random list (between 20-50 elements) of Ints between (0-99) AND a "k"th value (used to test the quick_select algorithm).  Then click the Graph/Sort button to show (1) the sorted list, (2) the "k"th value, and (3) a bargraph showing the runtime (in milliseconds) of the 8 required algorithms

### Doumentation - Adam
- **Version 1 Due Date:** Sunday Feb 4th

### Tests Cases - Adam/Brandon/Others?
- for Algos - This could be a Module with coded unit tests (ex code that calls each sorting algo function with a known array and compares that array to presorted array to verify proper sorting)
- for GUi/Visualization - Mabye this is just a description of manual tests performed (data entered through gui, expected output and observed output - including edge cases (?) 
