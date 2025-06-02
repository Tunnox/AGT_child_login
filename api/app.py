from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'Chuk_secret_key'  # Replace with your secret key

# Configure your PostgreSQL database connection here
connection = psycopg2.connect(dbname='AGT', user='postgres', password='pgsqtk116chuk95', host='chukspace.ctiuisa62ks5.eu-north-1.rds.amazonaws.com', port='5432')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login_username = data['loginUsername']
    login_password = data['loginPassword']

    cur = connection.cursor()
    try:
        cur.execute(
            'SELECT * FROM "public"."AGT_USER_LOGIN" WHERE ("USERNAME" = %s OR "EMAIL" = %s) AND "PASSWORD" = %s;', 
            (login_username, login_username, login_password)
        )
        user = cur.fetchone()
        
        if user:
            return jsonify({"message": "Login successful!", "success": True}), 200
        else:
            return jsonify({"message": "Invalid credentials, please create an account."}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    finally:
        cur.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)
