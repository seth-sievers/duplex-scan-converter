import PyPDF2

def main():
        #read in the file names 
        file_path = input('Please Enter the path to the file you wish to convert: ')
        if ((file_path[0] == '"') or (file_path[0] == "'")):
                file_path = file_path[1::]
        if ((file_path[-1] == '"') or (file_path[-1] == "'")):
                file_path = file_path[0:-1:]

        converted_name = input('Please Enter the name for the converted file: ')
        if ((converted_name[0] == '"') or (converted_name[0] == "'")):
                converted_name = converted_name[1::]
        if ((converted_name[-1] == '"') or (converted_name[-1] == "'")):
                converted_name = converted_name[0:-1:]

        # open the pdf file for reading and verify correct page count
        reader = PyPDF2.PdfReader(file_path)
        if ((len(reader.pages) % 2)):
                print('ERROR: There should be an even number of pages!')
                raise ValueError

        num_individual_pages = len(reader.pages)//2

        # create a pdf writer object and add the pages to it in the proper order
        converted_pdf = PyPDF2.PdfWriter()
        for i in range (0, num_individual_pages):
                #add the ith page from the front and then the ith page from the back
                converted_pdf.add_page(reader.pages[i])
                converted_pdf.add_page(reader.pages[(len(reader.pages)-1)-i])
        
        # write to the output file
        with open(converted_name, "wb") as output_file:
                converted_pdf.write(output_file)
        
        print('\nDone!')

##########################
if __name__ == '__main__':
        main()
##########################