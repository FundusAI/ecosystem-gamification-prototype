from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)

# Set company colors
primary_color = "#0447B8"
secondary_color = "#FF9839"

# Routes

# Helper function to generate random commit colors
def random_commit_color():
    colors = ['#3E753B', '#6CC644', '#BD2C00']  # bright green, dull green, red
    return colors[randint(0, len(colors) - 1)]

# Routes
@app.route('/')
def index():
    # return render_template("overview.html", active_page="overview", random_commit_color=random_commit_color)
    return redirect('challenge')


@app.route('/vouchers')
def vouchers():
    return render_template("vouchers.html", active_page="vouchers")

@app.route('/overview')
def overview():
    return render_template("overview.html", active_page="overview", random_commit_color=random_commit_color)


@app.route('/challenge', methods=['GET', 'POST'])
def challenge():
    if request.method == 'POST':
        # Process form data
        num_steps = request.form.get('num_steps', type=int)
        glucose_level = request.form.get('glucose_level', type=int)
        blood_pressure = request.form.get('blood_pressure')
        picture_of_feet = request.files.get('picture_of_feet')

        # Display the congratulatory message
        filled_fields = sum(field is not None for field in [num_steps, glucose_level])
        filled_fields += 1 if picture_of_feet else 0
        # filled_fields += 1 if len(blood_pressure) > 0 else 0

        return redirect('/overview')

    return render_template('challenge.html', primary_color=primary_color, secondary_color=secondary_color, active_page='challenge')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html", active_page='chat')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
