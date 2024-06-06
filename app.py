from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'parrot': {
        'name': 'Parrot',
        'age': 5,
        'workplace': 'Tropical Forest',
        'favorite_food': 'Sunflower seeds',
        'favorite_place': 'Jungle canopy',
        'latest_post': 'Squawk!',
        'friends': ['dog', 'cat']
    },
    'dog': {
        'name': 'Dog',
        'age': 3,
        'workplace': 'Backyard',
        'favorite_food': 'Bones',
        'favorite_place': 'Dog park',
        'latest_post': 'Woof!',
        'friends': ['cat']
    },
    'cat': {
        'name': 'Cat',
        'age': 2,
        'workplace': 'Living room',
        'favorite_food': 'Fish',
        'favorite_place': 'Sunny spot',
        'latest_post': 'Meow!',
        'friends': ['dog', 'parrot']
    },
    'rooster': {
        'name': 'Rooster',
        'age': 1,
        'workplace': 'Farmyard',
        'favorite_food': 'Grains',
        'favorite_place': 'Chicken coop',
        'latest_post': 'Cock-a-doodle-doo!',
        'friends': []
    }
}

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/<username>')
def show_profile(username):
    if username in users:
        user = users[username]
        return render_template('profile.html', user=user)
    else:
        return "User not found", 404

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        username = request.form['username']
        if username not in users:
            users[username] = {
                'name': request.form['name'],
                'age': int(request.form['age']),
                'workplace': request.form['workplace'],
                'favorite_food': request.form['favorite_food'],
                'favorite_place': request.form['favorite_place'],
                'latest_post': '',
                'friends': []
            }
            return redirect(url_for('show_profile', username=username))
        else:
            return "Username already exists. Please choose another one."
    return render_template('create_profile.html')

if __name__ == '__main__':
    app.run(debug=True)
