{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6bed228b-e143-4e56-b1de-c3ff3e67216d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\arung\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,request, url_for, redirect, render_template\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "import joblib\n",
    "\n",
    "# Load the model using joblib\n",
    "\n",
    "\n",
    "app = Flask(__name__,template_folder=\"templates\")\n",
    "model = joblib.load('fraud_detection_model.pkl')\n",
    "#model=pickle.load(open('fraud_detection_model.pkl','rb'))\n",
    "\n",
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "\n",
    "@app.route('/predict',methods=['POST','GET'])\n",
    "def predict():\n",
    "    int_features=[float(x) for x in request.form.values()]\n",
    "    final=[np.array(int_features)]\n",
    "    print(int_features)\n",
    "    print(final)\n",
    "    prediction=model.predict(final)\n",
    "    output=prediction[0]\n",
    "\n",
    "    if output== \"Fraud\":\n",
    "        return render_template('result.html',pred='Fraud')\n",
    "    else:\n",
    "        return render_template('result.html', pred='Not Fraud')\n",
    "@app.route('/pred')\n",
    "def pred():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eff2c043-9727-4637-a482-d6d905dc8f84",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
