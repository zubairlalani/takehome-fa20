import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  constructor(props){
    super(props)
    this.state = {
        "count" : props.count
    }
  }
  render() {
    return (
      <div>
        {this.state.count+" "}
        <button onClick={this.handleIncrement}>+</button>
        <button onClick={this.handleDecrement}>-</button>
       </div> 
        //{this.state.count}
    )
  }


  handleIncrement = () => {
    this.setState((prevState) => ({count: prevState.count + 1}));
  }

  handleDecrement = () => {
    this.setState((prevState) => ({count: prevState.count - 1}));
  }
}

export default Counter
