""" Algorithm Analyzer"""
from tkinter import *
from tkinter import ttk
import random as rd
import SortingAlgos as algos
import GraphViz as viz
import time
import customtkinter
from PIL import Image, ImageTk

GEN_LIST_MIN = 50
GEN_LIST_MAX = 50
GEN_INT_MIN = 0
GEN_INT_MAX = 99

class Timer:
    """simple Timer class to time algo function calls in milleseconds"""
    def __init__(self):
        self.start_time = 0
    def start(self):
        self.start_time = time.perf_counter()
    def end(self):
        return (time.perf_counter() - self.start_time) * 1000 #return in millisecond (perf_counter is in seconds)


def click_generate():
    """called when the "generate" button is clicked, 
    generates a random list of ints, and displays it in the entry box"""
    global kth # one of our sorting algos (quick_select) finds the kth value in an unsorted array, we'll generate this as well

    generated_list.clear() #clear the existing list
    
    list_length = rd.randint(GEN_LIST_MIN,GEN_LIST_MAX) # get a random array length
    for _ in range(list_length):
        generated_list.append(rd.randint(GEN_INT_MIN,GEN_INT_MAX)) #generate random int list

    label_generated_list.configure(text=str(generated_list)) # display list in the input box

    kth = rd.randint(0,GEN_LIST_MAX-1) #chose a "k" for the quick_select algo
    label_kth.configure(text = f"k={kth}") # display the generated k


def click_graph():
    """called when the "Sort/Graph" button is clicked, loops through the algos (the algos return the execution time)"""
    if (generated_list):
        
        timer = Timer() #create a simple millisecond timer       
        
        graph_data = {} # clear the dictionary used to store the graph data
        input_list = [] # will refresh this with the generated/unsorted list and feed it to each sorting algo
        
        
        """TODO These algo function calls should probably be in a loop to reduce repeated code/ improve readability"""
        # BUBBLE SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.bubble_sort(input_list) # pass in the unsorted_list
        sorted_list = input_list[:] #save this sorted list for display later (we'll only do this once)
        graph_data["bubble_sort"] = timer.end()

        # MERGE SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.merge_sort(input_list) # pass in the unsorted_list
        graph_data["merge_sort"] = timer.end()

        # QUICK SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.quick_sort(input_list) # pass in the unsorted_list
        graph_data["quick_sort"] = timer.end()

        # HEAP SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.heap_sort(input_list) # pass in the unsorted_list
        graph_data["heap_sort"] = timer.end()

        # COUNTING SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.counting_sort(input_list) # pass in the unsorted_list
        graph_data["counting_sort"] = timer.end()

        # RADIX SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.merge_sort(input_list) # pass in the unsorted_list
        graph_data["radix_sort"] = timer.end()

        # QUICK SELECT (don't run this one last)
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        kth_value = algos.quick_select(input_list,kth) # pass in the unsorted_list
        graph_data["quick_select"] = timer.end()

        # BUCKET SORT
        timer.start()
        input_list = generated_list[:] # copy the unsorted_list
        algos.bucket_sort(input_list) # pass in the unsorted_list
        graph_data["bucket_sort"] = timer.end()

       

        #Display the sorted list in the main GUI
        label_sorted_list.config(text=str(sorted_list)) #note this list is sorted now (by the last algo called)
        label_kth_value.config(text=f"kth value={kth_value}")

        # use the GraphViz module to show print the bargraph
        bar = viz.BarGraph()
        bar.data = graph_data # our Dict of aglo-name/execution-time pairs
        bar.x_label= "Algorithms Tested"
        bar.y_label = "Execution Time (ms)"
        bar.title = "Algorithm Exection Time Comparison"
        bar.show_graph()

#empty lists
generated_list = [] # holds or randomly generatee int list

#create tkinter window
root = Tk() #has to be first in a Tkinter file
root.title("Algo Analyzer")
root.minsize(1700, 1000)

# configuring the grid
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)


background_image = ImageTk.PhotoImage(Image.open("bg.jpeg"))
background_label = ttk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

root.configure(bg='#2E2E2E')
# Create a style for the input label
style = ttk.Style()
style.configure("InputLabel.TLabel", font=("Roboto", 14, "bold"))

customtkinter.CTkLabel(root, text="Algorithms Efficiency Analyzer",font=("Roboto", 34, "bold"), fg_color="transparent", width=60, height=10, text_color='white').grid(column=0, row=1, columnspan=3)
#customtkinter.CTkLabel(root, text="", fg_color="transparent", height=20).grid(column=0, row=2)


### ROW 0 ###
#create/place the "Generate" button and set the command to our click handler
button_generate = customtkinter.CTkButton(root, text="Generate List", width=40, height=60, font=("Roboto", 20, "bold"), command=click_generate,
                         fg_color="transparent", hover_color="grey") # assign click_gerate as the click handler
button_generate.grid(row=3,column=0, columnspan=3, pady=(10, 10))  
#create/place the abel to the left of the generate label (which displays the generated list)
label_unsorted = customtkinter.CTkLabel(root,text="Unsorted List:", text_color='white', width=20, font=("Roboto", 20, "bold"), anchor="w", fg_color="transparent")
label_unsorted.grid(row=4,column=0, columnspan=3, pady=(50, 10))
#create/place the label to show the generated list
label_generated_list = Label(root, width=80, height=5, anchor="w", background='#cfb095', font=("Roboto", 20, "bold")) 
label_generated_list.grid(row=5,column=0, padx=10, pady=10,  columnspan=3)
#create/place label to show generated "k"
label_kth = Label(root,width = 10, height=3, anchor="w", font=("Roboto", 15, "bold"))
label_kth.grid(row=6,column=0, columnspan=3, pady=(10, 10))

### ROW 1 ###
#create/place the generate button and set the command to our click handler
button_graph = customtkinter.CTkButton(root, text="Graph and Sort", width=40, height=60, font=("Roboto", 20, "bold"), command=click_graph, 
                                       fg_color="transparent", hover_color="grey") # assign click_graph as the click handler
button_graph.grid(row=7,column=0, columnspan=3, pady=(10, 10))
#create/place the  label to the left of the "sorted_list" label (which displays the list after sorting)
label_sorted = customtkinter.CTkLabel(root,text="Sorted List:", text_color='white', width=20, font=("Roboto", 20, "bold"), anchor="w", fg_color="transparent")
label_sorted.grid(row=8,column=0, columnspan=3,  pady=(50, 10))
#create/place the Label to display the list after sorting
label_sorted_list= Label(root,text="", width=80, height=5, anchor="w", border='1', background='#cfb095', font=("Roboto", 20, "bold"))
label_sorted_list.grid(row=9,column=0,padx=10,pady=10, columnspan=3)
#create/place label to show generated "k"th value
label_kth_value = Label(root,width = 10, height=3, anchor="w",  font=("Roboto", 15, "bold"))
label_kth_value.grid(row=10,column=0, columnspan=3, pady=(10, 50))


def main():
    """ MAIN function just calls the tkinter mainloop"""
    root.mainloop() #create a main loop - this loop is constantly checking mouse position, clicks etc

if __name__ == "__main__":
    main()
