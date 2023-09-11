from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ner', methods=['POST'])
def ner_endpoint():
    try:
        # STT 서버로부터 데이터 수신
        data = request.json

        # 수신된 데이터 중 텍스트 부분 추출
        text = data.get('text', '')

        # 텍스트를 공백으로 분할하여 단어 목록 생성
        words = text.split()

        if words:
            # 마지막 단어를 [MASK]로 수정
            words[-1] = '[MASK]'
            modified_text = ' '.join(words)
            print(text)
            print('\n'+modified_text)

            # 수정된 데이터를 STT 서버로 반환
            return jsonify(modified_text=modified_text), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify(error='데이터에 텍스트가 없습니다.'), 400

    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)