from flask import Flask, render_template

app = Flask(__name__)

# Ana səhifə üçün route ('/')
@app.route('/')
def index():
    # templates qovluğundakı index.html faylını ekrana çıxarır
    return render_template('index.html')

if __name__ == '__main__':
    # Tətbiqi 5000-ci portda işə salırıq
    app.run(host='0.0.0.0', port=5000)