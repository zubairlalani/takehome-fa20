import React, { Component } from 'react'
import Counter from './Counter'

class App extends Component {
  // YOUR CODE GOES BELOW
  
  render() {
    return (
      <div>
        <p>
        {this.props.id + ". "}
        {this.props.name+": "}
        <Counter count= {this.props.rating}/>
        </p>
      </div>
    )
  }
}

export default App
