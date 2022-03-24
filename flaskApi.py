from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        'name': 'This is Python ',
        'id' :  '0',
        'desc' : "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects."
    },
    {
        'name': 'Java',
        'id' :  '1',
        'desc' : "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible."
    },
    {
        'name': 'Typescript',
        'id' :  '2',
        'desc' : "TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale"
    }
]

@app.route('/')
def index():
    return "Welcome Home"

@app.route('/courses', methods=['GET'])
def crs():
    return jsonify({'Course' : courses})

@app.route('/courses/<int:course_id>', methods = ['GET'])
def getcrs(course_id):
    return jsonify({'Courses': courses[course_id]})

@app.route('/courses', methods = ['POST'])
def createcrs():
    course =    {
        'name': 'Solidity',
        'id' :  '3',
        'desc' : "Solidity is a programming language, with which we can write smart contracts and deploy it into blockchain. All web 3.0 apps/dapps use smart contracts extensively. Solidity looks similar to javascript and python. But with blockchain native features built in."
    }
    courses.append(course)
    return jsonify({'Created': course})

@app.route('/courses/<int:course_id>', methods = ['PUT'])
def updatecrs(course_id):
    courses[course_id]['desc'] = "Changed Description"
    return jsonify({'course': courses[course_id]})

@app.route('/courses/<int:course_id>', methods = ['DELETE'])
def deletecrs(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})

#  curl command
# curl -i -H "Content-Type: Aplication/json" -X POST http://127.0.0.1:5000/courses


if __name__ == '__main__':
    app.run(debug=True)
