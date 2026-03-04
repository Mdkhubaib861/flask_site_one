from flask import Flask, render_template, request
import math

Myapp = Flask(__name__)

@Myapp.route('/')
def home():
    return render_template('home.html')

@Myapp.route('/about')
def about():
    return render_template('about.html')

@Myapp.route('/contact')
def contact():
    return render_template('contact.html')

# This route will open when the form is submitted
@Myapp.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    message = request.form['message']

    return f'''
            <h1>
            Username:{username}<br>
            Mobile:{mobile}<br>
            Email:{email}<br>
            Message:{message}
            </h1>
            '''

@Myapp.route('/services')
def services():
    return render_template('services.html')

@Myapp.route('/products')
def products():
    return render_template('products.html')

@Myapp.route('/arithmetic')
def arithmetics():
    return render_template('arithmetic.html')

@Myapp.route('/result', methods=['POST'])
def results():
    # return render_template('result.html')
    n1 = int(request.form.get('n1'))
    n2 = int(request.form.get('n2'))
    add = n1 + n2
    sub = n1 - n2
    mux = n1 * n2
    div = n1 / n2
    return f'''
    <h1> Results </h1>
    <h3> Addition : {add} </h3>
    <h3> Subtraction : {sub} </h3>
    <h3> Multiplication : {mux} </h3>
    <h3> Division : {div} </h3>

    '''

@Myapp.route('/shapes')
def shapes():
    return render_template('shapes.html')

@Myapp.route('/circle')
def circle():
    return '''
        <h1> Circle </h1>
        <div class="container">
            <form action="/answer" method="post">
                <input type="hidden" name="shape" value="circle">
                <input type="number" placeholder="Enter Radius of Circle" name="radius" style="padding:10px;">
                <button type="submit" style="padding:10px;">Calculate Area</button>
            </form>     
        </div>
        '''

@Myapp.route('/square')
def square():
    return '''
    <h1> Square </h1>
    <div class="container">
        <form action="/answer" method="post">
            <input type="hidden" name="shape" value="square">
            <input type="number" placeholder="Enter Side of Square" name="side" style="padding:10px;">
            <button type="submit" style="padding:10px;">Calculate Area</button>
        </form>
    </div>
    '''

@Myapp.route('/triangle')
def triangle():
    return '''
    <h1> Triangle </h1>
    <div class="container">
        <form action="/answer" method="post">
            <input type="hidden" name="shape" value="triangle">
            <input type="number" placeholder="Enter height" name="height" style="padding:10px;">
            <input type="number" placeholder="Enter base" name="base" style="padding:10px;">
            <button type="submit" style="padding:10px;">Calculate Area</button>
        </form>
    </div>
    '''

@Myapp.route('/rectangle')
def rectangle():
    return '''
    <h1> Rectangle </h1>
    <div class="container">
        <form action="/answer" method="post">
            <input type="hidden" name="shape" value="rectangle">
            <input type="number" placeholder="Enter base" name="base" style="padding:10px;">
            <input type="number" placeholder="Enter height" name="height" style="padding:10px;">
            <button type="submit" style="padding:10px;">Calculate Area</button>
        </form>
    </div>
    '''

@Myapp.route('/answer', methods=['POST'])
def answer():
    if request.form.get('radius'):
        radius=float(request.form.get('radius'))
        area=round(radius*radius*math.pi,2)
        return render_template('answer.html',answer1=area, shape="Circle")
    if request.form.get('side'):
        side=float(request.form.get('side'))
        area=side*side
        return render_template('answer.html',answer1=area,shape="Square")
    if request.form.get('length') and request.form.get('breadth'):
        length=float(request.form.get('length'))
        breadth=float(request.form.get('breadth'))
        area=length*breadth
        return render_template('answer.html',answer1=area,shape="Rectangle")
    if request.form.get('base') and request.form.get('height'):
        base=float(request.form.get('base'))
        height=float(request.form.get('height'))
        area=base*height*0.5
        return render_template('answer.html',answer1=area,shape="Triangle")
    if request.form.get("dist_value") and request.form.get('unit'):
        dist_value = float(request.form.get("dist_value"))
        if request.form.get("unit") == "mm":
            converted_val =round(float(dist_value) * 10,2)
            new_unit = "Millemters"
        elif request.form.get("unit") == "inch":
            converted_val = round(float(dist_value) / 2.54,2)
            new_unit = "Inches"
        elif request.form.get("unit") == "feet":
            converted_val =round((float(dist_value) / 2.54) / 12,2)
            new_unit = "Feet"
        elif request.form.get("unit") == "meter":
            converted_val =round(float(dist_value) / 100,2)
            new_unit = "Meters"
        elif request.form.get("unit") == "km":
            converted_val =round(float(dist_value) / 1000,2)
            new_unit = "Kilo Meter"
        elif request.form.get("unit") == "m":
            converted_val =round(float(dist_value) / 1000000,2)
            new_unit = "Miles"
        elif request.form.get("unit") == "yard":
            converted_val =round(float(dist_value) / 1000000000,2)
            new_unit = "Yards"
        else:
            converted_val = ""
            new_unit = ""
        return render_template('answer.html', answer1=converted_val, new_unit=new_unit)
    else:
        return render_template('answer.html',answer1="")

@Myapp.route('/distance')
def distance():
    return render_template('distance.html')

@Myapp.route('/students')
def students():
    return render_template('students.html')

@Myapp.route('/students_result', methods=['POST'])
def data():
    name=request.form.get('name')
    gender=request.form.get('gender')
    english=int(request.form.get('english'))
    maths =int (request.form.get('maths'))
    physics =int (request.form.get('physics'))
    chemistry = int(request.form.get('chemistry'))

    total = english + maths + physics + chemistry


    percentage = round((total / 400) * 100, 2)

    if english >= 35 and maths >= 35 and physics >= 35 and chemistry >= 35:
        result = "Pass"
    else:
        result = "Fail"

    return render_template('students_result.html', name=name, gender=gender, english=english, maths=maths,physics=physics,chemistry=chemistry,total=total,percentage=percentage,result=result)

Myapp.run(debug=True)