from flask import Flask, render_template, request
import stripe, datetime

stripe_keys = {
    'secret_key': 'sk_test_fPHKYTWdK5ZhuxQ3me9TOndf',
    'publishable_key': 'pk_test_EUm15FduMZOImjeIy7dsKjdE'
}

stripe.api_key = stripe_keys['secret_key']
app = Flask(__name__)


@app.route('/')
def index():
    key = stripe_keys['publishable_key']
    # 取得charge全部資料
    charge_all = stripe.Charge.list(limit=100)
    charge_dic = {}
    charge_list = []
    for charge_data in charge_all:
        charge_dic['Amount'] = "$" + str(float(charge_data.amount) / 100) + " " + charge_data.currency.upper()
        charge_dic['Description'] = charge_data.description
        charge_dic['Name'] = charge_data.receipt_email
        charge_dic['Date'] = str(datetime.datetime.fromtimestamp(charge_data.created))
        charge_list.append(charge_dic)
        charge_dic = {}

    return render_template('index.html', **locals())


@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 1000
    # customer
    customer = stripe.Customer.create(
        email='test@gmail.com',
        source=request.form['stripeToken']
    )
    try:
        charge = stripe.Charge.create(
            customer=customer.id,
            capture='true',
            amount=amount,
            currency='usd',
            description='Demo Charge',
        )
        data="$" + str(float(amount) / 100) + " " + charge.currency.upper()
    except stripe.error.CardError as e:
        # The card has been declined
        body = e.json_body
        err = body['error']
        print
        "Status is: %s" % e.http_status
        print
        "Type is: %s" % err['type']
        print
        "Code is: %s" % err['code']
        print
        "Message is: %s" % err['message']

    return render_template('charge.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
