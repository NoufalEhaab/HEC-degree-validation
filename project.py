import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import time  


import pandas as pd

def validate(transcript_path):
    file = pd.read_csv(transcript_path)
    
    file1 = file.drop('rmk',axis = 1)
    file2 = pd.read_csv('cscore.csv')
    common_column = 'courseName'
    cscore = pd.merge(file1, file2, on=common_column, how='left')
    cscore = cscore.dropna()
    cscore = cscore.sort_values('points', ascending=False).drop_duplicates(subset='courseName')


    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('csgeneral.csv')
    common_column = 'courseName'
    csgeneral = pd.merge(file1, file2, on=common_column, how='left')
    csgeneral = csgeneral.dropna()

    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('csgeneralelective.csv')
    common_column = 'courseName'
    csgeneralelective = pd.merge(file1, file2, on=common_column, how='left')
    csgeneralelective=csgeneralelective.dropna()

    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('csmaths.csv')
    common_column = 'courseName'
    csmaths = pd.merge(file1, file2, on=common_column, how='left')
    csmaths = csmaths.dropna()

    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('cscompulsory.csv')
    common_column = 'courseName'
    cscompulsory = pd.merge(file1, file2, on=common_column, how='left')
    cscompulsory = cscompulsory.dropna()
    # cscompulsory = cscompulsory.sort_values('points', ascending=False).drop_duplicates(subset='courseName')


    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('cssupporting.csv')
    common_column = 'courseName'
    cssupporting = pd.merge(file1, file2, on=common_column, how='left')
    cssupporting = cssupporting.dropna()

    file1 = file
    file1 = file1.drop('rmk',axis = 1)
    file2 = pd.read_csv('cselective.csv')
    common_column = 'courseName'
    cselective = pd.merge(file1, file2, on=common_column, how='left')
    cselective = cselective.dropna()

    total_general_education = (is_pass(csgeneral)-19)
    total_university_electives = (is_pass(csgeneralelective)-12)
    total_math_science_foundation = (is_pass(csmaths)-12)
    total_computing_core = (is_pass(cscore)-39)
    total_domain_cs_core = (is_pass(cscompulsory)-24)
    total_domain_cs_electives = (is_pass(cselective)-15)
    total_domain_cs_supporting = (is_pass(cssupporting)-9)

    print(total_general_education)
    print(total_university_electives)
    print(total_math_science_foundation)
    print(total_computing_core)
    print(total_domain_cs_core)
    print(total_domain_cs_electives)
    print(total_domain_cs_supporting)
    result_text = result(total_general_education, total_university_electives, total_math_science_foundation,
                         total_computing_core, total_domain_cs_core, total_domain_cs_electives, total_domain_cs_supporting)

    update_result_dialog(result_text)
 
   
    

def update_result_dialog(validation_text):
    global result_dialog  
    result_dialog = tk.Toplevel(root)
    result_dialog.title("Validation Result")

    # Label to display validation result
    result_label = ttk.Label(result_dialog, text=validation_text, style='TLabel')
    result_label.pack(padx=20, pady=10)

    ok_button = ttk.Button(result_dialog, text="OK", command=result_dialog.destroy)
    ok_button.pack(pady=5)

    details_button = ttk.Button(result_dialog, text="Details", command=lambda: show_validation_details(validation_result))
    details_button.pack(pady=5)

def show_validation_details(validation_text):
    details_window = tk.Toplevel(root)
    details_window.title("Validation Details")

    validation_result_text = "\n".join(validation_text)

    validation_details_label = ttk.Label(details_window, text=validation_result_text, style='TLabel')
    validation_details_label.pack(padx=20, pady=10)

    ok_button = ttk.Button(details_window, text="OK", command=details_window.destroy)
    ok_button.pack(pady=5)
validation_result = []

def result(total_general_education, total_university_electives, total_math_science_foundation,
           total_computing_core, total_domain_cs_core, total_domain_cs_electives, total_domain_cs_supporting):
    
    

    if total_general_education < 0:
        validation_result.append("You need to take more courses in General Education.")

    if total_university_electives < 0:
        validation_result.append("You need to take more University Elective courses.")

    if total_math_science_foundation < 0:
        validation_result.append("You need to take more courses in Math and Science Foundation.")

    if total_computing_core < 0:
        validation_result.append("You need to take more courses in Computing Core.")

    if total_domain_cs_core < 0:
        validation_result.append("You need to take more courses in Domain Computer Science Core.")

    if total_domain_cs_electives < 0:
        validation_result.append("You need to take more courses in Computer Science Electives.")

    if total_domain_cs_supporting < 0:
        validation_result.append("You need to take more courses in Computer Science Supporting.")

    if total_general_education > 0:
        validation_result.append("You have taken extra courses in General Education.")

    # if total_university_electives > 0:
    #     validation_result.append("You have taken extra University Elective courses.")

    # if total_math_science_foundation > 0:
    #     validation_result.append("You have taken extra courses in Math and Science Foundation.")

    # if total_computing_core > 0:
    #     validation_result.append("You have taken extra courses in Computing Core.")

    # if total_domain_cs_core > 0:
    #     validation_result.append("You have taken extra courses in Computer Science Core.")

    # if total_domain_cs_electives > 0:
    #     validation_result.append("You have taken extra courses in Computer Science Electives.")

    # if total_domain_cs_supporting > 0:
    #     validation_result.append("You have taken extra courses in Computer Science Supporting.")

    if (total_general_education >= 0 and total_university_electives >= 0
            and total_math_science_foundation >= 0 and total_computing_core >= 0
            and total_domain_cs_core >= 0 and total_domain_cs_electives >= 0
            and total_domain_cs_supporting >= 0):
        validation_result.append("--------------Degree Validated Successfully---------------")
        return "Degree Validated Successfully"
    else:
        validation_result.append("--------------Degree Validation Failed---------------")
        return "Degree Validation Failed"
 


def is_pass(data):
    credit_hour_gained = 0
    for index, row in data.iterrows():
        if row['points'] > 0.0:
            credit_hour_gained += row['creditHour']
    
    return credit_hour_gained

root = None
selected_path_label = None
progress_bar = None
validation_label = None

def select_transcript():
    transcript_path = filedialog.askopenfilename(initialdir="/", title="Select Transcript CSV File",
                                                 filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if transcript_path:
        print("Transcript Path:", transcript_path)
        display_selected_path(transcript_path)
        read_file_stage()
        root.after(200, lambda: read_file_completed(transcript_path))
    return transcript_path

def display_selected_path(path):
    selected_path_label.config(text="Selected Transcript: " + path)

def read_file_stage():
    selected_path_label.config(text="Reading File...")
    progress_bar['value'] = 20

def read_file_completed(transcript_path):
    progress_bar['value'] = 100
    constraints_stage(transcript_path)

def constraints_stage(transcript_path):
    selected_path_label.config(text="Checking Constraints...")
    progress_bar['value'] = 40
    root.after(400, lambda: constraints_completed(transcript_path))

def constraints_completed(transcript_path):
    progress_bar['value'] = 80
    validation_stage(transcript_path)

def validation_stage(transcript_path):
    selected_path_label.config(text="Validated!")
    progress_bar['value'] = 100
    

def display_image():
    global root
    root = tk.Tk()
    root.title("HEC Degree Validation")

    style = ttk.Style()
    style.configure('TFrame', background='white')
    style.configure('TLabel', font=('Courier', 12), background='white')
    style.configure('TButton', font=('Courier', 12), background='white')

    frame = ttk.Frame(root, style='TFrame')
    frame.pack(fill=tk.BOTH, expand=True)

    image_path = "C:/Users/ehaab/OneDrive/Desktop/Semester5/KRR/KRR project/P1 - HEC Degree Requiremnts/Logo.png"
    img = Image.open(image_path)
    img = img.resize((100, 100))  

    # Convert the image for Tkinter
    img_tk = ImageTk.PhotoImage(img)

    label_image = ttk.Label(frame, image=img_tk, style='TLabel')
    label_image.grid(row=0, column=0, columnspan=2, pady=10) 
    label_text = ttk.Label(frame, text="Degree Validation", style='TLabel')
    label_text.grid(row=1, column=0, columnspan=2)  
    global selected_path_label
    selected_path_label = ttk.Label(frame, text="", style='TLabel')
    selected_path_label.grid(row=2, column=0, columnspan=2, pady=5)  

    global progress_bar
    progress_bar = ttk.Progressbar(frame, orient='horizontal', length=200, mode='determinate')
    progress_bar.grid(row=3, column=0, columnspan=2, pady=5)  
    validate_button = ttk.Button(frame, text="Validate", command=lambda: validate(select_transcript()), style='TButton')
    validate_button.grid(row=5, column=0, columnspan=2, pady=5)  

    global validation_label
    validation_label = ttk.Label(frame, text="", style='TLabel')
    validation_label.grid(row=6, column=0, columnspan=2, pady=5)  
   
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_rowconfigure(5, weight=1)
    frame.grid_rowconfigure(6, weight=1)

    window_width = 320  
    window_height = 500  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
   

    root.mainloop()


display_image()



    


