from run_helper import app

from app.routes.simulations.simulate_user_test_case_1_blueprint import simulate_user_test_case_1_blueprint

app.register_blueprint(simulate_user_test_case_1_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
