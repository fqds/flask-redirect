from flask import Flask,redirect
import config
import logging
app = Flask(__name__)

@app.errorhandler(404)
def hello(_):
    return redirect(config.TO_URL, code=302)

logging.basicConfig(level=logging.INFO, filename=config.PATH + 'log.log',filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("Starting application")

if __name__ == '__main__':
    if config.WITH_CERT: context = (config.CERT_PATH+'fullchain.pem', config.CERT_PATH+'privkey.pem')
    else: context = None
    app.run(host=config.FROM_HOST, port=config.FROM_PORT, ssl_context=context)