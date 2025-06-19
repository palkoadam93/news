from flask import Flask, jsonify
import json

app = Flask(__name__)

# Összes hír röviden
@app.route('/api/news')
def get_all_news():
    with open('news.json', encoding='utf-8') as f:
        data = json.load(f)
        # Csak a rövid nézet mezői
        short_news = [
            { "id": n["id"], "title": n["title"], "summary": n["summary"], "date": n["date"] }
            for n in data
        ]
        return jsonify(short_news)

# Egy hír részletesen
@app.route('/api/news/<int:news_id>')
def get_news_by_id(news_id):
    with open('news.json', encoding='utf-8') as f:
        data = json.load(f)
        news_item = next((n for n in data if n["id"] == news_id), None)
        if news_item:
            return jsonify(news_item)
        return jsonify({ "error": "Hír nem található" }), 404

if __name__ == '__main__':
    app.run(debug=True)
