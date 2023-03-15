# This is a Web-App using Python, HTML and Flask
# To run locally using Visual Studio Code or on Heroku etc
# Created By Imran Patel

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the input value from the form
    storage_data = float(request.form['storage_data'])

    # Calculate the required number of agent servers
    hours_per_day = 12
    num_agents_per_server = 10
    num_mappings_per_agent = 5
    num_agents = 1
    mapping_speed = 1 # GB per hour/mapping

    # Calculate the required number of agent servers
    num_agent_servers_required = int(storage_data / (num_agents_per_server * num_mappings_per_agent * mapping_speed * num_agents * hours_per_day)) + 1
    
    # Render the results template with the calculated value
    return render_template('results.html', num_agent_servers=num_agent_servers_required)

if __name__ == '__main__':
    app.run(debug=True)
