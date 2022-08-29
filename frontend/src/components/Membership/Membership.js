import React, { memo } from 'react';
import Cards from 'react-credit-cards';
import 'react-credit-cards/es/styles-compiled.css';
import { useSelector } from 'react-redux';
import { selectIsAuthenticated } from '../../features/auth/authSlice';
import { Navigate } from 'react-router-dom';

class PaymentForm extends React.Component {
  state = {
    cvc: '',
    expiry: '',
    focus: '',
    name: '',
    number: '',
  };
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    if (
      !(
        this.state.number.length > 0 &&
        this.state.cvc.length > 0 &&
        this.state.name.length > 0 &&
        this.state.expiry.length > 0
      )
    ) {
      alert('Invalid');
    } else {
      (async () => {
        const rawResponse = await fetch(
          'http://localhost:8000/api/membership',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
              authorization: `Token ${localStorage.getItem('jwt')}`,
            },
            body: JSON.stringify({
              number: this.state.number,
              cvc: this.state.cvc,
              name: this.state.name,
              expiry: this.state.expiry,
            }),
          }
        );
        const content = await rawResponse.json();
        alert(content);
      })();
    }
  }

  isString(x) {
    return /^[a-zA-Z_ ]*$/.test(x);
  }

  isNumeric(number) {
    return +number === +number;
  }

  handleInputFocus = (e) => {
    this.setState({ focus: e.target.name });
  };

  handleInputChangeString = (e) => {
    const { name, value } = e.target;
    if (this.isString(value)) {
      this.setState({ [name]: value });
    }
  };
  handleInputChangeNumber = (e) => {
    const { name, value } = e.target;
    if (this.isNumeric(value)) {
      this.setState({ [name]: value });
    }
  };

  render() {
    return (
      <div className="editor-page">
        <div className="container page">
          <div className="row">
            <div className="col-md-10 offset-md-1 col-xs-12">
              <div id="PaymentForm">
                <Cards
                  cvc={this.state.cvc}
                  expiry={this.state.expiry}
                  focused={this.state.focus}
                  name={this.state.name}
                  number={this.state.number}
                />
                <br />
                <form onSubmit={this.handleSubmit}>
                  <input
                    value={this.state.name}
                    className="form-group form-control form-control-lg"
                    type="text"
                    name="name"
                    maxLength="22"
                    placeholder="Name"
                    onChange={this.handleInputChangeString}
                    onFocus={this.handleInputFocus}
                    required
                  />
                  <input
                    value={this.state.number}
                    className="form-group form-control form-control-lg"
                    type="tel"
                    name="number"
                    maxLength="16"
                    placeholder="Card Number"
                    onChange={this.handleInputChangeNumber}
                    onFocus={this.handleInputFocus}
                    required
                  />
                  <input
                    value={this.state.cvc}
                    className="form-group form-control form-control-lg"
                    type="tel"
                    name="cvc"
                    maxLength="3"
                    placeholder="cvc"
                    onChange={this.handleInputChangeNumber}
                    onFocus={this.handleInputFocus}
                    required
                  />
                  <input
                    value={this.state.expiry}
                    className="form-group form-control form-control-lg"
                    type="tel"
                    name="expiry"
                    maxLength="4"
                    placeholder="expiry"
                    onChange={this.handleInputChangeNumber}
                    onFocus={this.handleInputFocus}
                    required
                  />
                  <input
                    className="btn btn-lg pull-xs-right btn-primary"
                    type="submit"
                    value="Submit"
                  />
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

function MainView() {
  // Redirect if not authenticated
  const isAuthenticated = useSelector(selectIsAuthenticated);
  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  return (
    <div>
      <PaymentForm />
    </div>
  );
}
export default memo(MainView);
