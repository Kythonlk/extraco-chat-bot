from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if not session.get('company_number'):
        # If the user hasn't provided a company number, ask for it.
        session['company_number'] = True
        msg.body("Hello, please tell me your company number.")

    else:
        company_number = session.get('company_number')
        
        if company_number == "001":
            # Respond based on company number 001.
            if '1' in incoming_msg:
                msg.body("You said 001, your company is Sewa, and please select a project:\n1. Fiberglass\n2. Precast")
                session['project_selected'] = True
            else:
                msg.body("Please select a valid project option (1 or 2).")

        elif company_number == "002":
            # Respond based on company number 002.
            if '1' in incoming_msg:
                msg.body("You said 002, your company is Dewa, and please select a project:\n1. Fiberglass\n2. Precast")
                session['project_selected'] = True
            else:
                msg.body("Please select a valid project option (1 or 2).")

        elif not session.get('project_selected'):
            msg.body("Please provide a valid company number (001 or 002).")

    return str(resp)

if __name__ == '__main__':
    app.run(port=4000)

