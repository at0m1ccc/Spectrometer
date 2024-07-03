import os
import sys
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Clear space (in Python, we just reset some variables)
# def clear_space():
#     global ModelSettings
#     ModelSettings = DefaultModelSettings.copy()


# clear_space()

print("\n\nStarting...\n*************\n")


# Define global constants and default model settings
class GlobalConstants:
    WizPrompts = "WizPrompts/wp_%s.bre"
    GNUPLOT = "gnuplot/bin/wgnuplot.exe"
    WizScreen = "WizScreen.bre"
    Customers = {
        "oxmk": "Общество с ограниченной ответственностью (г. Оксфор)",
        "ofme": "ООО ФМЭ (г. Омск)",
        "nlmk": "НЛМК (г. Липецк)",
        "mmk": "ММК (г. Магнитогорск)",
        "bak": "БАК (г. Казань)",
        "vork": "Воркутинский завод (г. Воркута)",
        "ntmk": "НТМК (г. Нижний Тагил)",
        "ofan": "ОФАН (г. Орёл-Излучина)",
        "ref": "Реформатский завод (г. Ульяновск)",
        "gk": "ГК (г. Череповец)",
        "tpu": "Томский политехнический университет (г. Томск)",
        "core": "Королевский завод (г. Королев)"
    }
    Analysis = {
        "gost": "Государственный стандарт",
        "gk": "ГОСТ ГК",
        "elc": "Электрический стандарт",
        "coke": "Кокс стандарт"
    }
    FINAL_STEP_ID = "Final"
    MODEL_WNRANGE_MAX = 1000
    MODEL_WNRANGE_LIMITS = [649, 7501]
    MODEL_DEGREE_LAG = 3
    MODEL_DEGREE_LEN = 10


GC = GlobalConstants()
GC.MODEL_DEGREE_MAX = 1 + (GC.MODEL_DEGREE_LEN + 1) * GC.MODEL_DEGREE_LAG

DefaultModelSettings = {
    "wnrange": [650, 4450],
    "irfile": "Default.ir",
    "pdegree": [19, 12, 6, 1]
}

ModelSettings = DefaultModelSettings.copy()


def choose_files(default, caption, multi, filetypes):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=default, title=caption, filetypes=filetypes)
    return file_path


def read_ir(file_path):
    # Mock function to simulate reading an IR file
    return {
        "meta": {
            "time": "20230321-121314",
            "ftirKey0": "oxmk",
            "ftirModel": "Model123",
            "ftirTemperature": 25.0,
            "ftirHumidity": 50.0,
            "ftirGain": "Gain123",
            "ftirResolution": "Resolution123",
            "ftirPower2000": 2000.0,
            "ftirCells": "Cells123",
            "ftirNoofScans": 10,
            "ftirApodizationFunction": "ApodFunc123"
        }
    }


def main():
    global ModelSettings

    while True:
        user_input = input("Enter command (o/i/s/q): ").strip()
        if user_input == 'o':
            foo = choose_files(default=ModelSettings["irfile"], caption="SPECOM 2.3 - Выбор файла", multi=False,
                               filetypes=[("Spectrotest IR files", "*.ir")])
            if os.path.exists(foo):
                bar = read_ir(foo)
                if bar:  # Assuming that the read_ir function checks for file validity
                    ModelSettings["irfile"] = os.path.basename(foo)
                    ModelSettings["irobject"] = bar
                    print(f"Файл {ModelSettings['irfile']} успешно загружен.")
                else:
                    print("\nОшибка! Файл не соответствует ожидаемому формату.")
            else:
                print("\nОшибка! Файл не найден.")

        elif user_input == 'i':
            s = ModelSettings["irobject"]
            meta = s["meta"]
            dtti = meta.get("time", "NA")
            dtti = pd.to_datetime(dtti, format="%Y%m%d-%H%M%S").strftime("%d.%m.%Y %H:%M")
            geog = GC.Customers.get(meta.get("ftirKey0", ""), "NA")
            sern = meta.get("ftirModel", "NA")
            temp = round(meta.get("ftirTemperature", "NA"))
            humi = round(meta.get("ftirHumidity", "NA"))
            gain = meta.get("ftirGain", "NA")
            reso = meta.get("ftirResolution", "NA")
            p2wk = round(meta.get("ftirPower2000", "NA"), 2)
            cell = meta.get("ftirCells", "NA")
            scns = meta.get("ftirNoofScans", "NA")
            apod = meta.get("ftirApodizationFunction", "NA")

            print(f"\nДата и время: {dtti}")
            print(f"Географическое местоположение: {geog}")
            print(f"Модель: {sern}")
            print(f"Температура: {temp}")
            print(f"Влажность: {humi}")
            print(f"Gain: {gain}")
            print(f"Разрешение: {reso}")
            print(f"Power2000: {p2wk}")
            print(f"Cells: {cell}")
            print(f"Количество сканов: {scns}")
            print(f"Функция аподизации: {apod}")

        elif user_input == 's':
            # Here we should call gnuplot, but in Python, we will use matplotlib
            if "irobject" in ModelSettings:
                s = ModelSettings["irobject"]
                # Plotting a simple example
                x = np.linspace(650, 4450, 100)
                y = np.sin(x)  # Replace with actual data
                plt.plot(x, y)
                plt.title("Пример графика")
                plt.xlabel("Wave number")
                plt.ylabel("Intensity")
                plt.show()
            else:
                print("\nОшибка! Нет загруженного файла для построения графика.")

        elif user_input == 'q':
            print("\nПрограмма завершена.")
            break


if __name__ == "__main__":
    main()
