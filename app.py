from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    files = request.form.getlist('files')
    dest_drive = request.form['dest_drive']
    
    # Construir comando rclone
    for file in files:
        command = f"rclone copy {file} {dest_drive}"
        subprocess.run(command, shell=True)
    
    return redirect(url_for('home'))

@app.route('/history')
def history():
    # Implementar lógica para visualizar histórico de transferências
    return "Histórico de Transferências"

if __name__ == '__main__':
    app.run(debug=True)

