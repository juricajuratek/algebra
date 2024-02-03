import pandas as pd
import matplotlib.pyplot as plt

# citamo csv
red_vines_df = pd.read_csv("red_vines.csv", delimiter=";")
white_vines_df = pd.read_csv("white_vines.csv", delimiter=";")

# izracunavamo prosjek za oba vina
avg_red= red_vines_df["quality"].mean()
avg_white = white_vines_df["quality"].mean()

# kreiramo chart
wine_types = ["Red Wine", "White Wine"]
avg_quality = [avg_red, avg_white]

plt.bar(wine_types, avg_quality, color=["crveno", "bijelo"])
plt.xlabel("Vrsta vina")
plt.ylabel("Prosjecna kvaliteta")
plt.title("Usporedba crvenih i bijelih vina (prosjek kvalitete)")
plt.show()