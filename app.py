from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='Antoni')

# Strona logowania
@app.route('/')
def login():
    return render_template('forum.html')

# Obsługa formularza logowania
@app.route('/sprawdz_haslo', methods=['POST'])
def sprawdz_haslo():
    password = request.form['password']
    # W rzeczywistości to sprawdzanie hasła powinno być bardziej zaawansowane
    if password == 'Hasło':  # Zmienić na prawdziwe hasło
        return redirect(url_for('forum_bierzmowanie'))
    else:
        return 'Nieprawidłowe hasło. Spróbuj ponownie.'

# Strona prawidłowa
@app.route('/forum_bierzmowanie')
def forum_bierzmowanie():
    return render_template('Forum_bierzmowanie.html')

if __name__ == '__main__':
    app.run(debug=True)
