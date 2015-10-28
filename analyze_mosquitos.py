
import pandas as pd
import matplotlib.pyplot as plt
 
def fahr_to_celcius(temp_fahr):
    """convert fahr to celsius
    
    return celsius conversion of input"""
    temp_celcius = (temp_fahr - 32) * 5/9
    return temp_celcius

def create_mosquitos_vs_tempC_plot(filename):
    #write processing here
    #load data
    mosquito_data = pd.read_csv(filename)
    #convert to celsius
    mosquito_data['temperature_C'] = fahr_to_celcius(mosquito_data['temperature'])
    #create the plot
    plt.plot(mosquito_data['temperature_C'], mosquito_data['mosquitos'],'.')
    #save the plot
    filename_png = filename[0:-4] + 'mosquito_vs_tempC.png'
    plt.savefig(filename_png)
    return mosquito_data
