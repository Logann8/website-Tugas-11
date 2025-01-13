from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fungsi untuk menghitung distribusi Poisson
def poisson_distribution(mean, x):
    if mean <= 0 or x < 0:
        return None
    e = math.exp(-mean)
    return (mean**x * e) / math.factorial(x)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    mean = None
    x_value = None
    distribution_table = []

    if request.method == "POST":
        mean = float(request.form.get("mean"))
        x_value = int(request.form.get("xValue"))

        # Hitung probabilitas untuk input pengguna
        result = poisson_distribution(mean, x_value)

        # Buat tabel distribusi Poisson untuk beberapa nilai X
        for x in range(0, 11):  # X dari 0 hingga 10
            probability = poisson_distribution(mean, x)
            distribution_table.append({"x": x, "probability": round(probability, 6)})

    return render_template("index.html", result=result, mean=mean, x_value=x_value, distribution_table=distribution_table)

if __name__ == "__main__":
    app.run(debug=True)
