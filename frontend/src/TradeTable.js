import React, { Component } from "react";
import axios from "axios";

class TradeTable extends Component {
    constructor() {
        super();
        this.state = {
            trades: [],
            openPositions: [],
        };
    }

    // componentDidMount() {
    //     this.fetchData();
    // }

    fetchData = () => {
        axios
            .get("trades/")
            .then((res) => {
                console.log("data", res.data);
                const { trades, open_positions } = res.data;
                console.log("trades", trades);
                this.setState({ trades, openPositions: open_positions });
            })
            .catch((error) => {
                console.log(error);
            });
    };

    render() {
        return (
            <div>
                <h2>Trades</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>Type</th>
                            <th>Symbol</th>
                            <th>Quantity</th>
                            <th>Purchase Price</th>
                            <th>Current Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.trades.map((trade, index) => (
                            <tr key={index}>
                                <td>{trade.time}</td>
                                <td>{trade.type}</td>
                                <td>{trade.symbol}</td>
                                <td>{trade.quantity}</td>
                                <td>{trade.purchase_price}</td>
                                <td>{trade.current_price}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <h2>Open Positions</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.openPositions.map((position, index) => (
                            <tr key={index}>
                                <td>{position.symbol}</td>
                                <td>{position.quantity}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <h3>Refresh</h3>
                <button onClick={this.fetchData}>Refresh</button>
            </div>
        );
    }
}

export default TradeTable;
