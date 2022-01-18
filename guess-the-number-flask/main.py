from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def game():
    """
        Return proper value provided by user.

        :rtype: html input

        :return: value provided by user from ["too small", "too big", "you won"]

        """
    if request.method == 'POST':
        min_number = int(request.form.get('min'))
        max_number = int(request.form.get('max'))
        guess = int(request.form.get('guess'))
        while True:
            if request.form.get('youwon'):
                return render_template('wingame.html')
            elif request.form.get('toobig'):
                max_number = guess
            elif request.form.get('toosmall'):
                min_number = guess

            guess = (max_number - min_number) // 2 + min_number

            return render_template('maingame.html', guess=guess, min=min_number, max=max_number)

    else:
        return render_template('maingame.html', guess='500', min='0', max='1000')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
