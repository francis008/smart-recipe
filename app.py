from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():

    ingredients_input = None

    if request.method == "POST":
        ingredients_input = request.form.get('ingredients')
        print(f"Received ingredients {ingredients_input}")
        
    return render_template('index.html', ingredients_received=ingredients_input) 
    
    

if __name__ == '__main__':
    app.run(debug=True)