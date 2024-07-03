import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from PIL import Image, ImageTk


def translate_text():
    # Retrieve the text from the input entry widget
    text_to_translate = input_textbox.get("1.0", "end-1c")

    # Determine source and target languages from dropdown menus
    source_lang = source_lang_var.get()
    target_lang = target_lang_var.get()

    # Translate the text using Google Translate API
    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text

    # Update the output textbox widget with the translated text
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", translated_text)

def exchange_languages():
    # Swap the values of source_lang_var and target_lang_var
    source_lang, target_lang = source_lang_var.get(), target_lang_var.get()
    source_lang_var.set(target_lang)
    target_lang_var.set(source_lang)


# Create the main application window
root = tk.Tk()
root.title("Language Translator")
root.configure(bg='gray')

container = ttk.Frame(root, padding=(20, 10))
container.place(relx=0.5, rely=0.5, anchor="center")

# Create source language dropdown menu
source_lang_label = tk.Label(root, text="Source Language:")
source_lang_label.grid(row=0, column=0)

source_lang_var = tk.StringVar()
source_lang_dropdown = ttk.Combobox(root, textvariable=source_lang_var,
                                    values=["auto", "afrikaans", "albanian", "amharic", "arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian",
                                            "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English",
                                            "Esperanto", "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian Creole",
                                            "Hausa", "Hawaiian", "Hebrew",  "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian",  "Irish", "Italian",
                                            "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean","Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian",
                                            "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian",
                                            "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho",
                                             "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish",  "Sundanese", "Swahili","Swedish", "Tajik", "Tamil",
                                            "Tatar","Telugu", "Thai","Turkish", "Turkmen", "Ukrainian","Urdu", "Uyghur","Uzbek" "Vietnamese", "Welsh", "Xhosa",
                                            "Yiddish", "Yoruba","Zulu"])  # You can add more languages as needed
source_lang_dropdown.grid(row=0, column=1)
source_lang_dropdown.current(0)  # Set default value to 'auto'

# Create target language dropdown menu
target_lang_label = tk.Label(root, text="Target Language:")
target_lang_label.grid(row=0, column=4)

target_lang_var = tk.StringVar()
target_lang_dropdown = ttk.Combobox(root, textvariable=target_lang_var,
                                    values=["auto", "afrikaans", "albanian", "amharic", "arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian",
                                            "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English",
                                            "Esperanto", "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian Creole",
                                            "Hausa", "Hawaiian", "Hebrew",  "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian",  "Irish", "Italian",
                                            "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean","Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian",
                                            "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian",
                                            "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho",
                                             "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish",  "Sundanese", "Swahili","Swedish", "Tajik", "Tamil",
                                            "Tatar","Telugu", "Thai","Turkish", "Turkmen", "Ukrainian","Urdu", "Uyghur","Uzbek" "Vietnamese", "Welsh", "Xhosa",
                                            "Yiddish", "Yoruba","Zulu"])  # You can add more languages as needed
target_lang_dropdown.grid(row=0, column=5)
target_lang_dropdown.current(0)  # Set default value to 'en'

# Create input textbox
input_label = tk.Label(root, text="Enter text to translate:")
input_label.grid(row=17, column=0, columnspan=2)

input_textbox = tk.Text(root, height=5, width=40)
input_textbox.grid(row=17, column=0, columnspan=2, padx=10, pady=10)

# Create output textbox to display translated text
#output_label = tk.Label(root, text="Translated text:")
#output_label.grid(row=17, column=2, columnspan=2)

output_textbox = tk.Text(root, height=5, width=40)
output_textbox.grid(row=17, column=4, columnspan=2, padx=10, pady=10)



# Create translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=19, column=2, columnspan=2, pady=10)

#exchange_img = tk.PhotoImage(file="arrow-goes-left-right-outline-icon.png")
exchange_img = Image.open("arrow-goes-left-right-outline-icon.png")
exchange_img = exchange_img.resize((40, 40))
exchange_img = ImageTk.PhotoImage(exchange_img)

#exchange_button = tk.Button(root, text="Exchange Languages", command=exchange_languages, bg="lightgreen")
#exchange_button.grid(row=18, column=2, columnspan=2, pady=10)

exchange_button = tk.Button(root, image=exchange_img, command=exchange_languages, bg="lightgray", bd=0)
exchange_button.grid(row=17, column=2, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
