import uuid

from flask import render_template, jsonify, request

from app import app, db
from app.models import Urls


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/submit_url', methods=['POST'])
def submit_url():
    try:
        data = request.get_json()
        long_url = data.get('longUrl')
        short_url = data.get('shortUrl')
        is_evil = data.get('isEvil')
        print("Received", long_url, short_url, is_evil)

        if long_url is None or len(long_url) > 128:  # todo check if valid url (via regex)
            return jsonify({'message': 'Please provide valid URL'}), 404

        # validate short url and check datatype of is_evil

        if len(short_url) == 0:
            short_url = uuid.uuid4().hex[:6]

        new_url = Urls(longUrl=long_url, shortUrl=short_url, isEvil=is_evil)
        db.session.add(new_url)
        db.session.commit()
        return jsonify({'message': 'URL submitted successfully'}), 200

    except Exception as e:
        return jsonify({'message': f"URL is not unique most likely: {e}"}), 500


@app.route('/urls')
def get_urls():
    try:
        urls = Urls.query.order_by(Urls.timestamp_utc.desc()).all()
        urls_dict = [url.to_dict() for url in urls]
        return jsonify({"data": urls_dict})
    except Exception as e:
        # log the error here
        return jsonify({'message': f"Error: {e}"}), 500


@app.route('/delete_url', methods=['POST'])
def deleteUrl():
    pass
