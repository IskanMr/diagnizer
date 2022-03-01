
from flask import Flask, render_template, request, jsonify
from clips import Environment
import os
import json

class diagnizerCore:
    def init(self):
         self.dataPath = os.path.abspath(os.path.join(os.getcwd(), 'data'))
         rulePath = os.path.join(self.dataPath, 'symptomsRule.clp')
         self.env = Environment()
         self.env.load(rulePath)

    def reset(self):
        self.env.reset()

    def addSymptom(self, symptom):
        e = f'(assert (has_symptom {symptom}))'
        self.env.eval(e)

    def run(self):
        _ = self.env.run()

    def getDiseases(self):
        diseases = []

        for fact in self.env.facts():
            fact = str(fact)
            if "disease_is" in fact:
                disease = fact[1:-1].split(" ")[1]
                disease = disease.replace("_", " ")
                disease = disease.title()
                diseases.append(disease)
        return diseases

    def getSymptoms(self):
        symptoms = []

        for fact in self.env.facts():
            fact = str(fact)
            if "has_symptom" in fact:
                symptom = fact[1:-1].split(" ")[1]
                symptom = symptom.replace("_", " ")
                symptom = symptom.title()
                symptoms.append(symptom)
        return symptoms


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

diagnizer = diagnizerCore();
diagnizer.init();

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    diagnizer.reset()

    data = request.get_data(as_text=True)
    try:
        data = json.loads(data)
        for symptom in data['symptoms']:
            symptom = symptom.replace(' ', '_').lower()
            diagnizer.addSymptom(symptom)

        diagnizer.run()
        diseases = diagnizer.getDiseases()

        return jsonify({
            'status': 'success',
            'diseases': diseases
        })
    except:
        return jsonify({
            'status': 'error'
        })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)