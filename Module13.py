import mysql.connector
import json
from flask import Flask, Response
#Exercise1
app= Flask(__name__)
@app.route('/prime/<int:num>')
def is_prime(num):
    try:
        prime= True
        if num<2:
            prime= False
        else:
            for i in range (2, num):
                if num%i==0:
                    prime= False
                    break
        result = {
            "Number": num,
            "IsPrime": prime
        }
        json_response = json.dumps(result)
        http_response = Response(response=json_response, status=200, mimetype="application/json")
        return http_response

    except ValueError:
        response = {
            "message": "Invalid input",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
#Exercise2
app = Flask(__name__)

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='time_travellers_quest',
    user='root',
    password='12345',
    autocommit=True,
    collation = 'utf8mb4_unicode_ci'
)

@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        sql = '''
            SELECT ident as 'icao', name, municipality 
            FROM airport 
            WHERE ident = %s
            '''
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (icao,))
        result = cursor.fetchone()
        if result:
            response = {
                'ICAO': result['icao'],
                'Name': result['name'],
                'Location': result['municipality']
            }
            json_response = json.dumps(result)
            http_response = Response(response=json_response, status=200, mimetype="application/json")
            return http_response
        else:
            raise ValueError('Airport not found')
    except ValueError:
        response = {
            "message": "Invalid input",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)