
# Create the class ExamExeption
class ExamException(Exception):
    pass

# Create Class CSVTimeSeriesFile
class CSVTimeSeriesFile:

    # Use magic method __ini__ to initialize the attribute of class
    def __init__(self, name):
        self.name = name

    
    # Create a function get_data
    def get_data(self):  

            # Try to open the file
            try:
                file = open(self.name, 'r')
                file.readline()
                file.seek(0, 0)
        
            # If i can't open the file, I raise an exception 
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
                
                #If the element in first position is different by epoch i will add at the list
                if elements[0] != 'epoch':
                    
                    data_temp.append(elements)
            
            # Close the file
            file.close()

            # Raise an exception if the file is empty
            if len(data_temp) == 0:
                raise ExamException('Il file non ha valori al suo interno')

            # Try to convert data 
            for i in range(len(data_temp)):
                try:

                    time_app = int(float(data_temp[i][0]))
                    temp_app = float(data_temp[i][1])

                    list_temp = [time_app, temp_app]

                    # Check if Value of Epoch are greater than 0
                    if time_app >= 0:
                        data.append(list_temp)

                except:
                    pass
            
            # Check if epoch are sorted correctly
            for i in range(len(data)-1):
                if data[i][0] >= data[i+1][0]:
                    raise ExamException('Epoch non ordinati correttamente o duplicati')

            # If all check are ok, return data
            return(data)