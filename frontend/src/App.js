import React from "react";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            symbol: "",
            quantity: "",
            price: "",
            type: "",
            time: "",
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ [event.target.name]: event.target.value });
    }

    handleSubmit(event) {
        event.preventDefault();

        axios
            .post("trades/", this.state)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Symbol:
                    <input
                        type="text"
                        name="symbol"
                        onChange={this.handleChange}
                    />
                </label>
                <label>
                    Quantity:
                    <input
                        type="text"
                        name="quantity"
                        onChange={this.handleChange}
                    />
                </label>
                <label>
                    Price:
                    <input
                        type="text"
                        name="price"
                        onChange={this.handleChange}
                    />
                </label>
                <label>
                    Time:
                    <input
                        type="text"
                        name="time"
                        onChange={this.handleChange}
                    />
                </label>
                <label>
                    Type:
                    <select
                        type="text"
                        name={this.state.type}
                        onChange={this.handleChange}
                    >
                        <option value="buy">Buy</option>
                        <option value="sell">Sell</option>
                    </select>
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

export default App;
