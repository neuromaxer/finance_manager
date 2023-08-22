import React from "react";
import axios from "axios";
import TradeTable from "./TradeTable";
import "./App.css";

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
        console.log({ [event.target.name]: event.target.value });
    }

    handleSubmit(event) {
        event.preventDefault();

        axios
            .post("trades/", this.state)
            .then(function (response) {
                console.log("Post Response:", response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    render() {
        return (
            <div className="App-container">
                <div className="App-form-containter">
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
                                name="type"
                                onChange={this.handleChange}
                                defaultValue={"buy"}
                            >
                                <option value="buy">Buy</option>
                                <option value="sell">Sell</option>
                            </select>
                        </label>
                        <input
                            className="App-submit"
                            value="Submit"
                            type="submit"
                        />
                    </form>
                </div>
                <TradeTable />
            </div>
        );
    }
}

export default App;
