from flask import Flask, request, jsonify
import numpy as np
from scipy.optimize import curve_fit

app = Flask(__name__)

# ... (Your reflectance_equation function from the original code) ...

@app.route('/calculate', methods=['POST'])
def calculate():
  data = request.get_json()
  n_f = data['n_f']
  k_f = data['k_f']
  n_s = data['n_s']
  wavelengths = np.array(data['wavelengths'])
  reflectances = np.array(data['reflectances'])

  popt, pcov = curve_fit(reflectance_equation, wavelengths, reflectances, p0=[n_f, k_f, n_s, 100, 0], bounds=([1, 0, 1, 1, -np.pi], [5, 1, 5, 1000, np.pi]))

  n_f_fitted, k_f_fitted, n_s_fitted, d_fitted, phase_shift_fitted = popt

  return jsonify({
    'n_f_fitted': n_f_fitted,
    'k_f_fitted': k_f_fitted,
    'n_s_fitted': n_s_fitted,
    'd_fitted': d_fitted,
    'phase_shift_fitted': phase_shift_fitted
  })

if __name__ == '__main__':
  app.run(debug=True)
