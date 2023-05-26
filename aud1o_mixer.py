import os
from pydub import AudioSegment
from tkinter import *
from tkinter import colorchooser


def change_audio_speed(filename, factor):
    audio = AudioSegment.from_file(filename)

    changed_speed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * factor)})
    return changed_speed_audio


def get_audio_filename():
    filename = entry.get()
    if os.path.isfile(filename):
        return filename
    else:
        label.config(text="Файл не найден. Попробуйте еще раз.", fg="red")


def change_speed():
    filename = get_audio_filename()
    speed_factor = float(entry_speed.get())
    changed_speed_audio = change_audio_speed(filename, speed_factor)
    output_filename = f"changed_speed_{filename}"
    changed_speed_audio.export(output_filename, format="wav")
    message = f"Измененный аудиофайл сохранен как {output_filename}"
    Label(window, text=message, fg="green", font=("Arial Bold", 12)).pack()
    # определение размеров окна и местоположения
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('+{}+{}'.format(x, y))


def choose_color():
    global font_color
    color = colorchooser.askcolor(title="Выберите цвет")
    font_color = color[1]


window = Tk()
window.title("Аудиомиксер 999999 бара бара бара бере бере бере")

# изменяем размер окна
window.geometry("600x200")
window.resizable(width=True, height=False)
# добавляем возможность изменения цвета фона и размера окна
window.configure(bg="#258a83")

label = Label(window, text="Введите имя аудиофайла с расширением:", font=("Arial Bold", 12), pady=10, bg="black",
              fg="white")
label.pack()

entry = Entry(window)
entry.pack()

label_speed = Label(window, text="Введите коэффициент изменения скорости:", bg="black", fg="white")
label_speed.pack()

entry_speed = Entry(window)
entry_speed.pack()

font_color = "#12968e"
button = Button(window, text="Изменить", command=change_speed)
button.pack()

window.mainloop()