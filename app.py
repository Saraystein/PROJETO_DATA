from flask import Flask, request, jsonify
import re

app = Flask(
    __name__,
    static_folder='static',
    static_url_path=''
)

@app.route('/')
def index():
    return app.send_static_file('index.html')

def iso_para_br_regex(data_iso):
    match = re.fullmatch(
        r'(?:'
        r'(?:19|20)(?:[02468][048]|[13579][26])-02-29|'
        r'(?:19|20)\d{2}-02-(0[1-9]|1\d|2[0-8])|'
        r'(?:19|20)\d{2}-(01|03|05|07|08|10|12)-(0[1-9]|[12]\d|3[01])|'
        r'(?:19|20)\d{2}-(04|06|09|11)-(0[1-9]|[12]\d|30)'
        r')',
        data_iso
    )
    if not match:
        return None
    ano, mes, dia = data_iso.split("-")
    return f"{dia}/{mes}/{ano}"

def br_para_iso_regex(data_br):
    match = re.fullmatch(
        r'(?:'
        r'(29)/02/((?:19|20)(?:[02468][048]|[13579][26]))|'
        r'((0[1-9]|1\d|2[0-8]))/02/((?:19|20)\d{2})|'
        r'((0[1-9]|[12]\d|3[01]))/(01|03|05|07|08|10|12)/((?:19|20)\d{2})|'
        r'((0[1-9]|[12]\d|30)) /(04|06|09|11)/((?:19|20)\d{2})'
        r')',
        data_br
    )
    if not match:
        return None
    partes = re.findall(r'\d+', data_br)
    if len(partes) == 3:
        dia, mes, ano = partes
        return f"{ano}-{mes}-{dia}"
    return None

@app.route('/convert/iso-to-br', methods=['POST'])
def convert_iso_to_br():
    data = request.get_json(force=True)
    data_iso = data.get("date", "")
    converted = iso_para_br_regex(data_iso)
    if converted:
        return jsonify({"converted": converted})
    return jsonify({"error": "Data ISO inválida. Use yyyy-mm-dd."}), 400

@app.route('/convert/br-to-iso', methods=['POST'])
def convert_br_to_iso():
    data = request.get_json(force=True)
    data_br = data.get("date", "")
    converted = br_para_iso_regex(data_br)
    if converted:
        return jsonify({"converted": converted})
    return jsonify({"error": "Data BR inválida. Use dd/mm/yyyy."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
