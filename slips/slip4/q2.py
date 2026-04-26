from flask import Flask

app = Flask(__name__)

@app.route('/')
def library():
    return '''
    <html>
    <body>
    <h1>City Public Library</h1>
    <table border="1">
        <tr><th>Title</th><th>Author</th></tr>
        <tr><td>The Alchemist</td><td>Paulo Coelho</td></tr>
        <tr><td>Wings of Fire</td><td>APJ Abdul Kalam</td></tr>
        <tr><td>Harry Potter</td><td>J.K. Rowling</td></tr>
        <tr><td>Rich Dad Poor Dad</td><td>Robert Kiyosaki</td></tr>
    </table>
    <p><b><font color="blue">"A reader lives a thousand lives before he dies."</font></b></p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
