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
    """
    
    """
    match = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', data_iso)
    if not match:
        return None
    ano, mes, dia = match.groups()
    return f"{dia}/{mes}/{ano}"

def br_para_iso_regex(data_br):
    """
    
    """
    match = re.fullmatch(r'(\d{2})/(\d{2})/(\d{4})', data_br)
    if not match:
        return None
    dia, mes, ano = match.groups()
    return f"{ano}-{mes}-{dia}"

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
