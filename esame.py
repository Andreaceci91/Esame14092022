# Andrea Ceci 
# MAT. SM3201219
# Laboratorio di Programmazione - Appello Esame 14/09/2022


# Create the class ExamExeption
class ExamException(Exception):
    pass

# Create Class CSVTimeSeriesFile
class CSVTimeSeriesFile:

    # Use magic method __init__ to initialize the attribute of class
    def __init__(self, name):
        self.name = name

    # Create function get_data
    def get_data(self):  

        # Try to open the file
        try:
            file = open(self.name, 'r')
            file.readline()
            file.seek(0, 0)
    
        # If i can't open the file, raise an exception 
        except:
            raise ExamException('Impossibile aprire il file')

                #Create a empty list
        data_temp = []
        data = []

        for line in file:               
            # Split the element on "," that separates the value
            elements = line.split(',')
                
            # Remove the newline character and black space
            elements[-1] = elements[-1].strip()
                
            #If the element in first position is different by epoch i will add it at the list
            if elements[0] != 'epoch':
                    
                data_temp.append(elements)
            
        # Close the file
        file.close()

        # Try to convert data 
        for i in range(len(data_temp)):
                
            try:
                time_app = int(float(data_temp[i][0]))
                temp_app = float(data_temp[i][1])

                lista_temp = [time_app, temp_app]

                # Check if Value of Epoch are greater than 0
                if time_app >= 0:
                    data.append(lista_temp)

            except:
                pass
            
        # Check if file has no value to process
        if len(data) == 0:
            raise ExamException('Il file non ha valori da processare al suo interno')            

        # Check if epoch are sorted correctly
        for i in range(len(data)-1):
            if data[i][0] >= data[i+1][0]:
                raise ExamException('Epoch non ordinati correttamente o duplicati')

        # If all check are ok, return data
        return(data)


# Create function to control the difference of temperature values
def compute_daily_max_difference(time_series):

    # Declare variables
    values = []
    length = len(time_series)

    # Check if legth of list have only 1 element
    if length == 1:
        values.append(None)

    else:    
        prev = 0
        after = 0
        
        i = 0
        #j = 0

        while i < length:

            # Use a variable to check if there are a single measure
            single = False
            
            temp = 0

            # Calculate the value before if the index is different by 0
            if i != 0:
                prev = (time_series[i-1][0] - (time_series[i-1][0] % 86400))

            # Calculate current value
            curr = (time_series[i][0] - (time_series[i][0] % 86400))
            
            # Calculate next value
            if i != length-1:
                after = (time_series[i+1][0] - (time_series[i+1][0] % 86400))
            
            # Check "Single" at the beginning of list
            if curr != after and i == 0:
                temp = None
                single = True

            if prev != curr and curr != after and i != 0:
                temp = None
                single = True
            
            # Check "Single" at the end of list
            if prev != curr and i == length-1:
                temp = None
                single = True

            # If i have not found "Single" element in list
            if single == False:
                j = i

                # Empty list I add Temp of same day
                list_calc = []

                while (j < length and ((time_series[j][0] - (time_series[j][0] % 86400)) == curr)):
                    
                    # Add at temporany list al values of the same day
                    list_calc.append(time_series[j][1])
                    j+=1
                
                # Calculate maximum daily excursion subtract at the "max value of temp" the "min value of temp"
                temp = max(list_calc) - min(list_calc)

                i = j-1
            
            i += 1

            # Attach temp at the list
            values.append(temp)

    # Return list of values
    return(values)

#==============================
#  Corpo del programma
#==============================

time_series_file = CSVTimeSeriesFile(name='/Users/andrea/Desktop/Esame14092022/data.csv')

# Use function Getdata and save value in Time_series
time_series = time_series_file.get_data()

# Invoce function below to calculate max daily excursion
results = compute_daily_max_difference(time_series)

print("\n***  Lista  ***")
for item in results:
    print(item)

print("Cambiamenti rievati:",len(results))