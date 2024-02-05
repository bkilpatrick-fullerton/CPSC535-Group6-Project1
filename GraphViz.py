
import matplotlib.pyplot as plt
import numpy as np

class BarGraph():
        def __init__(self):
                self.title = "Title"
                self.sub_title = ""
                self.data = {}
                self.x_label = "x_label"
                self.y_label = "y_label"

        def show_graph(self):
                x_vals = list(self.data.keys())
                y_vals = list(self.data.values())
                fig = plt.figure(figsize=(10,5))
                plt.bar(x_vals, y_vals, color ='maroon', width = 0.4)

                plt.xlabel(self.x_label)
                plt.ylabel(self.y_label)
                plt.title(self.title)
                plt.show()
                

def main():
        # creating the dataset
        data = {'C':20, 'C++':15, 'Java':30, 
                'Python':35}
        
        bar = BarGraph()
        bar.data = data
        
        bar.x_label= "Courses offered"
        bar.y_label = "No. of students enrolled"
        bar.title ="Students enrolled in different courses"
        bar.show_graph()

if __name__ == "__main__":
        main()