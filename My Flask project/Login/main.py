from flask import Flask, request, render_template

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def my_form():
    return render_template("register.html")

@app.route("/login")
def mylog():
    return render_template("index.html")

@app.route("/pro")
def pro():
    con = mysql.connect()
    cursor = con.cursor()
    local = "SELECT * FROM location"
    cursor.execute(local)
    locations = cursor.fetchall()
    return render_template("addpro.html", title='Location',locations=locations)

@app.route("/loc")
def loc():
    return render_template("addloc.html")

@app.route("/mov")
def mov():
    return render_template("movement.html")

@app.route("/back")
def back():
    return render_template("product.html")

@app.route("/",methods=['POST'])
def home():
    con=mysql.connect()
    cursor=con.cursor()
    username = request.form['uu']
    password = request.form['pp']
    values="INSERT INTO `login`(`user`, `pass`) VALUES('"+username+"','"+password+"')"
    print(values)
    cursor.execute(values)
    con.commit()
    con.close()
    return "<script>window.alert('Registration Successfully');window.location='/login';</script>"

@app.route("/log",methods=['GET','POST'])
def Authenticate():
    username = request.form['t1']
    password = request.form['t2']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM login WHERE user='"+username+"' and pass='"+password+"'")
    data=cursor.fetchone()
    if data is None:
        return "<script>window.alert('Invalid username and password');window.location='/';</script>"
    else:
        return "<script>window.alert('Login Successfully');window.location='/back';</script>"

@app.route("/promanage",methods=['GET','POST'])
def proadd():
    if request.form['v1'] == "Add product":
        con = mysql.connect()
        cursor = con.cursor()
        proid = request.form['proid']
        proname = request.form['proname']
        place=request.form['plc']
        qty=request.form['qty']
        if proid =="" or proname =="" or place =="" or qty =="":
            return "<script>window.alert('Check your fields');window.location='/pro';</script>"
        else:
            values = "INSERT INTO `product`(`product_id`, `product_name`,`place`,`qty`) VALUES('" + proid + "','" + proname + "','" +place+ "','" +qty+"')"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Product Added successfully');window.location='/pro';</script>"

    if request.form['v1'] == "Move product":
        con = mysql.connect()
        cursor = con.cursor()
        proid = request.form['proid']
        if proid == "":
            return "<script>window.alert('Check your fields');window.location='/pro';</script>"
        else:
            values="SELECT DISTINCT product_id,product_name from product Where product_id='"+proid+"'"
            cursor.execute(values)
            products = cursor.fetchall()
            local="SELECT * FROM location"
            cursor.execute(local)
            locations=cursor.fetchall()
            return render_template("movement.html", title='Product', products=products,locations=locations)

    if request.form['v1'] == "Update product":
        con = mysql.connect()
        cursor = con.cursor()
        proid = request.form['proid']
        proname = request.form['proname']
        place = request.form['plc']
        qty = request.form['qty']
        if proid == "":
            return "<script>window.alert('Check product_id');window.location='/pro';</script>"
        else:
            values = "UPDATE `product` SET `product_name`='"+proname+"',`place`='"+place+"',`qty`='"+qty+"' WHERE `product_id`='"+proid+"'"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Product Updated Successfully');window.location='/pro';</script>"

    if request.form['v1'] == "View product":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product")
        products=cursor.fetchall()
        return render_template("viewpro.html",title='Product',products=products)

    if request.form['v1'] == "Balance product":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product")
        pros=cursor.fetchall()
        return render_template("report.html",title='Pros',pros=pros)

@app.route("/locmanage",methods=['GET','POST'])
def locadd():
    if request.form['v1'] == "Add location":
        con = mysql.connect()
        cursor = con.cursor()
        locid = request.form['locid']
        locname = request.form['locname']
        if locid == "" or locname =="":
            return "<script>window.alert('Check your fields');window.location='/loc';</script>"
        else:
            values = "INSERT INTO `location`(`location_id`, `location_name`) VALUES('" + locid + "','" + locname + "')"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Location Added Successfully');window.location='/loc';</script>"

    if request.form['v1'] == "Delete location":
        con = mysql.connect()
        cursor = con.cursor()
        locid = request.form['locid']
        if locid == "":
            return "<script>window.alert('Check your fields');window.location='/loc';</script>"
        else:
            values = "DELETE FROM `location` WHERE location_id='"+locid+"'"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Location Deleted Successfully');window.location='/loc';</script>"


    if request.form['v1'] == "Update location":
        con = mysql.connect()
        cursor = con.cursor()
        locid = request.form['locid']
        locname = request.form['locname']
        if locid == "":
            return "<script>window.alert('Check your location_id');window.location='/loc';</script>"
        else:
            values = "UPDATE `location` SET `location_name`='"+locname+"' WHERE `location_id`='"+locid+"'"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Location Updated Successfully');window.location='/loc';</script>"

    if request.form['v1'] == "View location":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM location")
        locations=cursor.fetchall()
        return render_template("viewloc.html",title='Location',locations=locations)

@app.route("/moveproduct",methods=['GET','POST'])
def move():
    if request.form['v2'] == "Moved":
        con = mysql.connect()
        cursor = con.cursor()
        val="select * from product where product_id='"+request.form['pid']+"' and place='"+request.form['from']+"'"
        cursor.execute(val)
        new=cursor.fetchone()
        if new[3] == 0:
            return "<script>window.alert('No quantity available');window.location='/pro';</script>"
        else:
            diff=new[3]-int(request.form['qty'])
            if diff<0:
                return "<script>window.alert('No quantity available');window.location='/pro';</script>"
            else:
                val2 = "UPDATE `product` SET `qty`='" +str(diff)+ "' WHERE product_id='"+request.form['pid']+"' and place='"+request.form['from']+"'"
                cursor.execute(val2)
                query = "INSERT INTO `product_movement`(`movementid`, `timestamp`, `from_location`, `to_location`, `product_id`, `qty`) VALUES ('','" + request.form['date'] + "','" + request.form['from'] + "','" + request.form['to'] + "','"+request.form[
                    'pid'] + "','" + request.form['qty'] + "')"
                cursor.execute(query)

                val3 = "select * from product where product_id='" + request.form['pid'] + "' and place='" + request.form['to'] + "'"
                cursor.execute(val3)
                new2 = cursor.fetchone()
                add=new2[3]+int(request.form['qty'])
                val4 = "UPDATE `product` SET `qty`='" + str(add) + "' WHERE product_id='" + request.form['pid'] + "' and place='" + request.form['to'] + "'"
                cursor.execute(val4)
                con.commit()
                con.close()
                return "<script>window.alert('Product moved successfully');window.location='/pro';</script>"
    if request.form['v2'] == "View":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product_movement")
        movements = cursor.fetchall()
        return render_template("product_movement.html", title='Movement', movements=movements)
if __name__=="__main__":
    app.run()