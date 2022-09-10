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
    
            # Open the file
            #file = open(self.name, 'r')

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

            j = 0

            # Try to convert data 
            for i in range(len(data_temp)):
                try:
                    #print("*****")
                    # Inserisco float e poi int in quanto se converto direttamente a intero i time_app vengono ignorati
                    time_app = int(float(data_temp[i][0]))
                    #print("Tipo:",type(data_temp[i][0]))
                    #print("***", time_app)
                    temp_app = float(data_temp[i][1])
                    #print("Time:", time_app, "Temp:", temp_app)
                    lista_temp = [time_app, temp_app]
                    #print("Tipo:", type(lista_temp))

                    # Modifica 1
                    if time_app >= 0:
                        data.append(lista_temp)

                except:
                    pass
                    #raise ExamException("Errore nella conversione dei dati")

            # Check if epoch are sorted correctly
            for i in range(len(data)-1):
                j = i+1    
                while j != len(data):
                    
                    if data[i][0] >= data[j][0]:
                        raise ExamException('Epoch non ordinati correttamente')
                        #None

                    j += 1
                    
            # If all check are ok, return data
            return(data)