from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    health = ['___', '__']
    if request.method == 'POST':
        h = int(request.form['height'])
        w = int(request.form['weight'])
        bmi = w / ((h / 100) ** 2)
        health.insert(0, round(bmi, 2))
        print(health[::])
        print(round(bmi, 2))
        if len(health) > 0:

            ub = health[0]  # Conditions to find out BMI category
            if (ub < 18.5):
                health.insert(1, "underweight")

            elif (ub >= 18.5 and ub < 24.9):
                health.insert(1, "Healthy")

            elif (ub >= 24.9 and ub < 30):
                health.insert(1, "overweight")

            elif (ub >= 30):
                health.insert(1, "Suffering from Obesity")
    return render_template('index.html', health=" your BMI is {} and You are {}".format(health[0], health[1]))


@app.route("/about")
def page2():
    return render_template('about.html')


@app.route("/tempc", methods=['GET', 'POST'])
def celcius():
    list = ["__", "__"]
    if request.method == 'POST':
        c = int(request.form['c'])
        f = (c * (9/5)) + 32
        list.insert(0,c)
        list.insert(1,f)

    return render_template("celcius.html",fahrenheit="{} degree Celsius is equal to {} degree Fahrenheit".format(list[0], list[1]))

@app.route("/tempf", methods=['GET', 'POST'])
def faren():
    list_f= ["__", "__"]
    if request.method == 'POST':
        c = int(request.form['f'])
        f = (c- 32) / (9/5)
        list_f.insert(0,c)
        list_f.insert(1,round(f,2))

    return render_template("faren.html",celcius="{} degree farenheit is equal to {} degree Celcius".format(list_f[0], list_f[1]))

if __name__ == "__main__" :
    app.run(debug=True, port=8000)